#!/usr/bin/env python3
"""Arranque y control de este repositorio (versión ligera del protocolo común entre IA).

  python3 ia/verificar.py inicio   resume rama, último commit, registro y vigencia de las fuentes
  python3 ia/verificar.py ci       pruebas, SKILL.md y puentes, registro con «Agente:», secretos y borradores privados

Solo biblioteca estándar. No instala frenos ni hooks: eso lo decide Emi (ver ia/REGLAS.md).
"""
from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SKILLS = ["skills/instagram-studio", ".claude/skills/instagram-studio", ".agents/skills/instagram-studio"]
SCRIPT = "skills/instagram-studio/scripts/igstudio.py"
SECRETOS = [
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"\bsk-[A-Za-z0-9_-]{20,}", r"\bgh[pousr]_[A-Za-z0-9]{30,}",
    r"\bAKIA[0-9A-Z]{16}\b", r"\bxox[baprs]-[A-Za-z0-9-]{10,}", r"\bAIza[0-9A-Za-z_-]{35}\b",
    r"\bIGQ[A-Za-z0-9_-]{40,}", r"\bEAA[A-Za-z0-9]{40,}",
    r"(?i)\b(sessionid|csrftoken|ds_user_id|password|contraseña)\s*[=:]\s*['\"]?[A-Za-z0-9%+/=_-]{16,}",
    r"\b[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z0-9]\d\b",
]
MAX_DIAS_FUENTES = 35


