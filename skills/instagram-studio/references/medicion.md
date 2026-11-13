# Medir

Ninguna IA entra a la cuenta. Emi manda **capturas** de las estadísticas y la IA anota los números.

## Qué ve Emi

Las estadísticas las tienen las cuentas públicas, personales o profesionales. En una cuenta de creador están en **Panel profesional → Estadísticas**, y en cada pieza en **Ver estadísticas** (oficial, `ayuda-insights-acceso`).

| Métrica en la app | Qué es (oficial, `ayuda-metricas`, `ayuda-metricas-reels`) | Clave al anotar |
|---|---|---|
| Visualizaciones | Veces que se reprodujo o mostró. En Reels cuenta cada inicio y cada repetición. | `visualizaciones` |
| Espectadores (cuentas alcanzadas) | Cuentas únicas que lo vieron al menos una vez. | `espectadores` |
| Me gusta, comentarios, guardados, veces compartido | Interacciones. | `me_gusta`, `comentarios`, `guardados`, `compartidos` |
| Tiempo de visualización y tiempo promedio | Total de tiempo reproducido y su promedio por vista inicial. | `tiempo_total_s`, `tiempo_promedio_s` |
| Seguidores | Cuentas que empezaron a seguir por esa pieza. | `seguidores` |
| Seguidores y no seguidores | Reparto de quién lo vio. | `pct_no_seguidores` |

**Impresiones** quedó obsoleta para lo publicado desde el 02/07/2024 (oficial, documentación de la API de Meta para desarrolladores; en la app, la métrica principal es Visualizaciones).

## Cálculos que no da la app

Mosseri pide mirar los **me gusta por alcance** y los **envíos por alcance**, pero la app no los trae: se calculan a mano (oficial, `mosseri-3-senales`).

- `me_gusta ÷ espectadores`
- `compartidos ÷ espectadores`
- `tiempo_promedio_s ÷ duración del Reel` (criterio; la tarjeta compara contra Reels de la misma duración)

## Cuándo

- **Reels y carruseles: a los 7 días.** La mayoría de las vistas llega en los primeros 3 días (terceros, Metricool 2026). A los 7 días el número ya es estable (criterio).
- Trial reels: a las 24 h (oficial).
- **Cada mes**: horas de actividad de los seguidores. Con ellas se reemplazan las `horas_hipotesis` del perfil.
- Los datos se guardan 90 días en el panel y hasta 2 años por pieza (oficial).

## Anotar

```bash
python3 skills/instagram-studio/scripts/igstudio.py publicado 2026-11-17-reel-matriz --pilar ia-derecho --formato reel \
  --fecha 2026-11-17 --hora 19:00 --url https://www.instagram.com/reel/… --gancho "…" --texto "descripción tal como salió"
python3 skills/instagram-studio/scripts/igstudio.py publicado 2026-11-17-reel-matriz --metricas \
  visualizaciones=1200 espectadores=900 compartidos=14 guardados=20 me_gusta=80 tiempo_promedio_s=21 seguidores=9
python3 skills/instagram-studio/scripts/igstudio.py aprender "El gancho con pantalla en movimiento retuvo más que el de cara a cámara"
python3 skills/instagram-studio/scripts/igstudio.py estado    # actualiza red/estado.json para Matriz de Redes
```

## Leer los números

- Una pieza no basta. Una lección necesita al menos 3 piezas comparables (criterio).
- Se compara a Emi consigo mismo, no con promedios de estudios.
- Si una pieza tiene muchos espectadores pero tiempo promedio bajo, el gancho atrajo y el cuerpo no sostuvo.
- Si tiene pocos espectadores pero muchos compartidos, el tema sirve y el gancho no.
- Si **Estado de la cuenta** dice que la cuenta no es recomendable, se detiene todo y se revisa con Emi (oficial, `ayuda-elegibilidad`).
