# Qué se sabe de cómo Instagram ordena y recomienda

Revisado el 13/11/2026. Todas las fuentes se leyeron ese día y están en [`data/fuentes.json`](../data/fuentes.json).

**Advertencia.** Instagram no publicó el código de su ranking, a diferencia de X. **No existen pesos, porcentajes ni constantes verificables**, y esta skill no inventa ninguno. Lo que hay son descripciones oficiales del proceso, declaraciones de Adam Mosseri (director de Instagram) y estudios externos.

Cada regla dice su grado de certeza:

- **oficial**: Instagram o Meta, leído en la fuente primaria.
- **terceros**: estudio externo con método declarado. Es correlación, no causa.
- **criterio**: inferencia de la skill a partir de lo anterior. Se dice como inferencia.

Las propias tarjetas de sistema de Meta avisan: «These models and their input signals are dynamic and they change frequently». Por eso se revisan cada mes (ver «Mantener al día» en [SKILL.md](../SKILL.md)).

## 1. No hay un algoritmo, hay varios

| Superficie | A quién muestra | Qué predice (lista oficial, sin pesos) | Fuente |
|---|---|---|---|
| **Feed** | Cuentas que sigues | Pasar unos segundos en la publicación, comentar, dar me gusta, compartir y tocar la foto de perfil. En carruseles, recorrerlo completo. Además, si es informativa, si tiene menos de 90 días, si es repost y cuánto texto lleva sobre la imagen. | `ranking-explicado`, `tarjeta-feed` |
| **Recomendaciones en el feed** | Cuentas que no sigues | Incluye **qué tan informativa** es la publicación, con una evaluación de calidad hecha por un modelo de lenguaje. | `tarjeta-feed-recs` |
| **Reels** | Sobre todo no seguidores | Reenviar, ver hasta el final, dar me gusta, ir a la página del audio. La tarjeta añade: ver **menos de 3 s**, ver **más que el 95 %** de quienes vieron reels de la misma duración, saltarlo en **menos de 2 s**, comentar, compartir fuera de la app, seguir al autor y usar el audio. Unos 100 candidatos llegan al ranking final. | `ranking-explicado`, `tarjeta-reels` |
| **Explorar** | No seguidores | Me gusta, guardar, reenviar, comentar, seguir, ver más del 95 % o más de 5 s, y tocar «No me interesa». Hasta 1500 candidatos pasan a 100. La popularidad pesa más que en el feed. | `ranking-explicado`, `tarjeta-explore` |
| **Búsqueda** | Quien busca | Compara la búsqueda con el **usuario**, el **nombre del perfil**, las palabras clave de la descripción y los hashtags, más la cercanía. | `tarjeta-search`, `creators-elegibilidad` |

Lo que se deduce para Emi (criterio): **el Reel trae gente nueva y el carrusel la retiene**. El feed reparte sobre todo entre seguidores, así que con una cuenta nueva el carrusel solo despega cuando los Reels ya trajeron seguidores.

## 2. Las señales que nombra Mosseri

- **Las tres que más importan:** «watch time, likes and sends». Los me gusta pesan *ligeramente* más con seguidores y los envíos *ligeramente* más con no seguidores. No da orden ni pesos (oficial, `mosseri-3-senales`, 21/01/2025).
- **Los envíos por mensaje** son «one of the biggest signals». Él mismo agrega «Don't force it» (oficial, `mosseri-envios`, 02/07/2024).
- **Reparto por etapas.** Un Reel se muestra primero a un público pequeño de no seguidores y los que mejor funcionan pasan a públicos más amplios. Se distribuye «based on its engagement, not just the creator's follower count»: **una cuenta nueva sí tiene alcance** (oficial, `creators-cuentas-pequenas`, 26/02/2025).
- **Primeros 3 segundos.** «Pull the viewer in within the first 3 seconds» (oficial, `creators-elegibilidad`). La tarjeta de Reels predice explícitamente ver menos de 3 s y saltar en menos de 2 s (oficial, `tarjeta-reels`).
- **Constancia.** «Post regularly», sin cifra (oficial, `creators-cuentas-pequenas`). La cifra de 3 a 5 por semana es de terceros (ver [estudios.md](estudios.md)).
- **Audio en fotos y carruseles.** Ayuda a que se muestren a más gente y pueden aparecer en la pestaña Reels (oficial, `creators-reels-2025`, `creators-cuentas-pequenas`).

## 3. Lo que saca a una pieza de las recomendaciones

Sigue visible para los seguidores, pero no se recomienda a nadie más.

| Qué | Grado y fuente |
|---|---|
| Reels **de más de 3 minutos**. Se pueden subir hasta 20 min. | oficial, `ayuda-reels-duracion`, `creators-reels-2025` |
| Baja resolución, **marca de agua**, sin sonido, con bordes o logos, con texto en la mayor parte de la imagen, o **ya publicado en Instagram**. | oficial, `ranking-explicado`, `ayuda-reels-recomendados` |
| **Contenido no original.** Solo se recomienda el original, también en fotos y carruseles desde el 30/04/2026. Bordes, marca de agua, subtítulos o un crédito **no** lo vuelven original. Original es «work that you wholly created or reflects your unique perspective». | oficial, `originalidad-2024`, `originalidad-2026`, `pautas-originalidad` |
| **Anzuelos de interacción** («engagement bait», «clickbait»). | oficial, `ayuda-recomendaciones` |
| **Descripciones largas que no tienen relación con el contenido** y redes coordinadas de comentarios. | oficial, `ayuda-recomendaciones` |
| Comprar seguidores o me gusta. | oficial, `ayuda-recomendaciones` |
| Personas fotorrealistas hechas con IA sin la etiqueta de perfil IA. | oficial, `ayuda-recomendaciones`, `ia-perfil` |
| Cuenta privada. Solo se recomienda lo de cuentas públicas. | oficial, `creators-elegibilidad` |
| Infracciones repetidas: la cuenta entera deja de ser recomendable un tiempo. Se ve en **Estado de la cuenta**. | oficial, `ranking-explicado`, `ayuda-elegibilidad` |

