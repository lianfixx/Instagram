# Instagram: cómo ordena y recomienda contenido. Solo fuentes oficiales (Reels, feed y carruseles; sin historias)

- Consulta: 13/11/2026. Todas las páginas se leyeron directamente en esa fecha, con WebFetch o con el Chrome sin interfaz de la caja (`browser_fetch`).
- Grado: **oficial** = Instagram/Meta (about.instagram.com, creators.instagram.com, help.instagram.com, transparency.meta.com, about.fb.com, developers.facebook.com, o la cuenta verificada de Adam Mosseri o de @creators).
- Las citas textuales van en inglés, como en el original, y tienen 25 palabras o menos. Ningún documento oficial publica porcentajes ni pesos de señales; no se añade ninguno.

---

## 1. Adam Mosseri y los blogs oficiales sobre ranking

### 1.1 «Instagram Ranking Explained» (versión vigente)
URL: https://about.instagram.com/blog/announcements/instagram-ranking-explained · Autor: Adam Mosseri · Fecha: **31/05/2023**. Es una actualización del post original de 2021; no encontré ninguna versión de 2025 en esa URL, que sigue mostrando la fecha de 2023. · Grado: oficial

| Afirmación | Cita textual |
|---|---|
| No hay un único algoritmo: cada superficie tiene el suyo. | "Instagram doesn't have a singular algorithm that oversees what people do and don't see on the app." |
| Feed: las señales más importantes, «aproximadamente en orden», son tu actividad, la información del post, la información de quien publica y tu historial con esa persona. | "The most important signals across Feed, roughly in order of importance, are: Your activity…" |
| Feed: las 5 predicciones principales. | "how likely you are to spend a few seconds on a post, comment on it, like it, share it, and tap on the profile photo." |
| Feed: se evita mostrar demasiados posts seguidos de la misma cuenta o demasiadas sugerencias seguidas. | "we try to avoid showing too many posts from the same person in a row" |
| Explore: las acciones clave que se predicen. | "The most important actions we predict in Explore include likes, saves, and shares." |
| Explore: la popularidad del post pesa más que en Feed. | "These signals matter much more in Explore than they do in Feed or in Stories." |
| Reels: las predicciones principales son reenviar, ver hasta el final, dar me gusta e ir a la página del audio. | "how likely you are to reshare a reel, watch a reel all the way through, like it, and go to the audio page" |
| Reels: Instagram usa encuestas de «¿vale la pena?». | "we survey people and ask whether they find a particular reel worth their time or fun" |
| Reels: qué se muestra menos. | "low-resolution or watermarked reels, reels that are muted or contain borders, reels that are majority text, or reels that have already been posted on Instagram." |
| Si una cuenta incumple las pautas de forma reiterada, deja de ser recomendable durante un tiempo. | "none of their posts will be eligible for recommendation for a period of time." |
| Sobre el «shadowban», Instagram dice que no suprime contenido para vender anuncios. | "we don't suppress content to encourage people to buy ads." |
| Instagram está probando avisos de alcance limitado por marca de agua. | "notifications to help creators understand when the reach of their reel may be limited due to a watermark" |

### 1.2 Mosseri: las tres señales principales (serie de videos sobre ranking)
- URL: https://www.instagram.com/p/DFFyRp-pINJ/ (cuenta verificada **@mosseri**) · Fecha: **21/01/2025** · Cómo lo verifiqué: leí el texto del caption con WebFetch directamente en instagram.com. No vi el video; solo leí el caption. · Grado: oficial
  - "the top three signals that matter most for ranking are watch time, likes and sends."
  - "likes are slightly more important for connected content, and sends are slightly more important for unconnected content."
  - El caption distingue el alcance «conectado» (seguidores) del «no conectado» (no seguidores) y recomienda revisar el tiempo medio de visualización, los me gusta por alcance y los envíos por alcance en Insights. Mosseri no da pesos ni multiplicadores: solo dice «slightly» (ligeramente).

