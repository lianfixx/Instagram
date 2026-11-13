# Usar la skill en cualquier IA

La skill es Markdown plano, JSON y un script de Python sin dependencias. No depende de nada exclusivo de una plataforma.

| Dónde | Cómo |
|---|---|
| **Claude Code** | Abrir el repositorio. La skill se carga desde `.claude/skills/instagram-studio` (`/instagram-studio`). |
| **claude.ai** | Descargar la carpeta `skills/instagram-studio` como .zip y subirla en Configuración → Capacidades → Skills. Antes, `python3 ia/check_skill.py skills/instagram-studio` debe salir limpio. Sin terminal, las órdenes de `igstudio.py` se cumplen a mano con [redaccion.md](redaccion.md). |
| **Codex y otras IA con `.agents/skills/`** | Puente en `.agents/skills/instagram-studio`. |
| **ChatGPT y Gemini (Proyectos, Gems)** | Pegar [`ia/INSTRUCCIONES_PROYECTO.md`](../../../ia/INSTRUCCIONES_PROYECTO.md) y subir `SKILL.md` con las referencias. |
| **Gemini CLI** | `GEMINI.md` en la raíz. |

Sin terminal, la IA revisa a mano lo mismo que el script: los errores de [pilares.md](pilares.md) y [redaccion.md](redaccion.md) y los límites oficiales de [algoritmo.md](algoritmo.md) §6. Nunca dice que algo pasó la revisión si no la corrió.

Si no puede escribir en el repositorio, termina con un bloque «Registro pendiente para el repositorio» que incluye la entrada de `CHANGELOG.md` con la línea `Agente:`.
