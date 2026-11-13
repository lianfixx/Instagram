# Meta / Instagram: transparencia del ranking, DSA, ingeniería, originalidad e IA

Investigación hecha el 13/11/2026, leyendo las páginas en línea (WebFetch/WebSearch), no de memoria. Alcance: Reels y feed. Las historias quedan fuera, salvo cuando una fuente las menciona junto con lo demás.

**Grados de fiabilidad usados**
- **Oficial (transparencia):** transparency.meta.com.
- **Oficial (anuncio):** about.fb.com, about.instagram.com y creators.instagram.com.
- **Oficial (ingeniería):** engineering.fb.com. Explica cómo funciona el sistema por dentro, pero no son reglas para creadores.
- **Secundaria:** prensa como TechCrunch o PetaPixel. Se usa solo cuando no encontré la fuente oficial.

**Sobre las citas:** las tomé de lo que extrajo la herramienta de lectura web. Las que van entre comillas aparecieron como texto literal. Lo que va sin comillas es paráfrasis. Antes de publicar una cita literal conviene verificarla en la URL.

**Advertencia general:** Meta no publica pesos ni porcentajes del ranking orgánico, y aquí no se inventa ninguno. Las únicas cifras que aparecen son las que Meta publica, por ejemplo cuántos candidatos pasa de una etapa a otra o el 75 % de recomendaciones originales.

---

## 1. Transparency Center: «Our approach to explaining ranking» y las tarjetas de sistema (system cards)

### 1.0 Página general
- **URL:** https://transparency.meta.com/features/explaining-ranking/ (dice «UPDATED DEC 31, 2023»).
- **Tarjetas de Instagram que enlaza:** Feed, Stories, Explore, Reels Chaining, Search, **Feed Recommendations**, Suggested Accounts, Notifications, Comments y Threads Feed.
- **No hay una tarjeta llamada «ig-reels»:** la URL `/ig-reels/` devuelve **404**. La tarjeta de Reels se llama **«Reels Chaining»**.
- **Citas útiles:**
  - «Input signals fall into broad categories such as the unique features of a post».
  - «Prediction models, the predictions they make, and their input signals are dynamic».
  - «The controls listed in the system cards may not be available on all devices or to everyone».
- **Grado:** oficial (transparencia).

### 1.1 Reels (tarjeta «Reels Chaining»)
- **URL:** https://transparency.meta.com/features/explaining-ranking/ig-reels-chaining/
- **Fecha:** «UPDATED NOV 11, 2025».
- **Etapas:**
  1. **Reunir inventario:** reels de cuentas que sigues y reels parecidos a los que viste hace poco.
  2. **Usar señales:** un modelo ligero deja unos **100 candidatos**. Además, «The system also applies certain integrity processes to remove content that is non-recommendable».
  3. **Hacer predicciones.**
  4. **Ordenar por puntaje:** «Reels that the system predicts will provide more value for you are shown sooner».
- **Predicciones que nombra** (probabilidad de que el espectador):
  - use el audio del reel en un reel propio;
  - vea **menos de 3 s**;
  - toque «Interested»;
  - comente;
  - vea más del reel que el 95 % de los usuarios que ven reels de la misma duración;
  - abra en pantalla completa un reel vertical desde Explore;
  - lo vuelva a compartir (reshare);
  - lo comparta **fuera de Instagram**;
  - **siga al autor**.
- **Señales que nombra:**
  - si viste reels más de **15 s**;
  - tiempo que la gente pasa en el reel;
  - cuántas veces se descarta o se salta en menos de **2 s**;
  - toques en el enlace del audio y en «Use audio»;
  - comentarios, visitas a perfiles y guardados;
  - me gusta de otros usuarios;
  - veces compartido dentro y fuera de la app, «where data privacy laws permit»;
  - seguidores que el autor ganó con ese reel.
