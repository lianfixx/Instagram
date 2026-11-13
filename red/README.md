# Estado para Matriz de Redes

`estado.json` sigue el contrato `redes-estado/0.1.1` que propuso la sesión «Matriz de Redes» (`lianfixx/REDES`) el 13/11/2026: cuenta, cadencia con su fuente y certeza, formatos, publicados con su huella y sus métricas, lecciones, ideas para otras skills y pendientes de Emi. Es un índice que se genera solo; no se edita a mano:

```bash
python3 skills/instagram-studio/scripts/igstudio.py estado
```

Los grados de certeza son `oficial`, `terceros` y `criterio`. Las métricas van con los nombres de Instagram en `snake_case`.
