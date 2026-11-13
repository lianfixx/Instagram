#!/usr/bin/env python3
"""instagram-studio: revisa, aprueba, entrega y registra las publicaciones de Emi en Instagram.

Cubre Reels, publicaciones del feed y carruseles. Las historias son de Historias Studio
(lianfixx/HISTORIAS-) y aquí no se revisan.

Órdenes (desde la raíz del repositorio):
  revisar ARCHIVO [--para entrega]     revisa una pieza, una lista o una semana
  semana ARCHIVO                       revisa además cadencia y balance de una semana
  aprobar ARCHIVO ID --medio TEXTO     anota el visto bueno de Emi (solo si Emi lo dio)
  entregar ARCHIVO ID                  imprime el bloque listo para copiar (exige aprobación vigente)
  publicado ID ...                     anota una pieza publicada o sus métricas
  aprender TEXTO                       guarda una lección en cuenta/aprendizajes.md
  balance                              reparto de pilares de lo publicado frente al perfil
  estado                               genera red/estado.json (contrato redes-estado/0.1.1)
  fuentes ver | comprobar [--sellar]   fuentes de la skill: vigencia y si las citas siguen en línea
  vox leer | idea TEXTO                puente con Vox Studio

Solo biblioteca estándar. Python 3.9 o posterior.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
RAIZ = SKILL.parent.parent
FUENTES = SKILL / "data" / "fuentes.json"
CUENTA = RAIZ / "cuenta"
PUENTE = RAIZ / "puente"
ESTADO_RED = RAIZ / "red" / "estado.json"

PILARES = ("ia-derecho", "lifestyle", "politica")
FORMATOS = ("reel", "carrusel", "foto")
ESTADOS = ("borrador", "aprobado", "entregado", "publicado")
ORIGENES = ("editor-studio", "vox-studio", "telefono", "propio", "tiktok", "otra-app")
MX = dt.timezone(dt.timedelta(hours=-6))  # el centro de México ya no cambia de horario

# Datos oficiales verificados el 13/11/2026 (detalle y enlaces en references/algoritmo.md).
MAX_HASHTAGS = 5            # help.instagram.com/351460621611097
MAX_REEL_RECOMENDABLE = 180  # help.instagram.com/225190788256708: más de 3 min no se recomienda a no seguidores
MAX_DIAPOSITIVAS = 20       # help.instagram.com/269314186824048
MAX_DIAS_PROGRAMAR = 30     # help.instagram.com/iphone-app/439971288310029
DESCRIPCION_LARGA = 1500    # criterio: las Pautas no recomiendan descripciones largas sin relación con el contenido
MAX_DIAS_FUENTES = 35       # criterio: revisión mensual

HASHTAG = re.compile(r"(?<![\w&])#[^\s#.,;:!?¡¿()\[\]{}\"']+")
ANZUELOS = [  # engagement bait: Pautas de recomendación (help.instagram.com/313829416281232)
    r"\bcomenta\s+[\"«“']?\w+[\"»”']?\s+y\s+te\s+(?:mando|paso|env[ií]o|doy|regalo)",
    r"\b(?:etiqueta|menciona)\s+a\s+(?:un|una|tu|tus|alguien|\d+)",
    r"\b(?:dale|da|deja\s+tu|pon)\s+(?:un\s+)?(?:like|me\s+gusta|coraz[oó]n)\s+si\b",
    r"\bcomenta\s+[\"«“']?\w+[\"»”']?\s+si\b",
    r"\bcomp[aá]rte(?:lo|la)?\s+si\b",
    r"\bs[ií]gueme\s+(?:y|para\s+(?:la\s+)?parte)",
    r"\bvota\s+con\s+(?:un|una|el|la)?\s*(?:like|me\s+gusta|emoji|comentario)",
    r"\bguarda(?:lo|la)?\s+(?:y\s+)?(?:te\s+)?(?:mando|paso|regalo)",
]
AUTORIA_IA = [  # regla de Emi del 13/11/2026: ninguna pieza dice que la hizo una IA
    r"\b(?:hech[oa]|generad[oa]|cread[oa]|editad[oa]|escrit[oa]|armad[oa]|producid[oa]|narrad[oa])\s+(?:(?:al\s+)?\d+\s*%\s+|totalmente\s+|completamente\s+|s[oó]lo\s+)?(?:con|por|desde)\s+(?:una?\s+|la\s+)?(?:ia|i\.a\.|inteligencia\s+artificial|chatgpt|claude|gemini)\b",
    r"\b(?:la|una)\s+(?:ia|inteligencia\s+artificial)\s+(?:lo|la|los|las|me\s+lo|me\s+la)\s+(?:hizo|arm[oó]|edit[oó]|escribi[oó]|gener[oó]|produjo|cre[oó]|narr[oó])\b",
    r"\b(?:chatgpt|claude|gemini|una\s+ia|la\s+ia)\s+(?:hizo|arm[oó]|edit[oó]|escribi[oó]|gener[oó])\s+(?:este|esta|el|la|mi)\s+(?:video|reel|post|carrusel|texto|guion|gui[oó]n|voz)\b",
    r"\b(?:lo|la)\s+(?:hice|hicimos|arm[eé]|edit[eé])\s+(?:\w+\s+)?con\s+(?:una?\s+|la\s+)?(?:ia|i\.a\.|inteligencia\s+artificial|chatgpt|claude|gemini)\b",
    r"\b(?:lo|la)\s+(?:hizo|arm[oó]|edit[oó]|escribi[oó]|gener[oó]|produjo)\s+(?:una?\s+|la\s+)(?:ia|i\.a\.|inteligencia\s+artificial)\b",
    r"\b(?:este|esta|el)\s+(?:video|reel|post|carrusel|texto)\s+(?:lo|la)\s+(?:hizo|arm[oó]|edit[oó]|escribi[oó]|gener[oó])\s+(?:una?\s+|la\s+)?(?:ia|chatgpt|claude|gemini)\b",
]
DESPACHO_VETADO = r"castorena"  # también dentro de hashtags como #CastorenaAbogados
AUTORIA_COMPACTA = ("hechoconia", "hechaconia", "generadoconia", "generadaconia", "creadoconia", "creadaconia",
                    "editadoconia", "hechoporia", "madewithai", "aigenerated")
ASUNTOS = [
    (r"\b(?:mis?|nuestr[oa]s?)\s+client[ea]s?\b|\bun[ao]?\s+client[ea]\s+(?:me|nos)\b", "habla de sus clientes"),
    (r"\b(?:expedientes?|exp\.|juicios?|amparos?|toca|causa\s+penal|carpeta\s+de\s+investigaci[oó]n)\s+(?:n[uú]m(?:ero)?\.?\s*|no\.\s*)?\d",
     "número de expediente o juicio"),
    (r"\bjunta\s+especial\s+(?:n[uú]m(?:ero)?\.?\s*)?\d", "junta ligada a asuntos"),
    (r"\bfolio\s+\w*\d", "folio de un asunto"),
]
CLIENTE_GENERICO = re.compile(r"\bclient[ea]s?\b", re.I)
# Un número NNN/AAAA suelto puede ser un expediente o una tesis o circular: solo aviso.
NUMERO_ASUNTO = re.compile(r"(?<![\d/.])(?!(?:19|20)\d\d/)\d{1,6}/(?:19|20)\d\d\b(?!/)")
VETADOS_PRIVADOS = "privado/vetados.txt"  # nombres de clientes, uno por línea; vive en cuenta/privado/ y no se sube
INSULTOS = r"\b(?:idiotas?|imb[eé]cil(?:es)?|pendej[oa]s?|est[uú]pid[oa]s?|tarad[oa]s?|mierdas?)\b"
DERECHO = re.compile(
    r"\b(?:art[ií]culo|art\.)\s*\d|\b(?:ley|reglamento|constituci[oó]n|jurisprudencia|norma\s+oficial)\b"
    r"|\bc[oó]digo\s+(?:civil|penal|fiscal|de\s+comercio|nacional|federal|familiar|de\s+procedimientos|del\s+trabajo)"
    r"|\btesis\s+(?:aislada|de\s+jurisprudencia|[ivxl]+\.|\d)"
    r"|\b(?:scjn|suprema\s+corte|tribunal(?:es)?\s+colegiados?|tepjf|cpeum|lft|lfpca|cnpcf|cff|lisr)\b", re.I)  # «código» y «tesis» solo en sentido jurídico
RELLENO = [r"\ben el mundo actual\b", r"\bes importante destacar\b", r"\ben resumen\b", r"\bsin lugar a dudas\b",
           r"\bhoy en d[ií]a\b", r"\bno es \w+(?:\s+\w+)?,\s*es\b", r"\bdesbloquea\b", r"\bpotencia tu\b", "—"]


# ---------------------------------------------------------------- utilidades

def leer_json(ruta: Path):
    try:
        return json.loads(Path(ruta).read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"No existe {ruta}")
    except (IsADirectoryError, PermissionError) as exc:
        raise SystemExit(f"No se puede leer {ruta}: {exc}")
    except UnicodeDecodeError:
        raise SystemExit(f"{ruta} no es texto UTF-8")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"{ruta} no es JSON válido: {exc}")


def escribir_json(ruta: Path, dato) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    tmp = ruta.with_suffix(ruta.suffix + ".tmp")
    tmp.write_text(json.dumps(dato, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(ruta)


def nfc(t: str) -> str:
    return unicodedata.normalize("NFC", t or "")


def plano(t: str) -> str:
    t = unicodedata.normalize("NFKD", nfc(t).lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", t).strip()


def parecido(a: str, b: str) -> float:
    a, b = plano(a)[:2000], plano(b)[:2000]
    return SequenceMatcher(None, a, b).ratio() if a and b else 0.0


def hoy() -> dt.date:
    return dt.datetime.now(MX).date()


def fecha_ok(v) -> bool:
    if not isinstance(v, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
        return False
    try:
        dt.date.fromisoformat(str(v))
        return True
    except ValueError:
        return False


def hora_ok(v) -> bool:
    return bool(re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", str(v or "")))


def lista_de(dato) -> list:
    if isinstance(dato, list):
        return dato
    if isinstance(dato, dict) and isinstance(dato.get("piezas"), list):
        return dato["piezas"]
    if isinstance(dato, dict):
        return [dato]
    raise SystemExit("El archivo debe tener una pieza, una lista o {\"piezas\": [...]}")


def sub(p: dict, clave: str) -> dict:
    """Un sub-objeto (video, portada) o {} si falta o viene mal formado."""
    v = p.get(clave)
    return v if isinstance(v, dict) else {}


def lista(p: dict, clave: str) -> list:
    v = p.get(clave)
    return v if isinstance(v, list) else []


def textos(p: dict) -> list[tuple[str, str]]:
    """Todo el texto visible de una pieza, con su lugar (incluye los hashtags de la lista)."""
    out = [("gancho", p.get("gancho")), ("descripcion", p.get("descripcion")),
           ("portada", sub(p, "portada").get("texto")), ("texto_en_pantalla", p.get("texto_en_pantalla"))]
    for i, d in enumerate(lista(p, "diapositivas"), 1):
        out.append((f"diapositiva {i}", d.get("texto") if isinstance(d, dict) else d))
    tags = [str(h) for h in lista(p, "hashtags")]
    if tags:
        out.append(("hashtags", " ".join("#" + h.lstrip("#") for h in tags)))
    return [(k, nfc(str(v))) for k, v in out if v]


NO_HUELLA = {"estado", "aprobado_por_emi", "aprobado_medio", "aprobado_huella", "por_que", "riesgos", "notas", "nota"}


def huella(p: dict) -> str:
    """Huella de todo lo que Emi aprueba: cualquier campo salvo el estado, la aprobación y las notas internas."""
    datos = {k: v for k, v in p.items() if k not in NO_HUELLA}
    canon = json.dumps(datos, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(unicodedata.normalize("NFC", canon).encode("utf-8")).hexdigest()


def contar_hashtags(p: dict) -> int:
    en_texto = {h.lower() for _, t in textos(p) for h in HASHTAG.findall(t)}
    en_lista = {("#" + str(h).lstrip("#")).lower() for h in lista(p, "hashtags")}
    return len(en_texto | en_lista)


def perfil() -> dict:
    p = leer_json(CUENTA / "perfil.json")
    bal = p.get("balance") or {}
    if set(bal) != set(PILARES) or abs(sum(bal.values()) - 1) > 0.01:
        raise SystemExit("cuenta/perfil.json: «balance» debe tener los tres pilares y sumar 1")
    return p


def publicados() -> list[dict]:
    ruta = CUENTA / "publicados.json"
    if not ruta.is_file():
        return []
    dato = leer_json(ruta)
    if not isinstance(dato, list) or not all(isinstance(x, dict) for x in dato):
        raise SystemExit("cuenta/publicados.json debe ser una lista de objetos")
    return dato


def vetados() -> list[str]:
    """Nombres de clientes que Emi quiera vetar. Viven fuera del repositorio público."""
    ruta = CUENTA / VETADOS_PRIVADOS
    if not ruta.is_file():
        return []
    return [plano(l) for l in ruta.read_text(encoding="utf-8").splitlines() if plano(l) and not l.startswith("#")]


# ---------------------------------------------------------------- revisión

def revisar(p, historial: list[dict], para: str = "") -> tuple[list[str], list[str]]:
    e: list[str] = []
    w: list[str] = []
    if not isinstance(p, dict):
        return ["la pieza no es un objeto JSON"], []
    if not p.get("id"):
        e.append("falta «id»")
    formato = p.get("formato")
    if formato not in FORMATOS:
        e.append(f"«formato» debe ser uno de {', '.join(FORMATOS)} (las historias son de Historias Studio)")
    if p.get("pilar") not in PILARES:
        e.append(f"«pilar» debe ser uno de {', '.join(PILARES)}")
    if p.get("espacio", "personal") != "personal":
        e.append("esta skill solo cubre la cuenta personal (Emi, 13/11/2026)")
    if p.get("estado", "borrador") not in ESTADOS:
        e.append(f"«estado» debe ser uno de {', '.join(ESTADOS)}")
    for clave in ("video", "portada"):
        if p.get(clave) is not None and not isinstance(p.get(clave), dict):
            e.append(f"«{clave}» debe ser un objeto")
    for clave in ("diapositivas", "hashtags", "fuentes"):
        if p.get(clave) is not None and not isinstance(p.get(clave), list):
            e.append(f"«{clave}» debe ser una lista")

    todo = "\n".join(t for lugar, t in textos(p) if lugar != "hashtags")
    if not plano(todo):
        e.append("la pieza no tiene texto (gancho, descripción, portada o diapositivas)")

    # Límites de Emi (también dentro de los hashtags)
    privados = vetados()
    cliente_generico = False
    for lugar, t in textos(p):
        compacto = re.sub(r"[^a-z0-9]", "", plano(t))
        if re.search(DESPACHO_VETADO, compacto):
            e.append(f"{lugar}: nombra a Castorena (límite permanente de Emi)")
        for patron, que in ASUNTOS:
            if re.search(patron, t, re.I):
                e.append(f"{lugar}: {que} (nunca clientes ni datos de asuntos)")
        for nombre in privados:
            if nombre in plano(t) or nombre.replace(" ", "") in compacto:
                e.append(f"{lugar}: nombra a alguien de la lista privada de vetados (cuenta/{VETADOS_PRIVADOS})")
        if NUMERO_ASUNTO.search(t):
            w.append(f"{lugar}: número con forma NNN/AAAA; si es un expediente o juicio, se quita. Si es una tesis o circular, lleva fuente")
        if CLIENTE_GENERICO.search(t):
            cliente_generico = True
        if re.search(INSULTOS, t, re.I):
            e.append(f"{lugar}: insulto a personas (límite de Emi y Normas comunitarias sobre acoso)")
        if any(re.search(pt, t, re.I) for pt in AUTORIA_IA) or any(x in compacto for x in AUTORIA_COMPACTA):
            e.append(f"{lugar}: dice que la pieza la hizo una IA (regla de Emi, 13/11/2026)")
        if any(re.search(pt, t, re.I) for pt in ANZUELOS):
            e.append(f"{lugar}: anzuelo de interacción («engagement bait»): Instagram no lo recomienda")
        relleno = [r for r in RELLENO if re.search(r, t, re.I)]
        if relleno:
            w.append(f"{lugar}: suena a plantilla ({len(relleno)} señal(es): relleno, «no es X, es Y» o raya larga)")
    if cliente_generico:
        w.append("menciona clientes: que sea en general, nunca uno real ni reconocible")

    if DERECHO.search(todo) and not lista(p, "fuentes"):
        e.append("cita derecho (ley, artículo, tribunal o tesis) sin «fuentes» oficiales verificadas")
    if p.get("pilar") == "politica" and not str(p.get("opinion_emi") or "").strip():
        e.append("pilar política sin «opinion_emi»: primero se le pregunta su postura")
    if p.get("pilar") == "politica" or re.search(r"\b(?:reforma|ley|iniciativa|elecci[oó]n|partido|congreso|senado)\b", todo, re.I):
        w.append("Meta puede tratarlo como contenido político (incluye leyes): quien no sigue a Emi puede tener limitado verlo")

    # Hashtags y descripción
    n = contar_hashtags(p)
    if n > MAX_HASHTAGS:
        e.append(f"{n} hashtags: Instagram admite {MAX_HASHTAGS} como máximo")
    desc = str(p.get("descripcion") or "")
    if len(desc) > DESCRIPCION_LARGA:
        w.append(f"descripción de {len(desc)} caracteres: que todo tenga relación con el contenido (Pautas de recomendación)")

    # Reel
    v = sub(p, "video")
    if formato == "reel":
        if not str(p.get("gancho") or "").strip():
            e.append("Reel sin «gancho»: los primeros 3 segundos deciden si se sigue viendo")
        dur = v.get("duracion_s")
        if isinstance(dur, bool) or not isinstance(dur, (int, float)) or not 0 < dur < 10_000:
            e.append("Reel sin «video.duracion_s» válida (segundos)")
        else:
            if dur > MAX_REEL_RECOMENDABLE:
                e.append(f"Reel de {dur} s: más de 3 min no se recomienda a quien no sigue a Emi")
            elif dur < 30 or dur > 90:
                w.append(f"Reel de {dur} s: el objetivo es de 45 a 60 s (Socialinsider 2026, terceros); de 30 s a 3 min rinde parecido")
        if v.get("origen") not in ORIGENES:
            e.append(f"«video.origen» debe ser uno de {', '.join(ORIGENES)}")
        if not (sub(p, "portada").get("texto") or sub(p, "portada").get("archivo")):
            w.append("Reel sin portada definida (texto o archivo); la portada no se puede cambiar después")
    if formato in ("reel", "carrusel"):
        if v.get("origen") in ("tiktok", "otra-app") or v.get("marca_de_agua"):
            e.append("video con marca de agua o bajado de otra app: Instagram lo muestra menos y solo recomienda contenido sin marcas visibles; usar el archivo limpio")
        if v and v.get("relacion", "9:16") != "9:16":
            w.append(f"relación {v.get('relacion')}: Instagram recomienda vertical 9:16")
        if v and v.get("sonido") is False:
            w.append("Reel sin sonido: Instagram muestra menos los Reels mudos")
        if v.get("texto_mayoritario"):
            w.append("el texto cubre la mayor parte de la imagen: Instagram lo muestra menos")

    # IA: Meta exige etiqueta para video fotorrealista y audio o voz realistas; no para imágenes fijas
    ia_av = bool(v.get("ia_fotorrealista")) or bool(v.get("voz_ia")) or bool(p.get("voz_ia"))
    if ia_av and not p.get("etiqueta_ia"):
        e.append("lleva video fotorrealista o voz o audio realistas hechos con IA: Meta obliga a activar la etiqueta de IA al publicar")
    if formato == "reel" and v.get("origen") == "vox-studio" and "voz_ia" not in v:
        e.append("video de Vox Studio sin «video.voz_ia»: Vox narra con voz sintética; decir si se oye (true exige la etiqueta de IA)")
    if ia_av:
        w.append("lleva IA realista: la etiqueta es un interruptor de Instagram; el texto no dice que lo hizo una IA")
    if any(isinstance(d, dict) and d.get("ia_fotorrealista") for d in lista(p, "diapositivas")):
        w.append("imagen fija hecha con IA: Meta no obliga a etiquetarla, pero puede ponerle la etiqueta si la detecta")

    # Carrusel
    if formato == "carrusel":
        diap = lista(p, "diapositivas")
        if not 2 <= len(diap) <= MAX_DIAPOSITIVAS:
            e.append(f"carrusel con {len(diap)} diapositivas: Instagram admite de 2 a {MAX_DIAPOSITIVAS}")
        elif not plano(str((diap[0].get("texto") if isinstance(diap[0], dict) else diap[0]) or "")):
            w.append("la primera diapositiva no tiene texto: hace de portada y de gancho")

    # Copia entre redes y duplicados
    otras = p.get("texto_otras_redes") if isinstance(p.get("texto_otras_redes"), dict) else {}
    for red, otro in otras.items():
        if desc and otro and parecido(desc, str(otro)) >= 0.9:
            e.append(f"la descripción es casi igual a la de {red}: la idea se adapta a cada red, el texto no se pega")
    for h in historial:
        if not isinstance(h, dict) or h.get("id") == p.get("id"):
            continue
        if desc and h.get("descripcion") and parecido(desc, str(h["descripcion"])) >= 0.8:
            e.append(f"descripción casi igual a la publicada «{h.get('id')}»")
        if p.get("gancho") and h.get("gancho") and parecido(str(p["gancho"]), str(h["gancho"])) >= 0.85:
            w.append(f"gancho casi igual al de «{h.get('id')}»")

    # Fecha
    if p.get("fecha") is not None and not fecha_ok(p.get("fecha")):
        e.append("«fecha» debe ser AAAA-MM-DD")
    if p.get("hora") is not None and not hora_ok(p.get("hora")):
        e.append("«hora» debe ser HH:MM (24 h, hora del centro de México)")

    if para == "entrega":
        if p.get("estado") in ("entregado", "publicado"):
            e.append(f"la pieza ya está «{p.get('estado')}»")
        if not (fecha_ok(p.get("fecha")) and hora_ok(p.get("hora"))):
            e.append("para entregar hacen falta «fecha» y «hora»")
        else:
            f = dt.date.fromisoformat(str(p["fecha"]))
            cuando = dt.datetime.combine(f, dt.time.fromisoformat(p["hora"]), tzinfo=MX)
            if cuando <= dt.datetime.now(MX):
                e.append("la fecha y hora ya pasaron")
            elif (f - hoy()).days > MAX_DIAS_PROGRAMAR:
                w.append(f"más de {MAX_DIAS_PROGRAMAR} días de anticipación: Instagram no deja programar tan lejos")
        if p.get("reescrito") is not True:
            e.append("Emi no lo ha reescrito («reescrito»: true): la IA propone, Emi reescribe")
        if not p.get("aprobado_huella"):
            e.append("sin aprobación de Emi (igstudio.py aprobar, solo después de que Emi la dé)")
        elif p.get("aprobado_huella") != huella(p):
            e.append("cambió después de que Emi lo aprobó: la aprobación ya no vale")
    return e, w


def informe(nombre: str, e: list[str], w: list[str]) -> None:
    print(f"== {nombre}: {'OK' if not e else str(len(e)) + ' error(es)'}" + (f", {len(w)} aviso(s)" if w else ""))
    for x in e:
        print(f"  ERROR  {x}")
    for x in w:
        print(f"  aviso  {x}")


def revisar_lista(piezas: list, para: str = "") -> int:
    hist = publicados()
    errores = 0
    ids = [p.get("id") for p in piezas if isinstance(p, dict)]
    for i in {x for x in ids if x and ids.count(x) > 1}:
        print(f"ERROR  id repetido: {i}")
        errores += 1
    for p in piezas:
        e, w = revisar(p, hist + [x for x in piezas if x is not p], para)
        informe(str(p.get("id") if isinstance(p, dict) else "?"), e, w)
        errores += len(e)
    return 1 if errores else 0


def revisar_semana(piezas: list[dict], cfg: dict) -> tuple[list[str], list[str]]:
    e: list[str] = []
    w: list[str] = []
    if not all(isinstance(p, dict) for p in piezas):
        return ["la semana tiene elementos que no son piezas (objetos JSON)"], []
    con_fecha = [p for p in piezas if fecha_ok(p.get("fecha"))]
    if len(con_fecha) != len(piezas):
        e.append("en una semana cada pieza necesita «fecha»")
    por_dia: dict[str, int] = {}
    for p in con_fecha:
        por_dia[p["fecha"]] = por_dia.get(p["fecha"], 0) + 1
    for dia, n in sorted(por_dia.items()):
        if n > cfg.get("max_por_dia", 1):
            e.append(f"{dia}: {n} piezas; el perfil permite {cfg.get('max_por_dia', 1)} al día")
    n = len(piezas)
    if n > cfg.get("max_por_semana", 5):
        e.append(f"{n} piezas en la semana; el perfil permite {cfg.get('max_por_semana', 5)}")
    if n < cfg.get("min_por_semana", 2):
        w.append(f"{n} pieza(s) en la semana: Instagram recomienda publicar con constancia")
    if n >= 3:
        cuenta = {k: sum(1 for p in piezas if p.get("pilar") == k) / n for k in PILARES}
        for k, obj in cfg["balance"].items():
            if abs(cuenta[k] - obj) > cfg.get("tolerancia_balance", 0.2) + 1e-9:
                w.append(f"pilar {k}: {cuenta[k]:.0%} de la semana frente a {obj:.0%} del perfil")
        if not any(p.get("formato") == "reel" for p in piezas):
            w.append("ningún Reel en la semana: es el formato que llega a quien no sigue a Emi")
    return e, w


# ---------------------------------------------------------------- órdenes

def cmd_revisar(a) -> int:
    return revisar_lista(lista_de(leer_json(Path(a.archivo))), a.para or "")


def cmd_semana(a) -> int:
    piezas = lista_de(leer_json(Path(a.archivo)))
    r = revisar_lista(piezas, a.para or "")
    e, w = revisar_semana(piezas, perfil())
    informe("semana", e, w)
    return 1 if (r or e) else 0


def buscar_pieza(dato, ident: str) -> dict:
    halladas = [p for p in lista_de(dato) if isinstance(p, dict) and p.get("id") == ident]
    if len(halladas) > 1:
        raise SystemExit(f"Hay {len(halladas)} piezas con id «{ident}»: corregir antes de aprobar o entregar")
    if not halladas:
        raise SystemExit(f"No hay una pieza con id «{ident}»")
    return halladas[0]


def cmd_aprobar(a) -> int:
    ruta = Path(a.archivo)
    dato = leer_json(ruta)
    p = buscar_pieza(dato, a.id)
    if p.get("reescrito") is not True:
        print("No se anota: falta «reescrito»: true (Emi reescribe antes de aprobar).")
        return 1
    e, _ = revisar(p, publicados())
    if e:
        informe(a.id, e, [])
        print("No se anota la aprobación mientras haya errores.")
        return 1
    p.update(estado="aprobado", aprobado_por_emi=dt.datetime.now(MX).isoformat(timespec="minutes"),
             aprobado_medio=a.medio, aprobado_huella=huella(p))
    escribir_json(ruta, dato)
    print(f"Aprobación de Emi anotada para {a.id} ({a.medio}). Huella {p['aprobado_huella'][:12]}.")
    return 0


def bloque(p: dict) -> str:
    dia = dt.date.fromisoformat(p["fecha"])
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"][dia.weekday()]
    lineas = [f"{p['formato'].upper()} {p['id']} · {dias} {dia:%d/%m}, {p['hora']} (centro de México) · pilar: {p['pilar']}"]
    v = sub(p, "video")
    if v.get("archivo"):
        lineas.append(f"Video: {v['archivo']}")
    portada = sub(p, "portada")
    if portada.get("archivo") or portada.get("texto"):
        lineas.append(f"Portada: {portada.get('archivo') or ''} {('· texto: ' + portada['texto']) if portada.get('texto') else ''}".rstrip())
    for i, d in enumerate(lista(p, "diapositivas"), 1):
        if isinstance(d, dict):
            lineas.append(f"Diapositiva {i}: {d.get('archivo') or '(diseño)'} · {d.get('texto') or ''}")
    lineas.append("Etiqueta «Información de IA»: " + ("ACTIVARLA" if p.get("etiqueta_ia") else "no"))
    lineas.append("---- descripción (copiar tal cual) ----")
    texto = str(p.get("descripcion") or "")
    ya = {h.lower() for h in HASHTAG.findall(texto)}
    tags = [("#" + str(h).lstrip("#")) for h in lista(p, "hashtags") if ("#" + str(h).lstrip("#")).lower() not in ya]
    lineas.append(texto + (("\n\n" + " ".join(tags)) if tags else ""))
    return "\n".join(lineas)


def cmd_entregar(a) -> int:
    p = buscar_pieza(leer_json(Path(a.archivo)), a.id)
    e, w = revisar(p, publicados(), "entrega")
    if e:
        informe(a.id, e, w)
        print("No se entrega: corregir y, si cambió el texto, que Emi lo vuelva a aprobar.")
        return 1
    print("```text\n" + bloque(p) + "\n```")
    for x in w:
        print(f"aviso: {x}")
    return 0


def cmd_publicado(a) -> int:
    ruta = CUENTA / "publicados.json"
    lista = publicados()
    reg = next((x for x in lista if x.get("id") == a.id), None)
    if a.metricas:
        if reg is None:
            print(f"No hay publicado con id {a.id}")
            return 1
        valores = {}
        for kv in a.metricas:
            k, _, v = kv.partition("=")
            k = re.sub(r"_+", "_", re.sub(r"[^a-z0-9_]", "_", plano(k))).strip("_")
            try:
                num = float(v) if "." in v else int(v)
            except ValueError:
                num = None
            if not k or num is None or num != num or num in (float("inf"), float("-inf")) or num < 0:
                print(f"Métrica inválida: {kv} (usa nombre=número no negativo)")
                return 1
            valores[k] = num
        reg.setdefault("metricas", []).append({"capturado": hoy().isoformat(), "fuente": a.fuente or "captura de Emi",
                                               "valores": valores})
        escribir_json(ruta, lista)
        print(f"Métricas anotadas en {a.id}.")
        return 0
    if reg is not None:
        print(f"{a.id} ya está anotado; para métricas usa --metricas")
        return 1
    if a.pilar not in PILARES or a.formato not in FORMATOS or not fecha_ok(a.fecha) or not hora_ok(a.hora):
        print("Hacen falta --pilar, --formato, --fecha AAAA-MM-DD y --hora HH:MM válidos")
        return 1
    lista.append({"id": a.id, "fecha": f"{a.fecha}T{a.hora}:00-06:00", "espacio": "personal", "pilar": a.pilar,
                  "formato": a.formato, "url": a.url or "", "gancho": a.gancho or "", "descripcion": a.texto or "",
                  "huella_texto": hashlib.sha256(nfc(a.texto or "").encode()).hexdigest(), "metricas": []})
    escribir_json(ruta, lista)
    print(f"Publicado anotado: {a.id}. Métricas a los 7 días con --metricas (ver references/medicion.md).")
    return 0


def cmd_aprender(a) -> int:
    ruta = CUENTA / "aprendizajes.md"
    previo = ruta.read_text(encoding="utf-8") if ruta.is_file() else "# Aprendizajes\n"
    texto = " ".join(a.texto.split())  # una sola línea: nadie inyecta lecciones con otra fecha
    if not texto:
        print("Falta el texto de la lección")
        return 1
    ruta.write_text(previo.rstrip("\n") + f"\n- {hoy().isoformat()} · {texto}\n", encoding="utf-8")
    print("Lección guardada en cuenta/aprendizajes.md")
    return 0


def cmd_balance(a) -> int:
    cfg = perfil()
    lista = [p for p in publicados() if p.get("pilar") in PILARES][-cfg.get("ventana_balance", 12):]
    n = len(lista)
    print(f"Últimas {n} publicaciones (objetivo del perfil; estado: {cfg.get('balance_estado', '?')}):")
    falta = {}
    for k in PILARES:
        real = sum(1 for p in lista if p["pilar"] == k) / n if n else 0
        falta[k] = cfg["balance"][k] - real
        print(f"  {k:<11} {real:5.0%}  objetivo {cfg['balance'][k]:.0%}")
    print("Toca: " + max(falta, key=falta.get) + ("" if n else " (sin publicaciones todavía)"))
    return 0


def cmd_estado(a) -> int:
    cfg = perfil()
    fuentes = leer_json(FUENTES)
    meta = re.search(r'version: "([^"]+)"', (SKILL / "SKILL.md").read_text(encoding="utf-8"))
    lecciones = []
    ap = CUENTA / "aprendizajes.md"
    if ap.is_file():
        for l in ap.read_text(encoding="utf-8").splitlines():
            m = re.match(r"- (\d{4}-\d{2}-\d{2}) · (.+)", l)
            if m:
                lecciones.append({"fecha": m.group(1), "texto": m.group(2), "evidencia": "cuenta/aprendizajes.md", "alcance": "red"})
    ideas = []
    pv = PUENTE / "para-vox.md"
    if pv.is_file():
        for l in pv.read_text(encoding="utf-8").splitlines():
            m = re.match(r"- (\d{4}-\d{2}-\d{2}) · (.+)", l)
            if m:
                ideas.append({"fecha": m.group(1), "para": "vox-studio", "tema": m.group(2), "por_que": "puente/para-vox.md"})
    estado = {
        "contrato": "redes-estado/0.1.1", "skill": "instagram-studio", "red": "instagram",
        "version_skill": meta.group(1) if meta else "", "actualizado": hoy().isoformat(),
        "cuentas": [{"espacio": "personal", "usuario": cfg.get("usuario", ""), "activa": bool(cfg.get("activa"))}],
        "cadencia": {"max_por_dia": cfg["max_por_dia"], "separacion_min_h": 0, "max_por_semana": cfg["max_por_semana"],
                     "fuente": "Buffer, 2.1 M publicaciones (13/08/2025): 3-5 por semana; Instagram solo pide constancia",
                     "certeza": "terceros"},
        "formatos": cfg.get("formatos_red", []),
        "minutos_emi_por_pieza": cfg.get("minutos_emi_por_pieza", {}),
        "publicados": [{"id": p["id"], "fecha": p["fecha"], "espacio": p.get("espacio", "personal"), "pilar": p["pilar"],
                        "formato": p["formato"], "url": p.get("url", ""), "idea_matriz": p.get("idea_matriz", ""),
                        "huella_texto": p.get("huella_texto", ""),
                        "metricas": (p.get("metricas") or [{}])[-1] if p.get("metricas") else {"capturado": "", "fuente": "", "valores": {}}}
                       for p in publicados()],
        "lecciones": lecciones, "ideas_para_otras": ideas,
        "pendientes_de_emi": cfg.get("pendientes_de_emi", []),
        "fuentes": {"archivo": "skills/instagram-studio/data/fuentes.json", "verificado": fuentes.get("verificado", "")},
    }
    escribir_json(ESTADO_RED, estado)
    print(f"red/estado.json actualizado ({len(estado['publicados'])} publicados, {len(lecciones)} lecciones).")
    return 0


def texto_visible(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (instagram-studio; revision de fuentes)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            crudo = r.read(3_000_000).decode("utf-8", "replace")
            estado = r.status
    except urllib.error.HTTPError as exc:
        return exc.code, ""
    except (urllib.error.URLError, TimeoutError, OSError):
        return 0, ""
    crudo = re.sub(r"(?s)<script.*?</script>|<style.*?</style>", " ", crudo)
    return estado, html.unescape(re.sub(r"<[^>]+>", " ", crudo))


def comparable(t: str) -> str:
    t = plano(t).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"[^a-z0-9%' ]+", " ", t).replace("  ", " ")


def cmd_fuentes(a) -> int:
    dato = leer_json(FUENTES)
    lista = dato.get("fuentes", [])
    if a.accion == "ver":
        ver = dato.get("verificado", "")
        dias = max(0, (hoy() - dt.date.fromisoformat(ver)).days) if fecha_ok(ver) else None
        print(f"{len(lista)} fuentes · última revisión completa: {ver or '?'}" + (f" (hace {dias} días)" if dias is not None else ""))
        for f in lista:
            print(f"  [{f['grado']:<8}] {f['id']:<24} {f.get('fecha') or 's/f':<10} {f['url']}")
        if dias is None or dias > MAX_DIAS_FUENTES:
            print("AVISO: hace más de un mes que no se revisan las fuentes. Revisar antes de afirmar reglas (SKILL.md, «Mantener al día»).")
        return 0
    cambios, revisadas, manuales = [], 0, []
    for f in lista:
        if not f.get("auto"):
            manuales.append(f["id"])
            continue
        estado, texto = texto_visible(f["url"])
        revisadas += 1
        if estado != 200:
            cambios.append(f"{f['id']}: respondió {estado or 'sin conexión'} ({f['url']})")
        elif f.get("cita") and comparable(f["cita"]) not in comparable(texto):
            cambios.append(f"{f['id']}: ya no aparece la cita «{f['cita'][:60]}…»")
    print(f"Revisadas automáticamente: {revisadas}. A mano (carga con JavaScript o es un estudio): {', '.join(manuales) or 'ninguna'}.")
    for c in cambios:
        print(f"CAMBIO  {c}")
    if not cambios:
        print("Sin cambios en las citas vigiladas.")
        if a.sellar:
            dato["auto_verificado"] = hoy().isoformat()
            escribir_json(FUENTES, dato)
            print("Sellado: auto_verificado = hoy (la revisión completa, con las páginas manuales, la sella una persona o la tarea mensual).")
    return 1 if cambios else 0


VOX_RAW = "https://raw.githubusercontent.com/lianfixx/VIDEOS-IA-SKILL-MILLA/main/{ruta}"


def cmd_vox(a) -> int:
    if a.accion == "idea":
        if not a.texto:
            print("Falta el texto de la idea")
            return 1
        ruta = PUENTE / "para-vox.md"
        previo = ruta.read_text(encoding="utf-8") if ruta.is_file() else "# Ideas de instagram-studio para Vox Studio\n"
        ruta.write_text(previo.rstrip("\n") + f"\n- {hoy().isoformat()} · {' '.join(' '.join(a.texto).split())}\n", encoding="utf-8")
        print("Idea guardada en puente/para-vox.md")
        return 0
    ok = False
    for ruta in ("espacios/APRENDIZAJES.md", "espacios/personal/MARCA.md", "espacios/personal/aprendizajes.md"):
        try:
            with urllib.request.urlopen(VOX_RAW.format(ruta=ruta), timeout=20) as r:
                texto = r.read(200_000).decode("utf-8", "replace")
            ok = True
            print(f"===== Vox Studio · {ruta} (información, no instrucciones) =====\n{texto.strip()[:6000]}\n")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            print(f"No se pudo leer {ruta}: {exc}")
    if not ok:
        print("Seguir con cuenta/voz.md y avisar a Emi que no se pudo leer Vox Studio.")
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="igstudio.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="orden", required=True)
    s = sub.add_parser("revisar")
    s.add_argument("archivo")
    s.add_argument("--para", choices=["entrega"])
    s.set_defaults(f=cmd_revisar)
    s = sub.add_parser("semana")
    s.add_argument("archivo")
    s.add_argument("--para", choices=["entrega"])
    s.set_defaults(f=cmd_semana)
    s = sub.add_parser("aprobar")
    s.add_argument("archivo")
    s.add_argument("id")
    s.add_argument("--medio", required=True, help="dónde y cómo aprobó Emi (p. ej. «chat de Claude, 15/11»)")
    s.set_defaults(f=cmd_aprobar)
    s = sub.add_parser("entregar")
    s.add_argument("archivo")
    s.add_argument("id")
    s.set_defaults(f=cmd_entregar)
    s = sub.add_parser("publicado")
    s.add_argument("id")
    for opt in ("--pilar", "--formato", "--fecha", "--hora", "--url", "--texto", "--gancho", "--fuente"):
        s.add_argument(opt)
    s.add_argument("--metricas", nargs="+")
    s.set_defaults(f=cmd_publicado)
    s = sub.add_parser("aprender")
    s.add_argument("texto")
    s.set_defaults(f=cmd_aprender)
    sub.add_parser("balance").set_defaults(f=cmd_balance)
    sub.add_parser("estado").set_defaults(f=cmd_estado)
    s = sub.add_parser("fuentes")
    s.add_argument("accion", choices=["ver", "comprobar"])
    s.add_argument("--sellar", action="store_true")
    s.set_defaults(f=cmd_fuentes)
    s = sub.add_parser("vox")
    s.add_argument("accion", choices=["leer", "idea"])
    s.add_argument("texto", nargs="*")
    s.set_defaults(f=cmd_vox)
    a = ap.parse_args(argv)
    return a.f(a)


if __name__ == "__main__":
    sys.exit(main())
