#!/usr/bin/env python3
"""Pruebas de igstudio.py. Correr: python3 -m unittest discover -s skills/instagram-studio/scripts -p 'test_*.py'"""
from __future__ import annotations

import contextlib
import copy
import datetime as dt
import io
import json
import tempfile
import unittest
from pathlib import Path

import igstudio as g

MANANA = (g.hoy() + dt.timedelta(days=1)).isoformat()


def reel(**cambios) -> dict:
    p = {
        "id": "prueba-reel", "formato": "reel", "pilar": "ia-derecho", "espacio": "personal",
        "fecha": MANANA, "hora": "19:00",
        "gancho": "Construí mi propio sistema en una semana.",
        "descripcion": "Abogado y herramientas propias uniendo IA y Derecho. Si conoces a alguien que lo necesita, mándaselo.",
        "hashtags": ["abogados"], "portada": {"texto": "Mi sistema", "archivo": "portada.png"},
        "video": {"duracion_s": 55, "origen": "editor-studio", "relacion": "9:16", "sonido": True,
                  "ia_fotorrealista": False, "archivo": "reel.mp4"},
        "etiqueta_ia": False, "fuentes": [], "reescrito": True, "estado": "borrador",
    }
    p.update(cambios)
    return p


def carrusel(n: int = 6, **cambios) -> dict:
    p = {"id": "prueba-carrusel", "formato": "carrusel", "pilar": "ia-derecho", "fecha": MANANA, "hora": "13:00",
         "descripcion": "Cuatro herramientas en una vista.", "diapositivas": [{"texto": f"Paso {i}"} for i in range(1, n + 1)]}
    p.update(cambios)
    return p


def errores(p, hist=None, para=""):
    return g.revisar(p, hist or [], para)[0]


def avisos(p, hist=None, para=""):
    return g.revisar(p, hist or [], para)[1]


def tiene(lista, trozo) -> bool:
    return any(trozo in x for x in lista)


class Basicos(unittest.TestCase):
    def test_reel_valido(self):
        self.assertEqual(errores(reel()), [])

    def test_carrusel_valido(self):
        self.assertEqual(errores(carrusel()), [])

    def test_historias_no(self):
        self.assertTrue(tiene(errores(reel(formato="historia")), "Historias Studio"))

    def test_solo_personal(self):
        self.assertTrue(tiene(errores(reel(espacio="milla")), "solo cubre la cuenta personal"))

    def test_pilar_y_estado(self):
        self.assertTrue(tiene(errores(reel(pilar="gym")), "«pilar»"))
        self.assertTrue(tiene(errores(reel(estado="listo")), "«estado»"))

    def test_sin_texto(self):
        self.assertTrue(tiene(errores(reel(gancho="", descripcion="", portada={})), "no tiene texto"))

    def test_fecha_y_hora(self):
        self.assertTrue(tiene(errores(reel(fecha="17/11/2026")), "AAAA-MM-DD"))
        self.assertTrue(tiene(errores(reel(hora="7pm")), "HH:MM"))


