# Fronteras con las otras skills

Cada skill trabaja en su propio carril y en su propio repositorio. instagram-studio **no edita** los repositorios de las demás: lee lo que publican y les deja ideas o peticiones en `puente/`.

| Skill | Repositorio | Qué hace ella | Qué hace instagram-studio |
|---|---|---|---|
| **Historias Studio** | `lianfixx/HISTORIAS-` | Las **historias** de Instagram: plan, láminas, motor de dibujo y entrega en Drive. | Nada con historias. Si un Reel merece historias que lo empujen, deja la idea en `puente/para-historias.md` y Emi se la pide a Historias Studio. |
| **Vox Studio** | `lianfixx/VIDEOS-IA-SKILL-MILLA` | El **guion completo**, la voz, las imágenes, la música y el render de los shorts del espacio `personal`. | Decide qué video conviene, para quién, el **gancho de los primeros 3 s**, la descripción, la portada, la hora y la etiqueta de IA si aplica. Deja ideas en `puente/para-vox.md` (`igstudio.py vox idea "…"`). Lee el tono y las lecciones con `igstudio.py vox leer`. |
| **Editor Studio** | (de la sesión de Matriz de Redes) | Edita los videos que **graba Emi**. | Le pasa el gancho, la duración objetivo (menos de 3 min), el formato 9:16, la portada de 420×654 y los candados de pantalla. Recibe el MP4 limpio. |
| **x-viral** | `lianfixx/X` | La cuenta de X. | Nada en X. La misma idea se adapta; el texto no se pega. |
| **TikTok y LinkedIn** | sus propios repositorios | Sus redes. | Lo mismo que con X. El video de TikTok nunca se sube a Instagram con marca de agua. |
| **Matriz de Redes** | `lianfixx/REDES` | Coordina: qué idea va a qué red, calendario consolidado y retroalimentación. | Expone su estado en [`red/estado.json`](../../../red/estado.json) (contrato `redes-estado/0.1.1`) con `igstudio.py estado`. |

## Con Vox Studio, en detalle

- Un video de Vox para Instagram necesita de esta skill la idea, el público, el gancho, la duración objetivo y el candado de IA. Esta skill **no** escribe escenas ni guion.
- **Candado de IA (13/11/2026):** en los videos para Instagram, Vox muestra estilo collage o ilustrado, nada fotorrealista. Si algún día hay imagen o voz realistas, `etiqueta_ia: true` y Emi activa la etiqueta al publicar. Ningún texto dice que lo hizo una IA.
- Vox hoy reconoce solo el puente de `lianfixx/X`. Para que lea también el de Instagram se dejó [`puente/PETICION-vox.md`](../../../puente/PETICION-vox.md); aplicarla le toca a Vox Studio, con permiso de Emi.

## Con Historias Studio

Las historias quedan fuera de esta skill. Que Historias Studio lea `puente/para-historias.md` es una decisión de Emi.
