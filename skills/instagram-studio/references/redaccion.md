# Redactar y revisar una pieza

## Antes de escribir

1. Leer `cuenta/voz.md`, `cuenta/aprendizajes.md` y el tono de Vox Studio (`igstudio.py vox leer`).
2. `igstudio.py balance`: qué pilar toca.
3. Preguntarle a Emi, todo junto: qué pasó, qué piensa, qué quiere que haga quien lo vea y qué material tiene (video grabado, pantallas, fotos). **No se inventa nada.**
4. Si hay derecho, buscar la fuente oficial vigente, leerla y guardarla en `fuentes`.

## La pregunta que decide

Instagram nombra estas señales (ver [algoritmo.md](algoritmo.md)): que se vea hasta el final o más que otros Reels de su misma duración, que no se salte en los primeros 2 o 3 segundos, que se mande por mensaje, que se dé me gusta y que se siga al autor. Antes de dar por bueno un borrador:

- ¿Quien no conoce a Emi se queda después del segundo 3? ¿Qué ve y qué oye en ese momento?
- ¿A quién, concretamente, se lo mandaría alguien por mensaje, y por qué?
- ¿Alguien seguiría a Emi por esto? ¿Queda claro quién es?
- ¿El final cumple lo que prometió el gancho? Si no, la pieza gana «No me interesa».

Si la única respuesta honesta es «le darían me gusta», se cambia el ángulo, no los adjetivos.

## Reel

| Campo | Qué es |
|---|---|
| `gancho` | Lo que se ve y se oye en los primeros 3 s. Es una frase o una imagen. Agresivo está permitido; mentiroso, no. |
| `texto_en_pantalla` | El título que acompaña al gancho, si hay. Nunca debe cubrir la mayor parte de la imagen. |
| `descripcion` | Amplía el video, no lo repite. Pone primero las palabras con que lo buscarían («abogado», «IA», el tema), porque la búsqueda lee la descripción, no los comentarios. Cierra con una invitación genuina (a mandarlo a quien le sirva, o a preguntar), nunca con un anzuelo. |
| `hashtags` | 0 a 5, específicos. Clasifican, no dan alcance. |
| `portada` | Texto corto y legible en la cuadrícula del perfil, a 420×654. No se cambia después de publicar. |
| `video` | `duracion_s` (objetivo de 45 a 90 s; nunca más de 180), `origen` (`editor-studio`, `vox-studio` o `telefono`; nunca `tiktok`), `relacion` 9:16, `sonido`, `ia_fotorrealista`. |

**Frontera con quien hace el video.** Esta skill decide la idea, el público, el gancho, la descripción, la portada y la hora. **No escribe el guion completo**: el guion es de Vox Studio y la edición del video grabado, de Editor Studio. Ver [frontera.md](frontera.md).

## Carrusel

- **2 a 20 diapositivas**; para Emi, de 6 a 10 (criterio). La primera es portada y gancho.
- Una idea por diapositiva, con texto que se lea sin ampliar. La última dice qué hacer con lo aprendido.
- El feed premia que se recorra completo y que sea informativo (oficial). Si no aporta un paso, una cifra con fuente o un criterio, se corta.
- Con audio puede aparecer en la pestaña Reels (oficial).
- Colores: los de `cuenta/voz.md`.

## Que no suene a plantilla

El validador avisa de: «en el mundo actual», «es importante destacar», «en resumen», «sin lugar a dudas», «hoy en día», «no es X, es Y», «desbloquea», «potencia tu» y la raya larga. Mejor una frase que solo Emi diría, un detalle concreto o un número con su fuente.

**La IA propone, Emi reescribe.** Ninguna pieza se aprueba sin `"reescrito": true`.

## Formato del borrador

Va en `cuenta/privado/AAAA-Www.json`, que **no se sube** al repositorio. Puede ser una pieza, una lista o `{"piezas": [...]}`. Hay un ejemplo completo en [`assets/semana.ejemplo.json`](../assets/semana.ejemplo.json).

```json
{"id": "2026-11-17-reel-matriz", "formato": "reel", "pilar": "ia-derecho", "espacio": "personal",
 "fecha": "2026-11-17", "hora": "19:00",
 "gancho": "…", "texto_en_pantalla": "…", "descripcion": "…", "hashtags": ["abogados"],
 "portada": {"texto": "…", "archivo": ""},
 "video": {"duracion_s": 55, "origen": "editor-studio", "relacion": "9:16", "sonido": true,
           "ia_fotorrealista": false, "archivo": ""},
 "etiqueta_ia": false, "fuentes": [], "opinion_emi": "",
 "texto_otras_redes": {"tiktok": "…"},
 "por_que": "qué señal busca y para quién", "riesgos": "…",
 "reescrito": false, "estado": "borrador"}
```

## Revisar

```bash
python3 skills/instagram-studio/scripts/igstudio.py revisar cuenta/privado/2026-W47.json
python3 skills/instagram-studio/scripts/igstudio.py semana  cuenta/privado/2026-W47.json
```

Se corrige hasta que no queden errores y se atienden los avisos.