### 1.3 Mosseri: «sends» (envíos por DM)
- URL: https://www.instagram.com/reel/C86WDnEuBjB/ (cuenta **@mosseri**) · Fecha: **02/07/2024** · Cómo lo verifiqué: leí el caption con `browser_fetch` en instagram.com. · Grado: oficial
  - Caption: "sends are one of the biggest signals we use in ranking and can help your reach over time." También dice: "Don't force it".
  - Según la transcripción que publicó Search Engine Journal (03/07/2024; es una fuente secundaria y no vi el audio), dice: "One of the most important signals we use in ranking is sends per reach."

### 1.4 La métrica «Visualizaciones» (Views)
- URL: https://www.instagram.com/p/C-X-fRPRl10/ (cuenta **@creators**) · Fecha: **07/08/2024** · Leí el caption con WebFetch: "a few changes you'll see in Insights over the next few weeks". La frase que circula, "We're introducing 'Views' as the primary metric across all formats…", aparece citada en Social Media Today (07/08/2024) como texto del post; yo no la vi completa en el caption. No encontré un post personal de Mosseri sobre este cambio.
- Confirmación técnica: https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights (consultada el 13/11/2026). Dice que impressions está "deprecated" para el contenido creado después del 2 de julio de 2024. · Grado: oficial

### 1.5 Blog de Creators: cómo se distribuyen los Reels y cómo crecen las cuentas pequeñas
URL: https://creators.instagram.com/blog/helping-creators-of-all-sizes-break-through · Fecha: **26/02/2025** · Grado: oficial
- Señales: "Signals include user activity like watch time, retention, shares, likes, and comments."
- Distribución por etapas a no seguidores: "initially recommended and shown to a small audience… the best-performing reels are then shown to a slightly wider audience".
- El alcance depende de la interacción, no del número de seguidores: "distributing content based on its engagement, not just the creator's follower count."
- Gancho y View Rate: "Start with a compelling hook in the first 3 seconds… monitor your View Rate" (se describe como el porcentaje de personas que siguen viendo después de los 3 s).
- Audio en fotos y carruseles: "adding audio to your posts can also help them be shown to more people."
- Frecuencia: "Post regularly. One of the most effective ways to grow is to post consistently." No da ninguna cifra de frecuencia.
- Los cambios de abril de 2024 para cuentas de cualquier tamaño ya están "fully launched".

### 1.6 Blog de Creators: «Finding success on reels in 2025»
URL: https://creators.instagram.com/blog/the-latest-with-instagram · Fecha: **21/01/2025** · Grado: oficial
- Recomendables hasta 3 min: "Previously, only reels up to 90 seconds were eligible for recommendation, but now reels up to 3 minutes will be eligible". Al principio aplicaba al editor en EE. UU.
- Fotos y carruseles con audio: "when you add audio to photos and carousels, they may also appear in the Reels tab."
- Igualdad de oportunidades: "creators of all sizes have an equal chance of breaking through"; "post original content consistently".

### 1.7 Contenido original: ampliación a fotos y carruseles
URL: https://creators.instagram.com/blog/rewarding-original-creators-on-instagram · Fecha: **30/04/2026** · Grado: oficial
- Los agregadores quedan fuera de las recomendaciones también en fotos y carruseles: "aggregators who primarily re-upload others' work in photos and carousel posts will no longer be eligible for recommendations".
- La regla se extiende desde Reels (2024): "The same protections we introduced to reels in 2024 will now apply to photos and carousels."
- Dato oficial: "75% of recommendations in the US now coming from original posts."
- Qué no cuenta como original: "just adding a border, watermark, subtitles, or a credit in the captions."
- Recuperación: "a significant percentage of their recently posted photos, carousels, and reels are considered original in a 30-day period" (se calcula de forma continua y se consulta en Account Status).
- No afecta a los seguidores: "This update does not impact how we show people content from accounts they follow."