- **Controles del usuario:**
  - **Following** (o **Latest** en tabletas): muestra primero lo más reciente.
  - **Not interested:** el sistema «attempt[s] to filter out similar content in the future».
  - **Report**, **Remix**, **Save** y **Share**.
  - **Control de contenido sensible**.
  - La tarjeta **no menciona** un modo «sin personalizar» ni un reinicio de recomendaciones.
- **Para un creador:**
  - Los primeros 2–3 s son decisivos, porque la tarjeta mide saltos en menos de 3 s y descartes en menos de 2 s.
  - Importa que el video se vea más que otros de **su misma duración**.
  - Cuentan los envíos fuera de Instagram, el uso del audio y los seguimientos que gana el reel.

### 1.2 Feed (solo cuentas que sigues)
- **URL:** https://transparency.meta.com/features/explaining-ranking/ig-feed/
- **Fecha:** «UPDATED JUN 29, 2026».
- **Alcance:** solo ordena publicaciones de cuentas seguidas. El contenido sugerido y los anuncios **no** dependen de este sistema; tienen su propia tarjeta, Feed Recommendations.
- **Etapas:**
  1. Reunir publicaciones de cuentas seguidas y quitar las que violan las Normas comunitarias.
  2. Usar señales: un modelo ligero elige unas **700**, y se aplica integridad para reducir la distribución de contenido problemático.
  3. Hacer predicciones.
  4. Calcular el puntaje de unas **500** y ordenarlas, buscando variedad: «The system also tries to ensure your feed has a balanced mix of content types».
- **Las 10 predicciones que nombra:**
  1. «How likely you are to swipe through the whole carousel».
  2. «…to enjoy this post».
  3. «…to skip this post».
  4. Tiempo en el perfil del autor después de ver la publicación.
  5. «How likely you are to share a post with someone in a direct message».
  6. Tiempo que pasarás en la publicación.
  7. Probabilidad de saltar la primera publicación del feed.
  8. Probabilidad de pasar más de 10 s en la primera publicación.
  9. Probabilidad de activar el sonido.
  10. Probabilidad de que la primera publicación te retenga en la sesión.
- **Señales destacadas:**
  - **Carrusel:** número de deslizamientos, tarjetas vistas, si se reordenó y cuántas tarjetas tiene.
  - **Compartir por mensaje directo:** si la publicación es **informativa** (noticias, reseñas, tutoriales), si se creó **en los últimos 90 días**, si es un **repost** y si se abrió la hoja de compartir.
  - **Tiempo en la publicación:** si es una foto y **cuánto texto lleva superpuesto**.
- **Controles del usuario:**
  - **Mute** (silenciar).
  - **Favorites:** las cuentas favoritas tienen prioridad en el feed.
  - **Following/Latest:** «When you select this option, you won't see recommended content from instagram».
  - **Hide:** «helps to limit similar content».
  - **Unfollow**, **Report**, **Save** y **Share**.
- **Para un creador:**
  - En carruseles cuenta que se recorran completos.
  - Las piezas informativas, tutoriales y reseñas, recientes y **no reposteadas**, son las que se comparten por mensaje directo.
  - La cantidad de texto sobre una foto es una señal declarada. La tarjeta no dice si suma o resta.

### 1.3 Feed Recommendations (publicaciones sugeridas en el feed)
- **URL:** https://transparency.meta.com/features/explaining-ranking/ig-feed-recommendations/
- **Fecha:** «UPDATED JUN 29, 2026».
- **Alcance:** cuentas, publicaciones y reels sugeridos dentro del feed. Los anuncios y el «connected content» no entran.
- **Etapas:** inventario de contenido público que cumple las reglas de calidad e integridad, después señales y después ranking.
- **Predicciones que nombra:**
  - **«How informative a post is»**;
  - que toques «Interested»;
  - tiempo en Reels después de entrar desde el feed;
  - que sigas desplazándote después de la primera publicación;
  - que pases a la siguiente;
  - que hagas clic en el perfil del autor;
  - que toques para comentar;
  - que saltes la primera publicación;
  - que abras el reel en pantalla completa;
  - que actives el audio.
