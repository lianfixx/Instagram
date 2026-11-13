# Estudios de terceros

Son de empresas externas con método declarado y se leyeron el 13/11/2026. Miden **correlación** en miles de cuentas, que en su mayoría no son de abogados ni de México. Sirven como **hipótesis de partida**: en cuanto la cuenta de Emi tenga sus propias estadísticas, mandan esas. Las fuentes están en [`data/fuentes.json`](../data/fuentes.json), grado «terceros».

| Tema | Hallazgo | Estudio |
|---|---|---|
| Formato | El Reel alcanza más: **1.36×** lo que un carrusel (análisis de más de 4 M publicaciones de **enero de 2022 a octubre de 2024**). El carrusel logra más interacción sobre alcance en 2025: **6.90 %**, frente a 3.31 % del Reel (medianas, sin muestra declarada). | Buffer, *State of Social Media Engagement 2026* (05/03/2026) |
| Formato | Interacción sobre seguidores: carrusel 0.55 %, Reel 0.52 %, foto 0.37 %. **En visualizaciones por publicación, el carrusel supera al Reel** en todos los tamaños de cuenta (por ejemplo, de 5K a 10K seguidores: 2,117 frente a 1,000). Contradice a Buffer: el formato que más alcanza no está resuelto. | Socialinsider (67.5 M publicaciones de cuentas de empresa, 2025-2026) |
| Formato | El Reel logra más de 4 veces las interacciones de una foto. El carrusel logra **9 veces** más guardados. | Metricool 2026 (24 M publicaciones) |
| Duración del Reel | Mejor tramo, **de 45 a 60 s**. Entre 30 s y 3 min los resultados son casi iguales. Por debajo de 30 s rinden menos, y por encima de 3 min, la mitad. | Socialinsider (9.8 M Reels, enero-junio de 2026) |
| Frecuencia | Cada cuenta comparada consigo misma: con **3 a 5 publicaciones por semana** se crece más del doble que con 1 o 2. Con 10 o más se crece más, pero cuesta mucho más. | Buffer (2.1 M publicaciones, 102,000 cuentas, 13/08/2025) |
| Horas | Los estudios no coinciden y **ninguno tiene datos de México**. Buffer apunta al jueves a las 9 a. m. y al miércoles a las 12 y a las 6 p. m. Sprout, al martes y miércoles por la tarde. Metricool y HypeAuditor, a las 8 p. m. | Buffer (9.6 M), Sprout, Metricool + HypeAuditor *Instagram Content Playbook 2025* (700 M) |
| Cuándo llegan las vistas | La mayoría en los **primeros 3 días**, no en la primera hora. | Metricool 2026 |
| Hashtags | Las publicaciones con hashtags tuvieron 31.7 % menos vistas (correlación; puede deberse al tipo de cuenta que los usa). | Metricool 2026 |
| Collab | En perfiles de menos de 10K seguidores, las colaboraciones aceptadas logran unas 5 veces más interacción. El propio estudio advierte de un sesgo de selección. Emi decidió no usar Collab con MILLA. | Emplifi (520K publicaciones, primer semestre de 2026) |
| Número de diapositivas | El único estudio con método es de 2020 (Socialinsider): rendían mejor los de 10. Está viejo; no se usa como regla. | Socialinsider 2020 |

## Qué toma la skill

- Las **horas de partida** (`cuenta/perfil.json` → `horas_hipotesis`): entre semana, 13:00 y 19:00. Es criterio sobre estudios que no coinciden; se cambian por las horas de actividad que muestren las estadísticas de Emi tras 3 o 4 semanas.
- La **cadencia** de 3 a 5 piezas por semana sale de Buffer; el mínimo de 2 en una semana difícil y el máximo de 1 al día son criterio. Instagram solo pide constancia.
- Reels de **45 a 60 s** como objetivo y nunca más de 3 min. El límite de 3 min es oficial; el tramo, de terceros.
- Carrusel para profundidad, guardados e interacción; Reel para alcance a no seguidores según Buffer y los anuncios oficiales sobre Reels, aunque Socialinsider encuentra más visualizaciones en carruseles. Se decide con los números de Emi.