class Limites(unittest.TestCase):
    def test_castorena(self):
        self.assertTrue(tiene(errores(reel(descripcion="Lo uso en Castorena")), "Castorena"))

    def test_clientes_y_asuntos(self):
        for t in ("Un cliente me pidió esto", "el expediente 1234 se resolvió", "Amparo 345/2025",
                  "lo que hago para INDEP", "Junta Especial 2", "folio A123"):
            self.assertTrue(tiene(errores(reel(descripcion=t)), "clientes ni datos de asuntos"), t)

    def test_fechas_no_son_expedientes(self):
        self.assertEqual(errores(reel(descripcion="Lo publiqué el 17/11/2026 y salió el 18/11/2026")), [])

    def test_insultos(self):
        self.assertTrue(tiene(errores(reel(descripcion="Esos diputados son unos idiotas")), "insulto"))

    def test_autoria_ia(self):
        for t in ("Este video lo hizo una IA", "Hecho con IA", "editado con inteligencia artificial",
                  "ChatGPT escribió este guion", "la IA me lo armó", "Lo hizo una IA y quedó increíble"):
            self.assertTrue(tiene(errores(reel(descripcion=t)), "la hizo una IA"), t)

    def test_lema_permitido(self):
        for t in ("Herramientas que construí uniendo IA y Derecho", "Uso IA en mi trabajo de abogado",
                  "Mi estudio de video, que construí yo"):
            self.assertFalse(tiene(errores(reel(descripcion=t)), "la hizo una IA"), t)

    def test_derecho_sin_fuente(self):
        self.assertTrue(tiene(errores(reel(descripcion="El artículo 123 dice que…")), "fuentes"))
        self.assertEqual(errores(reel(descripcion="El artículo 123 dice que…", fuentes=["https://www.diputados.gob.mx/"])), [])

    def test_codigo_y_tesis_de_programacion_o_maestria(self):
        self.assertEqual(errores(reel(descripcion="Escribí el código de mi sistema mientras terminaba mi tesis de maestría")), [])
        self.assertTrue(tiene(errores(reel(descripcion="El Código Civil Federal dice")), "fuentes"))

    def test_politica_pide_postura(self):
        self.assertTrue(tiene(errores(reel(pilar="politica")), "opinion_emi"))
        p = reel(pilar="politica", opinion_emi="Está mal planteada")
        self.assertFalse(tiene(errores(p), "opinion_emi"))
        self.assertTrue(tiene(avisos(p), "contenido político"))


class ReglasDeInstagram(unittest.TestCase):
    def test_anzuelos(self):
        for t in ("Comenta GUÍA y te mando el PDF", "Etiqueta a un amigo abogado", "Dale like si estás de acuerdo",
                  "Compártelo si te sirvió", "Sígueme para la parte 2"):
            self.assertTrue(tiene(errores(reel(descripcion=t)), "anzuelo"), t)

    def test_invitacion_genuina(self):
        for t in ("Si conoces a alguien que lo necesita, mándaselo.", "¿Cuál te sirve más? Te leo",
                  "Comenta qué herramienta usas tú"):
            self.assertFalse(tiene(errores(reel(descripcion=t)), "anzuelo"), t)

    def test_hashtags(self):
        p = reel(hashtags=["a", "b", "c"], descripcion="Texto #d #e")
        self.assertEqual(errores(p), [])
        p = reel(hashtags=["a", "b", "c"], descripcion="Texto #d #e #f")
        self.assertTrue(tiene(errores(p), "6 hashtags"))
        p = reel(hashtags=["#abogados", "abogados"], descripcion="#Abogados")  # el mismo cuenta una vez
        self.assertEqual(errores(p), [])

    def test_duracion(self):
        self.assertTrue(tiene(errores(reel(video={**reel()["video"], "duracion_s": 181})), "más de 3 min"))
        self.assertEqual(errores(reel(video={**reel()["video"], "duracion_s": 180})), [])
        self.assertTrue(tiene(avisos(reel(video={**reel()["video"], "duracion_s": 20})), "menos de 30 s"))
        self.assertTrue(tiene(errores(reel(video={**reel()["video"], "duracion_s": None})), "duracion_s"))

    def test_marca_de_agua(self):
        self.assertTrue(tiene(errores(reel(video={**reel()["video"], "origen": "tiktok"})), "marca de agua"))
        self.assertTrue(tiene(errores(reel(video={**reel()["video"], "marca_de_agua": True})), "marca de agua"))

    def test_gancho_obligatorio(self):
        self.assertTrue(tiene(errores(reel(gancho="")), "gancho"))

    def test_formato_y_sonido(self):
        a = avisos(reel(video={**reel()["video"], "relacion": "16:9", "sonido": False, "texto_mayoritario": True}))
        self.assertTrue(tiene(a, "9:16") and tiene(a, "mudos") and tiene(a, "texto cubre"))

    def test_etiqueta_ia(self):
        v = {**reel()["video"], "ia_fotorrealista": True}
        self.assertTrue(tiene(errores(reel(video=v)), "Información de IA"))
        self.assertFalse(tiene(errores(reel(video=v, etiqueta_ia=True)), "Información de IA"))
        c = carrusel(diapositivas=[{"texto": "a", "ia_fotorrealista": True}, {"texto": "b"}])
        self.assertTrue(tiene(errores(c), "Información de IA"))

    def test_carrusel_limites(self):
        self.assertTrue(tiene(errores(carrusel(1)), "de 2 a 20"))
        self.assertTrue(tiene(errores(carrusel(21)), "de 2 a 20"))
        self.assertEqual(errores(carrusel(20)), [])

    def test_descripcion_larga(self):
        self.assertTrue(tiene(avisos(reel(descripcion="palabra " * 300)), "Pautas"))

    def test_plantilla(self):
        self.assertTrue(tiene(avisos(reel(descripcion="En el mundo actual, es importante destacar esto")), "plantilla"))