### 1.8 Pautas de contenido original (página permanente)
URL: https://creators.instagram.com/original-content-guidelines · Sin fecha (pie «© 2026 Meta»; consultada el 13/11/2026) · Grado: oficial
- Definición: "Original content is work that you wholly created or reflects your unique perspective."
- Prueba práctica: "if someone could remove your contribution… and the content would virtually be the same, it probably needs more of you in it."
- Ediciones menores: "low-effort edits (e.g. borders, watermarks, speed changes, just crediting the original creator)".
- Consecuencia: "it may be ineligible to appear in recommendations to people who don't already follow you".
- Alternativa: para curar contenido ajeno sin editarlo, usar repost o compartir en historias.

### 1.9 Blog de Creators: recomendaciones y elegibilidad
URL: https://creators.instagram.com/blog/instagram-recommendations-eligibility-tips-creators · Fecha: **30/08/2022**, actualizado el **25/04/2023** · Grado: oficial. Las partes sobre formato siguen vigentes; la duración de 3 min fue actualizada después.
- Formato: "high-resolution, 9 x 16 vertical videos with no borders, where text does not cover the majority of the screen."
- Duración: "In order to be recommended, your content has to be 3 minutes or less."
- Primeros 3 s: "Pull the viewer in within the first 3 seconds".
- Búsqueda: "put these keywords and hashtags in the caption, not the comments."
- Solo se recomiendan cuentas públicas: "We only recommend content from public accounts".

### 1.10 Trial reels (lanzamiento)
URL: https://creators.instagram.com/blog/instagram-trial-reels y https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers/ · Fecha: **10/12/2024** · Grado: oficial
- "Trial reels will be shown to non-followers first."
- Métricas a las ~24 h: "Approximately 24 hours after you share a trial reel, you can view key engagement metrics".
- Compartir automáticamente con seguidores "based on the views it receives within the first 72 hours." (dato de 2024; la página de ayuda actual solo dice "soon after you publish").

### 1.11 Reinicio de recomendaciones
URL: https://about.instagram.com/blog/announcements/reset-instagram-content-suggestions · Fecha: **19/11/2024** (anunciado como prueba) · Grado: oficial
- "reset their recommendations… clear your recommended content across Explore, Reels and Feed and start fresh."
- Página de ayuda vigente: https://help.instagram.com/iphone-app/556617736965724 → "Resetting your suggested content can't be undone… suggestions will become more personalized again".

### 1.12 «Your Algorithm» (control de temas)
URL: https://about.instagram.com/blog/announcements/reels-algorithm-control · Grado: oficial. El texto lo leí con WebFetch; `browser_fetch` devolvió la página vacía.
- **10/12/2025**: lanzamiento en Reels, solo en EE. UU. ("This new feature is available starting today in the US").
- **15/04/2026**: llega a Explore, global en inglés ("One algorithm, reflected across surfaces").
- **10/06/2026**: "Your Algorithm is now live across all of Instagram, including Feed, Reels, and Explore."
- En Feed, los posts recomendados por interés llevan una etiqueta, por ejemplo «From Running».

### 1.13 Mosseri en Threads (2026)
- https://www.threads.com/@mosseri, leído con `browser_fetch` el 13/11/2026. Post del **27/10/2026** sobre el video largo («Features»): "we're testing and ramping up access slowly". Es una prueba de video horizontal largo; la prensa habla de hasta 90 min en EE. UU. y Brasil, pero ese límite no lo verifiqué en una fuente oficial. No es Reels.
- Su post de fin de año del 31/12/2025 sobre IA y autenticidad (estética «raw») **no lo pude leer en el original**: solo vi cobertura de prensa. Queda como no verificado.

---

## 2. Meta Transparency Center (tarjetas de sistemas de IA)

