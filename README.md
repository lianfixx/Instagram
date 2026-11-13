# instagram-studio · la skill de Instagram de Emi

Skill para planear, redactar, revisar, entregar para publicar y medir los **Reels, publicaciones del feed y carruseles** de la cuenta personal de Emi en Instagram. Pilares: **IA + Derecho en México**, **estilo de vida y gym** y **opinión política**. Sirve en cualquier IA.

Las **historias** no están aquí: son de [Historias Studio](https://github.com/lianfixx/HISTORIAS-).

## De dónde sale

Es hermana de [x-viral](https://github.com/lianfixx/X), la skill de X, y usa su mismo método: primero la fuente primaria, todas las preguntas juntas, una auditoría independiente, portabilidad y un validador con pruebas.

La diferencia es que **Instagram no publicó el código de su ranking**. Aquí no hay pesos. Cada regla dice si es **oficial** (Instagram o Meta), de **terceros** (estudio con método) o **criterio** (inferencia), y lo que no tiene sustento está en [mitos](skills/instagram-studio/references/mitos.md).

## Mapa

| Ruta | Qué es |
|---|---|
| [`skills/instagram-studio/SKILL.md`](skills/instagram-studio/SKILL.md) | La skill: reglas, flujo y a dónde ir según el encargo. |
| [`references/algoritmo.md`](skills/instagram-studio/references/algoritmo.md) | Lo que dicen Instagram y Meta, con su fuente. |
| [`references/estudios.md`](skills/instagram-studio/references/estudios.md) · [`mitos.md`](skills/instagram-studio/references/mitos.md) | Estudios de terceros y mitos. |
| [`references/playbook.md`](skills/instagram-studio/references/playbook.md) | Plan de la cuenta y campaña de lanzamiento. |
| [`references/redaccion.md`](skills/instagram-studio/references/redaccion.md) · [`pilares.md`](skills/instagram-studio/references/pilares.md) | Cómo se escribe una pieza; pilares y límites. |
| [`references/entrega.md`](skills/instagram-studio/references/entrega.md) · [`medicion.md`](skills/instagram-studio/references/medicion.md) | Cómo publica Emi y cómo se mide. |
| [`references/frontera.md`](skills/instagram-studio/references/frontera.md) | Qué hace esta skill y qué hacen Vox, Editor, Historias, x-viral y Matriz de Redes. |
| [`scripts/igstudio.py`](skills/instagram-studio/scripts/igstudio.py) | Revisión, aprobación con huella, entrega, registro, estado y fuentes. |
| [`data/fuentes.json`](skills/instagram-studio/data/fuentes.json) | Las fuentes, con su grado; fecha cuando la fuente la publica. Las que cargan sin JavaScript llevan una cita que GitHub vigila; las demás (Centro de ayuda, tarjetas de Meta, Mosseri) se revisan a mano cada mes. |
| [`cuenta/`](cuenta/README.md) | Estado de la cuenta: perfil, voz, aprendizajes y publicados. |
| [`red/estado.json`](red/README.md) | Estado para Matriz de Redes. |
| [`puente/`](puente/README.md) | Lo que esta skill deja para Vox Studio e Historias Studio. |
| [`ia/`](ia/REGLAS.md) | Reglas, protocolo entre IA, control e [instrucciones para ChatGPT y Gemini](ia/INSTRUCCIONES_PROYECTO.md). |
| [`docs/investigacion/`](docs/investigacion/) | Notas completas de la investigación del 13/11/2026. |

## Uso rápido

```bash
I="python3 skills/instagram-studio/scripts/igstudio.py"
$I balance                                         # qué pilar toca
$I semana cuenta/privado/2026-W47.json             # revisar una semana
$I aprobar cuenta/privado/2026-W47.json ID --medio "chat"   # anotar el visto bueno de Emi
$I entregar cuenta/privado/2026-W47.json ID        # bloque listo para copiar
$I fuentes ver                                     # fuentes y su vigencia
$I estado                                          # actualizar red/estado.json
python3 ia/verificar.py ci                         # control completo antes de un commit
```

Funciona con Python 3.9 o posterior y no tiene dependencias. Sin terminal, ver [portabilidad](skills/instagram-studio/references/portabilidad.md).

## Cómo se mantiene al día

- En cada push, GitHub corre el control ([`control.yml`](.github/workflows/control.yml)).
- El día 1 de cada mes, GitHub comprueba que las citas de las fuentes que cargan sin JavaScript sigan en línea ([`fuentes.yml`](.github/workflows/fuentes.yml)). La revisión completa (Centro de ayuda, tarjetas de Meta y Mosseri) es manual o una tarea programada, si Emi la aprueba. GitHub pausa los workflows programados tras 60 días sin actividad.

## Estado

Versión 1.0.1 (13/11/2026), con las correcciones de la auditoría independiente.

- **Probado:** el script y el control ([`CHANGELOG.md`](CHANGELOG.md)).
- **No probado todavía:** nada con una cuenta real, porque Emi la crea el 14-15/11; los menús de la app citados en la entrega; la tarea mensual completa.
- Ninguna IA inicia sesión en Instagram: Emi publica lo que la skill le entrega.

El repositorio es público. Contiene las reglas de trabajo de Emi, no borradores ni datos de terceros. Uso personal de Emiliano García Milla. Las fuentes citadas son de sus autores; aquí se enlazan, no se redistribuyen.