class Duplicados(unittest.TestCase):
    def test_texto_pegado_de_otra_red(self):
        p = reel(texto_otras_redes={"tiktok": reel()["descripcion"]})
        self.assertTrue(tiene(errores(p), "tiktok"))
        p = reel(texto_otras_redes={"tiktok": "Una semana, un sistema propio. Parte 1."})
        self.assertEqual(errores(p), [])

    def test_casi_igual_a_publicado(self):
        hist = [{"id": "viejo", "descripcion": reel()["descripcion"], "gancho": reel()["gancho"]}]
        e, w = g.revisar(reel(), hist)
        self.assertTrue(tiene(e, "viejo") and tiene(w, "gancho casi igual"))


class Aprobacion(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.orig = g.CUENTA
        g.CUENTA = self.dir
        (self.dir / "publicados.json").write_text("[]", encoding="utf-8")
        self.ruta = self.dir / "semana.json"

    def tearDown(self):
        g.CUENTA = self.orig
        self.tmp.cleanup()

    def guardar(self, piezas):
        self.ruta.write_text(json.dumps({"piezas": piezas}, ensure_ascii=False), encoding="utf-8")

    def correr(self, *argv) -> tuple[int, str]:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            r = g.main(list(argv))
        return r, buf.getvalue()

    def test_sin_aprobar_no_se_entrega(self):
        self.guardar([reel()])
        r, out = self.correr("entregar", str(self.ruta), "prueba-reel")
        self.assertEqual(r, 1)
        self.assertIn("sin aprobación", out)

    def test_aprobar_exige_reescrito(self):
        self.guardar([reel(reescrito=False)])
        r, out = self.correr("aprobar", str(self.ruta), "prueba-reel", "--medio", "chat")
        self.assertEqual(r, 1)

    def test_aprobar_y_entregar(self):
        self.guardar([reel()])
        r, _ = self.correr("aprobar", str(self.ruta), "prueba-reel", "--medio", "chat de Claude")
        self.assertEqual(r, 0)
        r, out = self.correr("entregar", str(self.ruta), "prueba-reel")
        self.assertEqual(r, 0)
        self.assertIn(reel()["descripcion"], out)
        self.assertIn("#abogados", out)
        self.assertIn("Etiqueta «Información de IA»: no", out)

    def test_cambio_invalida_aprobacion(self):
        self.guardar([reel()])
        self.correr("aprobar", str(self.ruta), "prueba-reel", "--medio", "chat")
        dato = json.loads(self.ruta.read_text(encoding="utf-8"))
        for campo, valor in (("descripcion", "Otro texto distinto"), ("hora", "20:00"),
                             ("video", {**reel()["video"], "archivo": "otro.mp4"})):
            p = copy.deepcopy(dato["piezas"][0])
            p[campo] = valor
            self.assertTrue(tiene(g.revisar(p, [], "entrega")[0], "ya no vale"), campo)

    def test_fecha_pasada(self):
        ayer = (g.hoy() - dt.timedelta(days=1)).isoformat()
        self.assertTrue(tiene(errores(reel(fecha=ayer), para="entrega"), "ya pasó"))

    def test_aprobar_con_errores_no(self):
        self.guardar([reel(descripcion="Lo hice en Castorena")])
        r, _ = self.correr("aprobar", str(self.ruta), "prueba-reel", "--medio", "chat")
        self.assertEqual(r, 1)
        self.assertNotIn("aprobado_huella", self.ruta.read_text(encoding="utf-8"))

    def test_publicado_metricas_y_estado(self):
        r, _ = self.correr("publicado", "p1", "--pilar", "ia-derecho", "--formato", "reel", "--fecha", "2026-11-17",
                           "--hora", "19:00", "--texto", "hola")
        self.assertEqual(r, 0)
        r, _ = self.correr("publicado", "p1", "--metricas", "Visualizaciones=1200", "compartidos=14")
        self.assertEqual(r, 0)
        dato = json.loads((self.dir / "publicados.json").read_text(encoding="utf-8"))
        self.assertEqual(dato[0]["metricas"][0]["valores"], {"visualizaciones": 1200, "compartidos": 14})
        r, _ = self.correr("publicado", "p1", "--metricas", "vistas=muchas")
        self.assertEqual(r, 1)
        # estado.json con el contrato de Matriz de Redes
        (self.dir / "perfil.json").write_text(json.dumps(json.loads((self.orig / "perfil.json").read_text(encoding="utf-8"))),
                                              encoding="utf-8")
        orig_estado = g.ESTADO_RED
        g.ESTADO_RED = self.dir / "estado.json"
        try:
            r, _ = self.correr("estado")
            est = json.loads(g.ESTADO_RED.read_text(encoding="utf-8"))
        finally:
            g.ESTADO_RED = orig_estado
        self.assertEqual(r, 0)
        self.assertEqual(est["contrato"], "redes-estado/0.1.1")
        self.assertEqual(est["publicados"][0]["metricas"]["valores"]["compartidos"], 14)
        self.assertIn(est["cadencia"]["certeza"], ("oficial", "terceros", "criterio"))


class Semana(unittest.TestCase):
    CFG = {"balance": {"ia-derecho": 0.4, "lifestyle": 0.4, "politica": 0.2}, "max_por_dia": 1,
           "max_por_semana": 5, "min_por_semana": 2, "tolerancia_balance": 0.2}

    def test_dos_el_mismo_dia(self):
        e, _ = g.revisar_semana([reel(id="a"), carrusel(id="b", fecha=MANANA)], self.CFG)
        self.assertTrue(tiene(e, "piezas; el perfil permite 1"))

    def test_demasiadas(self):
        piezas = [reel(id=str(i), fecha=(g.hoy() + dt.timedelta(days=i)).isoformat()) for i in range(1, 7)]
        e, _ = g.revisar_semana(piezas, self.CFG)
        self.assertTrue(tiene(e, "6 piezas"))

    def test_balance_y_sin_reel(self):
        piezas = [carrusel(id=str(i), fecha=(g.hoy() + dt.timedelta(days=i)).isoformat()) for i in range(1, 4)]
        _, w = g.revisar_semana(piezas, self.CFG)
        self.assertTrue(tiene(w, "pilar lifestyle") and tiene(w, "ningún Reel"))

    def test_ejemplo_del_repositorio(self):
        piezas = g.lista_de(g.leer_json(g.SKILL / "assets" / "semana.ejemplo.json"))
        for p in piezas:
            self.assertEqual(errores(p), [], p["id"])


class Fuentes(unittest.TestCase):
    def test_fuentes_bien_formadas(self):
        d = g.leer_json(g.FUENTES)
        ids = [f["id"] for f in d["fuentes"]]
        self.assertEqual(len(ids), len(set(ids)))
        for f in d["fuentes"]:
            self.assertIn(f["grado"], ("oficial", "terceros"))
            self.assertTrue(f["url"].startswith("https://"))
            if f["auto"]:
                self.assertTrue(f["cita"], f["id"])
        self.assertTrue(g.fecha_ok(d["verificado"]))

    def test_referencias_citan_fuentes_que_existen(self):
        import re
        ids = {f["id"] for f in g.leer_json(g.FUENTES)["fuentes"]}
        for md in (g.SKILL / "references").glob("*.md"):
            for cita in re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", md.read_text(encoding="utf-8")):
                if cita.startswith(("redes-estado", "instagram-studio", "x-viral", "vox-studio", "editor-studio")):
                    continue
                if cita in ("editor-studio", "otra-app", "ia-derecho"):
                    continue
                self.assertIn(cita, ids, f"{md.name} cita «{cita}»")

    def test_comparable(self):
        self.assertIn(g.comparable("we don’t suppress"), g.comparable("<p>We don't  suppress content</p>"))


if __name__ == "__main__":
    unittest.main()