### 2.1 Reels (Reels Chaining)
URL: https://transparency.meta.com/features/explaining-ranking/ig-reels-chaining/ · **Actualizada el 11/11/2025** · Grado: oficial
- Proceso: reunir el inventario de candidatos → aplicar un modelo ligero → quedarse con unos 100 → calcular un puntaje de relevancia. Cita: "A lightweight model is run to select approximately 100 of the most relevant reels."
- Integridad: "remove content that is non-recommendable or that may go against our Community Guidelines."
- Algunas de las predicciones que enumera:
  - "How likely you are to watch less than three seconds of a reel". Sus señales incluyen "How many times the post has been skipped within two seconds of being opened".
  - "How likely you are to watch more than 95% of users who watched reels of the same length". Es retención relativa a la duración del reel.
  - Probabilidad de reenviar, de compartir fuera de Instagram, de comentar, de seguir al autor y de usar el audio del reel.
- Aviso de la propia tarjeta: "These models and their input signals are dynamic and they change frequently".

### 2.2 Explore
URL: https://transparency.meta.com/features/explaining-ranking/ig-explore/ · **Actualizada el 22/06/2026** · Grado: oficial
- Etapas: recuperación de hasta 1500 candidatos → ranking temprano que deja 100 → ranking tardío multitarea. Cita: "At the end of the retrieval stage, up to 1500 media are fetched."
- Ranking tardío: "based on their likelihood of user engagement such as like and save."
- Algunas predicciones: ver más del 95 % de un video, verlo más de 5 s, seguir al autor, guardar, reenviar, comentar, dar me gusta y marcar «No me interesa».

### 2.3 Índice de tarjetas
https://transparency.meta.com/features/explaining-ranking/ (página actualizada el 31/12/2023). Hay tarjetas separadas para Feed, Feed Recommendations, Explore, Reels Chaining, Search y Suggested Accounts, entre otras. Las únicas que leí completas son la de Reels y la de Explore.

---

## 3. Centro de ayuda de Instagram (todas las páginas consultadas el 13/11/2026; el Centro de ayuda no muestra fechas)

### 3.1 Pautas de recomendación
URL: https://help.instagram.com/313829416281232 · «Recommendations on Instagram» · Grado: oficial
- Estándar más alto que las Normas comunitarias: "Our Recommendations Guidelines are designed to maintain a higher standard than our Community Standards".
- Ahora son **3 categorías** (no 5): "Three categories of content are allowed on Meta technologies, but may not be eligible for recommendations."
  1. Contenido que impide fomentar una comunidad segura: autolesiones o trastornos alimentarios, violencia, contenido sexual o sugerente, productos regulados, productos para adelgazar y cirugía estética.
  2. Contenido de baja calidad: "Unoriginal content that is largely repurposed from another source with only minor, immaterial edits"; "Long captions unrelated to the underlying content and coordinated comment networks".
  3. Contenido falso o engañoso, calificado por verificadores externos.
- Cuentas que Instagram intenta no recomendar, entre otras:
  - las que compran seguidores o likes: "misleading practices to build followings, such as purchasing 'likes'"
  - las que publican de forma reiterada personas fotorrealistas generadas por IA sin la etiqueta de perfil IA: "photorealistic AI-generated person, unless the account has disclosed this by adding the AI-generated profile label".

### 3.2 Elegibilidad para recomendaciones y Account Status
- https://help.instagram.com/653964212890722 (Recommendation eligibility):
  - Account Status muestra si eres elegible "on Reels, Feed, Explore, Search or Suggested Accounts".
  - Ser elegible no garantiza nada: "your eligibility for recommendations doesn't guarantee that your content will be recommended."
  - Si la cuenta no es elegible, no se recomienda nada de ella: "none of your content will be recommended". Aun así, los seguidores siguen viendo el contenido.
- https://help.instagram.com/338481628002750 (Check your Account Status): permite ver el contenido eliminado y las funciones bloqueadas, y pedir revisión. Cita: "In most cases, you'll get a warning before losing access to your account."