- **Señales que nombra:**
  - **una evaluación de calidad generada por un LLM** sobre la publicación;
  - tiempo en el contenido del autor durante 84 días;
  - impresiones según la antigüedad del contenido (1–3, 8–14 y 14–21 días);
  - cuánta gente pasa de largo, visita el perfil o activa el audio;
  - plataforma del dispositivo.
- **Controles del usuario:**
  - **Not interested:** oculta publicaciones de ese autor, y el sistema «will attempt to demote similar content in the future».
  - **Manage suggested content:** reúne los indicadores de interés, el control de contenido sensible, la opción de **pausar (snooze)** las sugerencias y la de ocultar sugerencias que contengan ciertas palabras, frases o emojis.
  - **Following/Latest:** feed sin recomendaciones, en orden cronológico.
  - **Hide**, **Save** y **Report**.
- **Para un creador:** es la confirmación oficial más clara de que se predice qué tan **informativa** es una publicación y de que un **LLM evalúa su calidad**. Lo que más ayuda es aportar valor concreto y legible.

### 1.4 Explore
- **URL:** https://transparency.meta.com/features/explaining-ranking/ig-explore/
- **Fecha:** «UPDATED JUN 22, 2026».
- **Etapas:**
  1. **Recuperación (retrieval)**, con filtrado colaborativo, PageRank personalizado y redes «two-tower». Usa fuentes basadas en autores y en contenido: «up to 1500 media are fetched».
  2. **Ranking temprano** con red two-tower: «the top 100 media are passed to the next stage».
  3. **Ranking tardío** con una red multitarea y multietiqueta.
- **Predicciones** (cuatro «Recommender»):
  - seguir al autor;
  - ver más de 5 s;
  - ver más del 95 % del video;
  - **tocar «Not Interested»**;
  - comentar, dar me gusta, compartir y guardar;
  - tiempo de reproducción previsto;
  - ver menos de 3 s;
  - ver un reel más de 11 s o una publicación que no es reel más de 6 s;
  - ver el reel completo;
  - usar o guardar el audio;
  - pasar al siguiente reel.
- **Señales:**
  - tiempo en publicaciones de un autor;
  - **desempeño de la publicación:** cuántos la vieron, la tocaron, la vieron más del 95 % o la guardaron, y cuántos comentarios tiene;
  - acciones pasadas del usuario;
  - saltos en menos de 2 s;
  - si se ve con sonido.
- **Controles del usuario:**
  - **Not Interested:** «The system will attempt to filter out similar content in the future».
  - **Tune Your Algorithm**, vinculado a «Your Algorithm» (ver 1.6).
  - **Like** y **Report**.
- **Grado:** oficial (transparencia).

### 1.5 Search (búsqueda)
- **URL:** https://transparency.meta.com/features/explaining-ranking/ig-search/
- **Fecha:** «UPDATED JUN 23, 2026».
- **Etapas:**
  1. Inventario ligado a la búsqueda: hashtags, lugares, reels, publicaciones, perfiles y audio.
  2. Puntaje.
  3. Filtros de integridad y de **duplicados (deduplicación)**.
  4. Ranking.
- **Predicciones:** clic seguido de una acción, como seguir, dar me gusta, guardar, compartir o visitar el perfil. Incluye clic en un audio seguido de crear un reel con él.
- **Señales:**
  - **parecido entre las palabras buscadas y el nombre de usuario, el nombre del perfil, las palabras clave o los hashtags**;
  - tasas de clic y acción por país, región o ciudad;
  - grafo social;
  - interacción con la publicación;
  - tema;
  - **cercanía geográfica**;
  - popularidad de la canción por país.
