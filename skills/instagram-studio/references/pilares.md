# Pilares y límites

## Pilares

| Pilar | `pilar` | Qué entra | Formato que mejor le va (criterio) |
|---|---|---|---|
| IA + Derecho en México | `ia-derecho` | Las herramientas que Emi construyó, cómo trabaja un abogado con ellas y derecho útil explicado con su fuente. | Reel para el gancho; carrusel para el paso a paso. |
| Estilo de vida y gym | `lifestyle` | Rutina, gym, maestría, vida de abogado joven. | Reel a cuadro y foto propia. |
| Opinión política | `politica` | Análisis jurídico con postura, como crítico independiente. | Reel de opinión o carrusel con argumento y fuente. |

**Proporción propuesta: 40/40/20**, pendiente de que Emi la confirme (`cuenta/perfil.json` → `balance_estado`). En X decidió partes iguales. La política lleva menos peso porque Meta cuenta las leyes como contenido político y quien no sigue a Emi puede tener limitado verlo ([algoritmo.md](algoritmo.md) §4). Si Emi elige partes iguales, se cambia `balance` en el perfil y listo.

Durante la campaña de lanzamiento (17 al 26/11/2026) todo es `ia-derecho`. El validador solo avisa del desbalance a partir de 3 piezas por semana, y es un aviso, no un error.

## Límites de Emi

Son errores en el validador, salvo donde se indica.

1. **Nunca clientes ni datos de asuntos**, ni siquiera anonimizados: nada de números de expediente, juntas o salas ligadas a asuntos, folios ni nombres de clientes. Esto incluye la **pantalla**: grabaciones de Matriz, DOF y Boletines con datos de demostración o difuminados. El validador revisa el texto; la pantalla la revisan Editor Studio y Emi.
2. **No se nombra a Castorena Abogados** ni a sus licenciados. Los colores navy y dorado que Emi eligió no lo nombran.
3. **Nunca decir que una pieza la hizo, la armó o la editó una IA** (Emi, 13/11/2026). El lema «herramientas que construí uniendo IA y Derecho» sí vale: habla de lo que él construyó.
4. **Sin insultos a personas.** Es límite de Emi y además las Normas comunitarias de Instagram prohíben el acoso.
5. **Todo derecho con fuente oficial verificada** (`fuentes`). Una pieza informa u opina; no es asesoría para un caso.
6. **Política: primero la postura de Emi** (`opinion_emi`). No habla a nombre del PAN ni de Acción Juvenil, ni usa sus logotipos.
7. **No se inventan** vivencias, opiniones, cifras ni citas. La IA propone y Emi reescribe (`reescrito`).

## Lo que Emi quitó (13/11/2026)

Emi pidió **no aplicar avisos de autoelogio ni de ética gremial** (Código de Ética de la Barra Mexicana) y permitir **ganchos agresivos**. La skill no los marca. Siguen aplicando:

- **La ley.** Por ejemplo, el artículo 42 de la Ley de Profesiones pide que la publicidad profesional diga la institución que expidió el título; aplica si una pieza anuncia servicios.
- **Las reglas de Instagram.** Un gancho agresivo está bien; un anzuelo de interacción («comenta X y te mando…») o un *clickbait* que no cumple lo que promete saca la pieza de las recomendaciones.
- **Los límites de arriba.**

## Misma idea, otra red

La idea se adapta a cada red y el texto nunca se pega igual. Si la pieza trae `texto_otras_redes`, el validador marca error cuando la descripción es casi idéntica (90 % de parecido o más). Las reglas de X están en `lianfixx/X`; aquí se enlazan, no se copian.