### 3.3 Qué Reels se recomiendan y cuáles se ven menos
URL: https://help.instagram.com/1525585517644948 · Grado: oficial
- Se recomiendan los Reels que entretienen a una audiencia amplia, inspiran a crear, usan música de la biblioteca o audio original y están "filmed vertically".
- Se ven menos los que "Are muted, blurry, or low resolution", "Contain borders, logos, or watermarks", "Have the majority of the image covered by text" o "Are not original videos".
- Los seguidores no se ven afectados: "Reels from people you follow will still be shown… we won't make them less visible."

### 3.4 Cómo se eligen los posts sugeridos (feed, Reels, Explore)
URL: https://help.instagram.com/381638392275939 · Grado: oficial
- Factores: tu actividad ("what posts you've liked, saved, reposted or commented on"), tus conexiones, la información del post ("How popular the post may be… when or where it was posted"), la información de la cuenta ("How many times people have interacted with that account in the past few weeks"), el dispositivo y tu actividad en Threads.

### 3.5 Tipos de cuenta y acceso a Insights
- https://help.instagram.com/138925576505882: una cuenta profesional puede ser Business o Creator. Cita: "Professional accounts can't be set to private." Las profesionales tienen panel profesional, anuncios, botones de contacto e Insights.
- https://help.instagram.com/1533933820244654: las cuentas personales públicas también ven Insights. Cita: "You need to have a public (personal or professional) account on Instagram to view insights." Hay datos de los últimos 90 días; para ver datos demográficos hacen falta más de 100 espectadores o cuentas que interactúan. Si la cuenta pasa a privada, pierde los Insights.
- Diferencia entre tipos: las personales públicas ven Insights desde «Your dashboard» y las profesionales desde «For professionals > Insights».
- Funciones solo para profesionales: promocionar contenido (Boost), Account Status de recomendaciones con detalle (https://help.instagram.com/653964212890722: "If you're using a professional account, you can see if your content may be eligible…") y umbrales distintos para trial reels (ver 3.9).

### 3.6 Definición de métricas
- **About Instagram insights**: https://help.instagram.com/788388387972460
  - Views: "The number of times your content was played or displayed. Content includes reels, posts, stories, live videos and ads."
  - Viewers: "The number of unique accounts that have seen your content on screen at least once". Es lo que antes se llamaba alcance o «cuentas alcanzadas».
  - Interactions: "likes, comments, saves and shares."
  - Accounts engaged: cuentas únicas que interactuaron. En posts se puede separar entre seguidores y no seguidores.
  - Las métricas están marcadas como "estimated and in-development".
- **Reels**: https://help.instagram.com/202865988324236
  - Views: "The number of times your reel starts to play or replay."
  - Watch time: "The total amount of time your reel was played, including any time spent replaying".
  - Average watch time: "watch time divided by the number of initial views."
  - Follows: las cuentas que empezaron a seguirte por ese reel.
  - Los datos de un reel están disponibles hasta 2 años.
- **Posts y carruseles**: https://help.instagram.com/553860108359435
  - Views: "The number of times your content was displayed."
  - Interactions.
  - Profile activity.
  - Disponibles hasta 2 años.
- **API oficial (Meta for Developers)**: https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights
  - `reels_skip_rate`: "The percentage of views from people who skipped during the first 3 seconds of the reel." Marcada como "estimated and in development".
  - `shares` y `saved` existen como métricas por publicación.
  - `impressions` está obsoleta para el contenido creado después del 02/07/2024.
- **Lo que no encontré en el Centro de ayuda**: definiciones de «envíos por alcance» y «me gusta por alcance». Mosseri las usa como ratios para que el creador las calcule, pero no aparecen como métricas nativas. Tampoco encontré «skip rate» en la página de ayuda de Reels: solo está en la API.

### 3.7 Límites de Reels
- https://help.instagram.com/225190788256708 (Record a reel):
  - "You can record and edit videos up to 20 minutes with Instagram Reels."
  - "Reels over 3 minutes won't be recommended to new audiences."
- https://help.instagram.com/1038071743007909 (Reel size & aspect ratios):
  - "aspect ratio between 1.91:1 and 9:16"
  - "minimum frame rate of 30 FPS… minimum resolution of 720 pixels"
  - Portada recomendada: "420px by 654px (or 1:1.55 ratio)". La portada no se puede editar después de subir el reel.
- Peso máximo del archivo en MB: **no lo encontré** en el Centro de ayuda.
- Calidad (blog de Creators, 09/04/2026, https://creators.instagram.com/blog/best-camera-settings-instagram-reels): "export at 2K, HDR, and 60 fps—Instagram will prioritize playback up to those settings". También dice que la alta calidad "can help your Reels reach more people".

### 3.8 Hashtags: límite de 5 (verificado)
- https://help.instagram.com/351460621611097 · "You can use up to 5 tags on a post. If you include more than 5 tags on a single photo/video, your comment won't post."
- El anuncio de @creators (18/12/2025) lo conozco solo por Social Media Today (fuente secundaria): "We find that using fewer (up to 5) more targeted hashtags… can improve both your content's performance". No lo leí en el post original.
- Que Mosseri dijera que los hashtags «no aumentan el alcance» también lo vi solo en prensa (Social Media Today). No verificado en el original.

### 3.9 Trial reels (Centro de ayuda vigente)
URL: https://help.instagram.com/1013292530224018 · Grado: oficial
- Requisitos:
  - Cuenta pública, con "at least 200 followers" si es profesional o "at least 1,000 followers" si es personal.
  - Si la cuenta no es recomendable, pierde el acceso a trial reels.
- Contenido repetido: "Your trial reel may get limited reach if Instagram detects that you've previously shared the same content."
- Insights: "within 24 hours".
- No perjudica a los Reels normales: "Trial reels are evaluated independently in Instagram's ranking and don't impact the performance or ranking of your standard reels content."
- Compartir automáticamente: "if it's performing well soon after you publish it, based on signals like views and engagement."

### 3.10 Carruseles
URL: https://help.instagram.com/269314186824048 · Grado: oficial
- "You can share a post with up to 20 photos and videos as a single post". **Verificado: 20.**
- La orientación que elijas aplica a todo el carrusel.
- "videos in carousels are not considered reels and will not show up in the Reels tab". Ojo: un carrusel con audio sí puede aparecer en la pestaña Reels (ver 1.6).
- Después de publicarlo se puede reordenar y eliminar elementos, pero no añadir nuevos.

### 3.11 Programación nativa
URL: https://help.instagram.com/iphone-app/439971288310029 · Grado: oficial
- Requiere cuenta pública (personal o profesional): "You must have a public account on Instagram."
- "You can schedule up to 25 posts a day, up to 30 days in advance."
- Funciones incompatibles: "product tagging, collaborative posts, sponsored posts and fundraisers aren't compatible with scheduled content".

### 3.12 Colaboraciones (Collabs)
URL: https://help.instagram.com/iphone-app/5861247717337470 · Grado: oficial
- "You can add up to 5 collaborators to your post." El post se comparte con los seguidores de cada colaborador y aparece en sus perfiles.
- Solo el creador original puede borrar el post. Si el post incumple las normas, la sanción puede alcanzar a todos los colaboradores.
- El blog de originalidad (30/04/2026) recomienda Collabs, Remix o la etiqueta de colaboración pagada para usar contenido de terceros sin que cuente como no original.

### 3.13 Reutilización (Remix)
URL: https://help.instagram.com/652943337035777. En cuentas públicas, cualquiera puede reutilizar tus Reels, videos y fotos con remix, secuencias, plantillas o stickers, salvo que lo desactives.

---

## 4. No encontrado oficialmente (posibles mitos o datos sin respaldo)

1. **Pesos o multiplicadores** («los envíos valen 3 a 5 veces más que los me gusta», «el tiempo de visualización vale X %»). Mosseri solo dice "slightly more important".
2. **Orden fijo de las 3 señales** de Mosseri (tiempo de visualización, me gusta, envíos). Él las enumera, pero no dice que estén ordenadas por importancia.
3. **«Envíos por alcance» y «me gusta por alcance» como métricas nativas de Insights.** No existen en el Centro de ayuda ni en la API; son ratios que el creador calcula a mano.
4. **«Skip rate» visible en la app.** Solo lo verifiqué en la API (`reels_skip_rate`). La página de ayuda de Reels no lo menciona. «View Rate» sí aparece en el blog de Creators del 26/02/2025.
5. **«Hora dorada» o «los primeros 30 a 60 minutos deciden todo».** No está en ninguna fuente oficial. Lo oficial es la distribución por etapas a audiencias cada vez más amplias, sin ventana de tiempo fija.
6. **Frecuencia ideal** («publica N veces al día o a la semana»). Lo oficial dice solo "post regularly / consistently", sin cifras.
7. **Mejor hora para publicar universal.** No hay nada oficial. Insights muestra cuándo están activos tus seguidores.
8. **Los hashtags aumentan el alcance.** No es oficial. Lo oficial es el límite de 5 y que sirven para Search o categorizar. La afirmación de Mosseri de que «no aumentan el alcance» no la verifiqué en el original.
9. **«Editar un post después de publicarlo mata el alcance»** o **«los enlaces en el caption penalizan».** No encontré nada oficial sobre ninguna de las dos.
10. **Shadowban como castigo oculto.** Instagram lo niega (Ranking Explained, 2023) y remite a Account Status.
11. **«Los carruseles se muestran de nuevo desde la 2.ª diapositiva a quien no interactuó».** No lo encontré en ninguna fuente oficial leída. Se atribuye a Mosseri, pero no lo verifiqué.
12. **Programar con 75 días de antelación.** La ayuda oficial dice **30 días** y un máximo de 25 posts al día.
13. **«Los Reels de más de 90 s no se recomiendan».** Está desactualizado: el límite oficial para recomendar es de 3 minutos desde el 21/01/2025.
14. **«Los trial reels dañan el rendimiento de la cuenta».** La ayuda oficial dice lo contrario: se evalúan de forma independiente.
15. **Peso máximo de archivo de Reels (MB) y duración del video largo «Features» (90 min).** No encontré ninguno de los dos datos en una fuente oficial.
16. **Post de Mosseri del 31/12/2025 sobre la estética «raw» o imperfecta y la IA.** Solo lo vi en prensa; no lo verifiqué en el original.
17. **Versión 2025 de «Instagram Ranking Explained».** La URL oficial sigue mostrando el 31/05/2023. Si hubo una actualización en 2025, no está en esa URL.

## 5. Páginas que no cargaron o cargaron incompletas
- https://creators.instagram.com/best-practices y https://creators.instagram.com/grow/insights: solo mostraron la navegación, sin el texto de las buenas prácticas, que está dentro de la app.
- https://transparency.meta.com/features/explaining-ranking/ig-reels/: error «page isn't available». La tarjeta vigente de Reels es `ig-reels-chaining`.
- `browser_fetch` devolvió vacía https://about.instagram.com/blog/announcements/reels-algorithm-control; la leí con WebFetch.
- https://help.instagram.com/556617736965724 (versión de escritorio): vacía. Leí la versión de iPhone.
- https://help.instagram.com/488619974671134 y https://help.instagram.com/627963287377328: vacías. No eran imprescindibles.
- Uppbeat (cobertura de Mosseri sobre carruseles y envíos): bloqueada (429 o control de seguridad de Vercel). No es fuente oficial.