- **Controles del usuario:** borrar el historial, filtrar por categoría y **ver resultados no personalizados**.
- **Para un creador:** el nombre del perfil, las palabras clave del texto y los hashtags deben coincidir con lo que la gente busca. Esto lo dice la tarjeta.

### 1.6 Controles transversales, fuera de las tarjetas
- **Reiniciar recomendaciones («Reset suggested content»)**
  - Cita: «clear your recommended content across Explore, Reels and Feed and start fresh».
  - Ruta: Perfil > menú > Content preferences > Reset suggested content.
  - URL: https://about.fb.com/news/2024/11/introducing-recommendations-reset-instagram/
  - Fecha: publicado el 19/11/2024, actualizado el 14/07/2025.
  - La misma nota describe «Not interested» e «Interested» en el menú de tres puntos.
  - Grado: oficial (anuncio).
- **«Your Algorithm»**
  - Muestra los temas que Instagram cree que te interesan y te deja escribir temas para ver más o menos de ellos.
  - Fechas: 10/12/2025 en Reels (Estados Unidos); 15/04/2026 en Explore; 10/06/2026 en todo Instagram. Cita de esa última actualización: «Your Algorithm is now live across all of Instagram, including Feed, Reels, and Explore».
  - Las publicaciones sugeridas pueden llevar una etiqueta como «From Running».
  - URL: https://about.instagram.com/blog/announcements/reels-algorithm-control
  - Grado: oficial (anuncio).
  - **Para un creador:** la clasificación por **tema** es explícita. Conviene que cada pieza tenga un tema reconocible y constante.

---

## 2. Ley de Servicios Digitales de la UE (DSA): artículos 27 y 38, feed no personalizado e informes

- **Anuncio de agosto de 2023** (Nick Clegg)
  - URL: https://about.fb.com/news/2023/08/new-features-and-additional-transparency-measures-as-the-digital-services-act-comes-into-effect/
  - Fecha: 22/08/2023.
  - Ofrece en la UE la opción de ver contenido «not ranked» en Reels, Stories, Search y otras partes de la app.
  - Reels e historias pueden verse solo de cuentas seguidas, «ranked in chronological order, newest to oldest».
  - La búsqueda puede basarse solo en las palabras escritas.
  - Meta publicó «22 system cards for Facebook and Instagram», que son las de la sección 1.
  - La nota **no detalla** Explore. Según la prensa de 2023 (fuente secundaria), Explore tiene la opción «Not personalized» en el menú «For you».
  - Grado: oficial (anuncio).
- **Informes de la DSA**
  - URL: https://transparency.meta.com/reports/regulatory-transparency-reports/
  - Incluye para Instagram: informes de transparencia de plataformas de muy gran tamaño (VLOP), **resultados de la evaluación de riesgo sistémico**, auditorías independientes e informes de implementación de auditorías.
  - La página no mostró los enlaces de descarga en texto, así que no pude abrir los PDF desde Meta.
- **Evaluación de riesgo sistémico de Instagram de 2025**
  - Leída en una copia de terceros, el archivo de Open Terms Archive: https://raw.githubusercontent.com/OpenTermsArchive/dsa-reports-versions/refs/heads/main/Instagram/Systemic%20Risks%20%E2%80%94%202025.md
  - Grado: oficial en origen, pero **sin verificar contra el PDF de Meta**.
  - Menciona «Recommendation Guidelines, which are published in the Instagram Help Centre» y «We filter content to remove items that potentially violate our policies».
  - Sobre contenido sensible: «We may remove, reduce the distribution of, or inform users of potentially sensitive content».
  - Sobre política: «we will be recommending more political content based on personalised signals».
  - Solo leí el primer 28 % del documento.
- **Qué le sirve a un creador de la DSA**
  1. En la UE una parte del público ve los Reels y el feed en **orden cronológico y sin personalizar**. Ahí solo llegas a quien ya te sigue, así que los seguidores reales importan.
  2. Las «Recommendation Guidelines» son más estrictas que las Normas comunitarias. Lo que no las cumple sigue publicado, pero no se recomienda.
  3. El contenido sensible o dudoso pierde distribución.