def git(*args: str) -> str:
    r = subprocess.run(["git", "-C", str(RAIZ), *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def edad_fuentes() -> tuple[str, int | None]:
    try:
        d = json.loads((RAIZ / "skills/instagram-studio/data/fuentes.json").read_text(encoding="utf-8"))
        fecha = d["verificado"]
        dias = max(0, (dt.date.today() - dt.date.fromisoformat(fecha)).days)
        return f"{len(d['fuentes'])} fuentes, revisadas el {fecha} (hace {dias} días)", dias
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        return f"no se pudieron leer ({exc})", None


def inicio() -> int:
    print(f"Repositorio: lianfixx/Instagram · rama {git('rev-parse', '--abbrev-ref', 'HEAD') or '?'}")
    print(f"Último commit: {git('log', '-1', '--format=%h %cs %s') or 'ninguno'}")
    actor = re.search(r"^IA-Actor:\s*(.+)$", git("log", "-1", "--format=%B"), re.M)
    print(f"Última IA: {actor.group(1) if actor else 'no declarada'}")
    sucio = git("status", "--porcelain")
    print("Cambios sin commit: " + (f"{len(sucio.splitlines())} archivo(s)" if sucio else "ninguno"))
    texto, dias = edad_fuentes()
    print(f"Fuentes: {texto}")
    if dias is None or dias > MAX_DIAS_FUENTES:
        print("  AVISO: hace más de un mes que no se revisan. Revisar antes de afirmar reglas (SKILL.md, «Mantener al día»).")
    registro = RAIZ / "CHANGELOG.md"
    if registro.is_file():
        titulos = [l for l in registro.read_text(encoding="utf-8").splitlines() if l.startswith("## ")][:3]
        print("Registro reciente:\n  " + "\n  ".join(titulos))
    print("Leer: AGENTS.md → ia/REGLAS.md → skills/instagram-studio/SKILL.md → cuenta/")
    return 0


def rastreados() -> list[Path]:
    salida = git("ls-files", "-z", "--cached", "--others", "--exclude-standard")
    if salida:
        return [RAIZ / p for p in salida.split("\0") if p]
    return [p for p in RAIZ.rglob("*") if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts]


def ci() -> int:
    fallas: list[str] = []

    def correr(nombre: str, cmd: list[str]) -> None:
        r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True)
        print(f"{'ok   ' if r.returncode == 0 else 'FALLA'} {nombre}")
        if r.returncode != 0:
            fallas.append(nombre)
            print((r.stdout + r.stderr).strip()[-2000:])

    correr("pruebas de igstudio", [sys.executable, "-m", "unittest", "discover", "-s", "skills/instagram-studio/scripts", "-p", "test_*.py"])
    correr("pruebas de verificar", [sys.executable, "-m", "unittest", "discover", "-s", "ia", "-p", "test_*.py"])
    correr("SKILL.md y puentes", [sys.executable, "ia/check_skill.py", *SKILLS])
    correr("fuentes legibles", [sys.executable, SCRIPT, "fuentes", "ver"])
    correr("perfil de la cuenta legible", [sys.executable, SCRIPT, "balance"])
    correr("ejemplo de semana sin errores", [sys.executable, SCRIPT, "semana", "skills/instagram-studio/assets/semana.ejemplo.json"])

    canon = (RAIZ / SKILLS[0] / "SKILL.md").read_text(encoding="utf-8")
    desc = re.search(r"^description: (.+)$", canon, re.M)
    for puente in SKILLS[1:]:
        d2 = re.search(r"^description: (.+)$", (RAIZ / puente / "SKILL.md").read_text(encoding="utf-8"), re.M)
        if not desc or not d2 or desc.group(1) != d2.group(1):
            fallas.append(f"{puente}: la descripción no coincide con la skill canónica")
    try:
        fuentes = json.loads((RAIZ / "skills/instagram-studio/data/fuentes.json").read_text(encoding="utf-8"))
        meta = re.search(r'fuentes_verificadas: "([\d-]+)"', canon)
        if not meta or meta.group(1) != fuentes["verificado"]:
            fallas.append("SKILL.md: fuentes_verificadas no coincide con data/fuentes.json → verificado")
    except (OSError, ValueError, KeyError, TypeError):
        fallas.append("data/fuentes.json ilegible")
    try:
        estado = json.loads((RAIZ / "red/estado.json").read_text(encoding="utf-8"))
        if estado.get("contrato", "").split("/")[0] != "redes-estado" or estado.get("red") != "instagram":
            fallas.append("red/estado.json: contrato o red inesperados")
    except (OSError, ValueError, AttributeError):
        fallas.append("red/estado.json ilegible (correr igstudio.py estado)")

    registro = RAIZ / "CHANGELOG.md"
    texto = registro.read_text(encoding="utf-8") if registro.is_file() else ""
    entradas = re.split(r"^## ", texto, flags=re.M)[1:]
    if not entradas:
        fallas.append("CHANGELOG.md sin entradas")
    for e in entradas:
        if not re.search(r"^- Agente: \S", e, re.M):
            fallas.append(f"CHANGELOG.md: la entrada «{e.splitlines()[0]}» no tiene línea «Agente:»")

    for ruta in rastreados():
        rel = ruta.relative_to(RAIZ).as_posix()
        if rel.startswith("cuenta/privado/") and rel != "cuenta/privado/.gitkeep":
            fallas.append(f"{rel}: los borradores privados no se suben (repositorio público)")
        if re.search(r"(^|/)(borradores?|drafts?)/|\.cookies$|(^|/)\.env$", rel):
            fallas.append(f"{rel}: parece un borrador o un archivo de sesión; no va en un repositorio público")
        if not ruta.is_file() or ruta.stat().st_size > 2_000_000:
            continue
        try:
            contenido = ruta.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for patron in SECRETOS:
            if re.search(patron, contenido):
                fallas.append(f"{rel}: posible secreto o dato personal ({patron[:24]}…)")
    for f in fallas:
        print(f"FALLA {f}")
    print("Control: " + ("aprobado" if not fallas else f"{len(fallas)} falla(s)"))
    return 1 if fallas else 0


if __name__ == "__main__":
    orden = sys.argv[1] if len(sys.argv) > 1 else ""
    sys.exit({"inicio": inicio, "ci": ci}.get(orden, lambda: (print(__doc__), 2)[1])())