### Subir el mismo video a TikTok e Instagram

La regla de originalidad castiga piezas idénticas **dentro de Instagram**. Subir el video propio a dos redes no la rompe (criterio sobre `originalidad-2024`). Lo que sí lo saca de recomendaciones es la **marca de agua** de la otra app (oficial). Por eso a Instagram se sube el MP4 limpio de Editor Studio y nunca el que se descarga de TikTok.

## 4. Contenido político

- Meta **puede** recomendar contenido político de cuentas que la persona no sigue, en Reels, Explorar y el feed. Cada usuario tiene un control para ver más o menos (oficial, `politica-meta`, actualizado el 18/09/2025).
- La definición de Meta incluye publicaciones sobre **leyes**, elecciones y temas sociales. Una pieza de Emi sobre una reforma puede contar como política.
- **Sin confirmar:** qué opción viene puesta de inicio en México. Entre 2024 y enero de 2025 la regla fue no recomendarlo; después Meta cambió a un enfoque personalizado (prensa). Hay que revisarlo en la app.
- Para la skill (criterio): las piezas de IA + Derecho que hablan de herramientas o de cómo trabaja Emi no son políticas. Las que opinan sobre una ley pueden llegar a menos gente nueva. Por eso la política es el pilar con menos peso propuesto (ver [pilares.md](pilares.md)).

## 5. IA en las publicaciones

- **Etiqueta «Información de IA» (AI info), obligatoria** cuando la publicación lleva video fotorrealista o audio realista creados o alterados digitalmente. «We may apply penalties if they fail to do so» (oficial, `ia-etiqueta-2024`, `ia-info`).
- Si el contenido solo se **editó** con IA, la etiqueta va en el menú y no a la vista (oficial, `ia-info`).
- Ninguna fuente oficial leída dice que la etiqueta baje el alcance.
- **Etiqueta de perfil IA:** solo para cuentas que presentan a una persona generada con IA. «Creators who simply use AI tools as part of their creative process don't need to add the label» (oficial, `ia-perfil`, 31/08/2026). A Emi no le aplica.
- **Regla de Emi (13/11/2026):** ningún texto dice que la pieza la hizo una IA. Se cumple sin romper la regla de Instagram si de Vox Studio se muestra solo el estilo collage o ilustrado, nada fotorrealista. Si alguna vez hay IA fotorrealista, el interruptor se activa: es una obligación de la plataforma, no un texto de Emi. El validador lo exige (`etiqueta_ia`).

## 6. Formato y límites (oficial, Centro de ayuda, leído el 13/11/2026)

| Dato | Valor | Fuente |
|---|---|---|
| Reel | De 1.91:1 a 9:16; mínimo 720p y 30 fps. Portada recomendada de 420×654 px, que **no se cambia después**. | `ayuda-reels-formato` |
| Calidad | El blog de Creators (09/04/2026) sugiere exportar en 2K, HDR y 60 fps. | `creators-calidad` |
| Hashtags | **Máximo 5** por publicación. | `ayuda-hashtags` |
| Carrusel | Hasta **20** fotos o videos. Después se pueden reordenar o quitar elementos, pero no añadir. | `ayuda-carrusel` |
| Programar | Cuenta pública; hasta 25 publicaciones al día y **30 días** de anticipación. Las publicaciones en Collab no se pueden programar. | `ayuda-programar` |
| Trial reels | Piden cuenta recomendable y **200 seguidores en cuenta profesional** (1000 en personal). Se evalúan aparte y no afectan a los Reels normales. Las métricas llegan en unas 24 h. | `ayuda-trial`, `trial-reels` |
| Collab | Hasta 5 colaboradores. Por decisión de Emi, nada de Collab con MILLA. | `ayuda-collab` |
| Estadísticas | Las ven las cuentas públicas, **personales o profesionales**. Una cuenta profesional no puede ser privada. | `ayuda-insights-acceso`, `ayuda-tipos-cuenta` |

## 7. Controles que tiene quien ve

«No me interesa» e «Interesado», feed cronológico, Favoritos, pausar sugerencias, contenido sensible, reiniciar las recomendaciones y **Tu algoritmo**, que desde el 10/06/2026 permite elegir temas en el feed, Reels y Explorar (oficial, `tu-algoritmo`, `tarjeta-feed`).

Lo que se deduce (criterio): tocar «No me interesa» es una señal negativa que Explorar predice. Un gancho que promete algo que el video no entrega se paga.

## 8. Lo que no se pudo verificar en fuente oficial

Los pesos o multiplicadores. El orden de las tres señales. «Envíos por alcance» y «me gusta por alcance» como métricas de la app: son cálculos que se hacen a mano (ver [medicion.md](medicion.md)). Una hora dorada. Una frecuencia o una hora ideal. Que editar la descripción o poner enlaces castigue. Que los carruseles se vuelvan a mostrar desde la segunda diapositiva. Todo eso está en [mitos.md](mitos.md).