- **Contexto regulatorio, no de Meta:**
  - Un tribunal de Ámsterdam (octubre de 2025, caso Bits of Freedom) exigió que la opción sin perfilado sea accesible directamente, incluso en Reels.
  - La Comisión Europea publicó el 10/07/2026 conclusiones preliminares sobre «diseño adictivo» en Instagram y Facebook.
  - Ambos datos vienen de fuentes secundarias; no leí los textos oficiales.

---

## 3. Blog de ingeniería de Meta: oficial (ingeniería)

- **«Scaling the Instagram Explore recommendations system»**
  - URL: https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/
  - Fecha: 09/08/2023.
  - Etapas: recuperación desde varias fuentes (tendencias, aprendizaje automático, tiempo real); primer ranking con un modelo two-tower ligero; segundo ranking con un modelo multitarea y multietiqueta (MTML) sobre unos 100 candidatos; **reordenamiento final con reglas de integridad y de negocio**.
  - Esas reglas incluyen **diversidad**, como no mostrar al mismo autor seguido.
  - Combina las predicciones en un **«value model»**: una suma ponderada donde las acciones positivas suman y las negativas, como «see less», **restan**. No publica los pesos.
  - Citas: «Tuning the weights of the VM allows us to explore different tradeoffs between online engagement metrics» y «Simply returning results sorted with reference to the final VM score might not be always a good idea».
  - La recuperación descarta del historial del usuario lo que tiene muchas denuncias o es objetable.
- **«Journey to 1000 models: Scaling Instagram's recommendation system»**
  - URL: https://engineering.fb.com/2025/05/21/production-engineering/journey-to-1000-models-scaling-instagrams-recommendation-system/
  - Fecha: 21/05/2025.
  - El embudo es **sourcing → early-stage ranking → late-stage ranking**, y Instagram tiene más de 1000 modelos en producción.
  - Los modelos predicen me gusta, comentarios y seguimientos. Cita: «If we recommend irrelevant content, user engagement suffers».
  - No trae consejos para creadores.
- **«Adapting the Facebook Reels RecSys AI model based on user feedback»**
  - URL: https://engineering.fb.com/2026/01/14/ml-applications/adapting-the-facebook-reels-recsys-ai-model-based-on-user-feedback/
  - Fecha: 14/01/2026.
  - Es **solo de Facebook Reels**; no menciona Instagram.
  - Describe una encuesta de interés real (UTIS), «To what extent does this video match your interests?», usada para ir más allá de los me gusta y del tiempo de visualización.
  - Sirve como indicio de hacia dónde va Meta, pero **no está confirmado para Instagram**.
- **Andromeda**
  - URL: https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/
  - Fechas: 02/12/2024, con una entrega posterior el 28/10/2026.
  - Es **recuperación de anuncios**, no de contenido orgánico. No encontré ninguna fuente de Meta que la vincule al ranking orgánico; lo que circula sobre «Andromeda y Reels orgánicos» viene de agencias.
- **Aprendizaje de secuencias (sequence learning)**
  - Los posts de Meta sobre secuencias de acciones del usuario (2024 y 2026) tratan de **anuncios**.
  - No encontré un post de ingeniería de 2024–2025 sobre el ranking de Reels de Instagram con aprendizaje de secuencias.
- **Ajustes para contenido original:** no encontré ningún post de ingeniería sobre esto. La información está en los anuncios de la sección 4.

---

## 4. Contenido original, reposts, marcas de agua e IA

