# Registro de cambios

Lo más reciente arriba. Formato en `ia/PROTOCOLO.md`, sección 3.

## 2026-11-13 · instagram-studio 1.0.0: primera versión
- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 13/11/2026: una skill propia para Instagram (Reels y feed), con el método de x-viral (`lianfixx/X`). Las respuestas de Emi llegaron por la sesión «Matriz de Redes»: solo la cuenta personal, sin Collab con MILLA; abogado con maestría en Alta Dirección; «full IA» desde el 07/11; objetivo de prestigio y después empleo; aprobación en un paquete semanal; crea la cuenta el 14 y 15/11; campaña de 4 videos que graba él (Matriz, DOF, Boletines y Vox); ganchos agresivos, sin avisos de ética gremial; «jamás en nada digas que lo armó una IA»; Reel de Vox solo en estilo collage o ilustrado.
- Cambios: la skill `skills/instagram-studio/` con sus referencias:
  - qué se sabe del ranking, solo de fuentes oficiales y sin pesos;
  - estudios de terceros;
  - 20 mitos con su veredicto;
  - pilares y límites, redacción, plan y campaña, entrega, medición, fronteras con las otras skills, portabilidad y encargos.
  
  Además:
  - `data/fuentes.json`: 43 fuentes con grado y cita.
  - `scripts/igstudio.py`: revisar, semana, aprobar con huella, entregar, publicado, aprender, balance, estado, fuentes y vox. Tiene 43 pruebas.
  - Estado de la cuenta en `cuenta/` y estado para Matriz de Redes en `red/estado.json` (contrato `redes-estado/0.1.1`).
  - Puentes con Vox Studio e Historias Studio, y la petición para Vox.
  - Reglas para cualquier IA (`ia/`), `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` y los puentes `.claude/skills` y `.agents/skills`.
  - Workflows `control.yml` (en cada push) y `fuentes.yml` (día 1 de cada mes).
  - Notas de la investigación en `docs/investigacion/`.
- Archivos: todo el repositorio, salvo el `README.md` inicial, que se reescribió.
- Verificación: `python3 ia/verificar.py ci` → aprobado; `igstudio.py fuentes comprobar` → aprobado (11 citas vigiladas en línea el 13/11/2026); fuentes oficiales → leídas una por una el 13/11/2026 por tres agentes; publicar en Instagram → no aplica (la cuenta aún no existe).
- Pendiente:
  - Emi: crear la cuenta de creador y pasar el usuario.
  - Emi: confirmar los pilares (se propone 40/40/20).
  - Emi: grabar los 4 videos con datos de demostración.
  - Emi: decidir si se crea la tarea mensual de revisión de fuentes y si Vox Studio aplica la petición del puente.
  - Primera pieza el 17/11/2026.
  - Auditoría independiente: en curso.
