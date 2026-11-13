# Registro de cambios

Lo más reciente arriba. Formato en `ia/PROTOCOLO.md`, sección 3.

## 2026-11-13 · instagram-studio 1.0.1: correcciones de la auditoría independiente
- Agente: Claude Code (sesión en la nube)
- Solicitud: encargo de Emi del 13/11/2026: una auditoría adversarial independiente y corregir todo lo que encuentre.
- Revisor: un agente independiente. Leyó en la fuente primaria las páginas de la ayuda de Instagram, las de transparency.meta.com y las de instagram.com, abiertas con el Chrome de box, y los blogs y estudios con WebFetch. Encontró 18 hallazgos: 3 altos, 10 medios y 5 bajos.
- Cambios:
  - **Voz de IA.** La ayuda de Instagram exige la etiqueta para «A reel narrated with a realistic AI-generated voiceover». La voz sintética de Vox obliga a la etiqueta. El Reel 4 se narra con la voz de Emi o lleva la etiqueta. Nuevo campo `video.voz_ia`, obligatorio en videos de Vox. Las imágenes fijas ya no exigen la etiqueta, porque Meta no lo pide.
  - **Repositorio público.** Se quitó el nombre de un cliente del código y de las pruebas. Los nombres a vetar van en `cuenta/privado/vetados.txt`, que no se sube. Se quitó «después: empleo» de los objetivos públicos.
  - **Límites en hashtags.** Los límites de Emi ahora se revisan también en los hashtags (por ejemplo, `#CastorenaAbogados` o `#hechoconia`).
  - **Huella de aprobación.** Ahora cubre todos los campos visibles (etiqueta de IA, formato, pilar, video) y ya no hay colisiones.
  - **Bloque de entrega.** Ya no se pierden los hashtags que son prefijo de otro.
  - **Reglas del validador:**
    - menos falsos positivos: tesis, circulares, «la IA creó…», «me gusta si…» y «ratas del gimnasio»;
    - menos falsos negativos: «mi clienta», «lo hice con IA», «hecho 100% con IA», «Comenta SÍ si…», SCJN y LFT sin fuente;
    - un número NNN/AAAA suelto ahora da aviso, no error.
  - **Robustez:**
    - entradas mal formadas, NaN, métricas vacías o negativas, ids repetidos;
    - piezas ya entregadas o publicadas, y hora de hoy ya pasada;
    - lecciones e ideas forzadas a una sola línea.
  - **Referencias:**
    - «no se recomienda» queda separado de «se muestra menos»;
    - los anzuelos se citan en la FAQ de Creators;
    - los hashtags relevantes «can help you reach more people» (FAQ oficial);
    - el salto de 2 s es una señal, no una predicción;
    - «not just» en el reparto por seguidores;
    - Buffer 1.36× viene de datos de 2022 a 2024;
    - se añadió el dato de Socialinsider que contradice al de Buffer en alcance;
    - cadencia de 3 a 5 (Buffer) y 2 como mínimo (criterio);
    - la hora de las 8 p. m. viene de Metricool + HypeAuditor 2025;
    - duración objetivo única de 45 a 60 s;
    - impresiones según la API;
    - «Tu algoritmo», solo en inglés;
    - menús de la ayuda: «Add AI label» y «More options → Schedule this post».
  - El CI prueba Python 3.10 y 3.12. Se intentó con 3.9, pero el runner de GitHub (Ubuntu 26.04) ya no lo ofrece; 3.9.25 lo probó el auditor en local con `ia/verificar.py ci` → aprobado.
  - Fuentes nuevas: `creators-faq`, `ayuda-etiqueta-ia` y `metricool-playbook-2025`.
- **Errata de la entrada 1.0.0.**
  - Dice que las fuentes oficiales se leyeron «una por una». No es exacto: varias páginas de la ayuda y tres tarjetas de Meta no cargaron con las herramientas de esta sesión. Esas páginas las leyó después el auditor con el Chrome de box, salvo las tarjetas de Feed, Explore y Search, y algunas páginas de la ayuda (elegibilidad y métricas de publicaciones).
  - El README decía que todas las fuentes tenían fecha y cita. Ya se corrigió.
- Archivos: `skills/instagram-studio/scripts/{igstudio,test_igstudio}.py`, `skills/instagram-studio/SKILL.md`, `references/{algoritmo,estudios,mitos,playbook,redaccion,entrega,medicion,frontera}.md`, `data/fuentes.json`, `assets/semana.ejemplo.json`, `cuenta/{perfil.json,aprendizajes.md}`, `puente/{para-vox,PETICION-vox}.md`, `ia/INSTRUCCIONES_PROYECTO.md`, `.github/workflows/control.yml`, `red/estado.json`, `README.md` y este registro.
- Verificación:
  - `python3 ia/verificar.py ci` → aprobado (64 pruebas de igstudio).
  - Pruebas hostiles del auditor, corridas de nuevo → corregidas.
  - Cita de `creators-faq` → en línea el 13/11/2026.
- Pendiente:
  - Avisar a Emi y a Matriz de Redes que el Reel de Vox necesita la voz de Emi o la etiqueta.
  - Sin verificar: las tarjetas de Feed, Explore y Search, qué opción de contenido político viene por defecto en México, y el límite de caracteres de la descripción.

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