### 4.1 Originalidad y agregadores
- **2022 (fuente secundaria):** Mosseri anunció que se priorizaría el contenido original sobre los reposts y reconoció que lo estiman con clasificadores. Fuente: TechCrunch, 20/04/2022.
- **30/04/2024: «Helping Creators Find New Audiences»**
  - URL: https://creators.instagram.com/recommendations-and-originality
  - Grado: oficial (anuncio).
  - Reposts: «when we find two or more identical pieces of content on Instagram, we will only recommend the original one». El original reemplaza a la copia en las recomendaciones.
  - **Excepciones**, contenido «materially edited»: un meme, una compilación de parodias, un video **narrado con una voz en off nueva** o un remix de reacción.
  - Para ser recomendable, el contenido debe ser «original, does not violate our community guidelines, has no visible watermarks».
  - **Agregadores:** las cuentas que «repeatedly post content … they didn't create or enhance in a material way» salen de las recomendaciones. La página no da un número límite. El dato de «10 veces en 30 días» aparece solo en prensa y no lo encontré en la página oficial.
  - Los reposts llevan **etiqueta que enlaza al original** (según TechCrunch, 30/04/2024).
- **30/04/2026: «Rewarding original creators on Instagram»**
  - URL: https://creators.instagram.com/blog/rewarding-original-creators-on-instagram
  - Grado: oficial (anuncio).
  - Amplía la regla de Reels a **fotos y carruseles**.
  - Qué es original: «Original content is work that you wholly created or reflects your unique perspective».
  - Qué no basta: agregar «a border, watermark, subtitles, or a credit in the captions».
  - La elegibilidad se calcula sobre un periodo móvil de **30 días** («calculated on a rolling basis»). La página no da un porcentaje; el «50 %» circula solo en fuentes secundarias.
  - Cifra oficial: «75% of recommendations in the US now coming from original posts».
  - No cambia lo que ven los seguidores.
  - Se revisa en **Estado de la cuenta (Account Status)**, donde se puede apelar.
  - Para usar contenido ajeno recomienda Collabs, Remix, reposts o compartir en historias, y la etiqueta de colaboración pagada.
  - **No menciona la IA.**
- **Consejos de elegibilidad (2022, actualizados el 25/04/2023)**
  - URL: https://creators.instagram.com/blog/instagram-recommendations-eligibility-tips-creators
  - Grado: oficial (anuncio), pero **antiguo**.
  - «Don't post reels that contain watermarks, that are blurry or otherwise low quality».
  - «Avoid visibly recycled content».
  - «Pull the viewer in within the first 3 seconds».
  - Video vertical y en pantalla completa.
  - El límite de «3 minutes or less» para ser recomendado es de 2023 y puede haber cambiado; verificarlo antes de usarlo.
- **Recommendation Guidelines:** incluyen el contenido que los usuarios dicen que no les gusta, «such as clickbait or engagement bait», y el «unoriginal content that is largely repurposed from another source». No pude leer las páginas de Ayuda (help.instagram.com) porque cargan vacías para la herramienta.

### 4.2 Etiquetas de IA en publicaciones («AI info»)
- **Febrero de 2024: «Labeling AI-Generated Images on Facebook, Instagram and Threads»**
  - URL: https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/
  - Fecha: 06/02/2024, actualizado el 01/04/2025.
  - Grado: oficial (anuncio).
  - **Obligación:** «We'll require people to use this disclosure and label tool» cuando publiquen «photorealistic video or realistic-sounding audio that was digitally created or altered».
  - **Sanción:** «we may apply penalties if they fail to do so».
  - Detección: los metadatos de **C2PA e IPTC** y las «invisible watermarks».
  - Para contenido de alto riesgo: «we may add a more prominent label».
- **Abril de 2024: «Our approach to labeling AI-generated content and manipulated media»**
  - URL: https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/
  - Fechas: 05/04/2024, con notas del 01/07/2024 y del 12/09/2024; última actualización el 23/10/2025.
  - El 01/07/2024 «Made with AI» pasó a llamarse **«AI info»**.
  - El 12/09/2024 la etiqueta de contenido **solo editado** con IA se movió al **menú** de la publicación. La de contenido **generado** con IA sigue visible.
  - Grado: oficial (anuncio).
