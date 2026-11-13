# Entregar para publicar

## Regla de oro

**Ninguna IA inicia sesión en la cuenta de Emi** ni publica, programa, comenta, sigue, da me gusta o manda mensajes por él. Es regla común de Emi desde el 11/11/2026, cuando X bloqueó el inicio de sesión desde la computadora en la nube; no se intenta en Instagram. La IA entrega y Emi publica. Box sirve solo para ver perfiles y páginas públicas.

## Requisitos de cada pieza

`igstudio.py entregar ARCHIVO ID` solo imprime el bloque si se cumple todo esto:

- No hay errores de revisión.
- `"reescrito": true`: Emi reescribió el texto.
- Emi **aprobó ese texto exacto** con sus archivos y su hora, y la IA lo anotó **después** con `igstudio.py aprobar ARCHIVO ID --medio "…"`. La orden guarda una huella; si cambia cualquier texto, archivo o la hora, la aprobación deja de valer. Anotar una aprobación que Emi no dio es la falta más grave en este repositorio.
- `fecha` no pasada y `hora` en formato HH:MM, en hora del centro de México.

Emi aprueba en un paquete semanal, pero **pieza por pieza**. «Aprobado todo» sin haber visto cada pieza no basta.

## El bloque

```text
REEL 2026-11-17-reel-matriz · martes 17/11, 19:00 (centro de México) · pilar: ia-derecho
Video: (archivo de Editor Studio)
Portada: (archivo) · texto: …
Etiqueta «Información de IA»: no
---- descripción (copiar tal cual) ----
(texto aprobado)

#hashtag1 #hashtag2
```

## Cómo publica Emi

1. En la app: **+** → Reel (o Publicación para carrusel y foto) → elige el video o las imágenes.
2. Portada: sube el archivo de portada. **No se puede cambiar después.**
3. Pega la descripción tal cual.
4. Si el bloque dice «ACTIVARLA»: en la pantalla de creación, **Add AI label** (en español, «Etiqueta de IA»), según la ayuda de Instagram.
5. Para programar: **More options → Schedule this post** (en español, «Más opciones → Programar esta publicación»), según la ayuda → fecha y hora → Programar. Se puede hasta 30 días antes, con cuenta pública (oficial).
6. Le dice a la IA «publicado» y, si puede, pega el enlace.

Los nombres de los menús son orientativos y pueden cambiar de una versión de la app a otra: no se han probado con la cuenta de Emi. Si no aparecen, buscar «Etiqueta de IA» o «Programar» en las opciones de la pantalla de creación.

La IA cambia el `estado` solo cuando Emi lo confirma; no dice «programado» ni «publicado» por su cuenta.

## Si algo cambia

Si una pieza ya programada tiene que cambiar, se avisa a Emi y él la edita o la borra. Si cambia el texto, es un borrador nuevo: se revisa y Emi lo vuelve a aprobar.