- **Página de seguimiento de etiquetas**
  - URL: https://transparency.meta.com/governance/tracking-impact/labeling-ai-content
  - Fecha: 19/02/2025.
  - Las etiquetas se muestran como «AI Info» y se aplican cuando se detectan «industry standard AI image indicators» o cuando el usuario lo declara.
  - **No dice que la etiqueta reduzca el alcance.**
- **Ayuda de Instagram:** https://help.instagram.com/761121959519495 **no cargó** para la herramienta (devuelve solo «Help Center»). Según un extracto de búsqueda, dice que etiquetar «in some cases it's required» y que Meta la aplica si detecta IA. Está sin verificar.

### 4.3 Etiqueta de perfil generado con IA («AI-generated profile»)
- **URL:** https://creators.instagram.com/blog/ai-generated-profile-label
- **Fecha:** 31/08/2026. Antes se llamaba «AI creator» (mayo de 2026, fuente secundaria).
- **Grado:** oficial (anuncio).
- **A quién aplica:** a perfiles que presentan a una **persona generada con IA**.
- **Sanción:** «Creators who don't appropriately label their AI-generated profiles may see limits to their profile's reach».
- **Si se pone la etiqueta:** «Creators who proactively add the AI-generated profile label will not see a change to their profile's reach».
- **Quién no la necesita:** «Creators who simply use AI tools as part of their creative process don't need to add the label».
- La etiqueta de perfil aparece junto al contenido solo si la publicación no tiene ya su propia etiqueta de IA.
- El estado se revisa en Account Status, donde se puede apelar.

### 4.4 Implicaciones para un creador que publica videos hechos con IA (inferencias a partir de lo anterior)
1. **Si el video es fotorrealista o lleva voz o audio realistas**, hay que **activar la etiqueta de IA** al publicar. Es obligatorio y puede haber sanciones (Meta, febrero de 2024). Ninguna fuente oficial dice que la etiqueta «AI info» reduzca el alcance.
2. **Si la cuenta gira en torno a una persona o avatar generado con IA**, hay que activar «AI-generated profile». No hacerlo puede costar la elegibilidad para recomendaciones (31/08/2026).
3. **Ser original no tiene que ver con usar IA.** Lo que pierde recomendaciones es **subir de nuevo** material ajeno, aunque se le pongan bordes, subtítulos, marcas de agua o créditos. Un video de IA hecho por ti, con tu guion o tu perspectiva, cuenta como «wholly created or reflects your unique perspective».
4. **Sin marcas de agua visibles**, ni de otras apps ni de las herramientas de IA. Cuentan como criterio para no recomendar (2023 y 2024).
5. **Ninguna página oficial que haya leído** dice que el contenido de IA se penalice por ser de IA.
6. **Señales declaradas en las tarjetas:**
   - aguantar los primeros 2–3 s;
   - superar el visionado medio de los reels de su misma duración;
   - que se comparta por mensaje directo y fuera de la app;
   - que se use su audio;
   - que gane seguimientos;
   - en el feed: recorrido completo del carrusel, valor informativo y frescura (menos de 90 días).

---

## Páginas que no cargaron o que cambiaron
- `transparency.meta.com/features/explaining-ranking/ig-reels/`: **404**. La tarjeta de Reels está en `ig-reels-chaining`.
- `help.instagram.com/761121959519495` y `help.instagram.com/313829416281232`: devuelven solo «Help Center» (la página carga su contenido con JavaScript).
- Los PDF de riesgo sistémico y de transparencia de la DSA no tenían enlaces en el texto de la página. Usé la copia de Open Terms Archive.
- La página general «explaining ranking» dice «UPDATED DEC 31, 2023». Las tarjetas individuales se actualizaron entre noviembre de 2025 y junio de 2026.
