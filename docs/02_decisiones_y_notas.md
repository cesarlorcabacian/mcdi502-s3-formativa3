# Decisiones de diseño y notas

## Discrepancias detectadas en la guía
- Los pasos 4–8 mencionan "parte 1, 4, 5, 6 y 7". Se interpretó como desorden de numeración: el notebook usa partes 1–8 en secuencia, con el mismo orden de ejecución.
- El Paso 2 cita `MCDI502_S3_EvaluacionFormativa.ipynb`, que no fue entregado; este repositorio lo reconstruye a partir de los 4 notebooks base.

## Fidelidad a la guía
- **5 registros por fuente** (los notebooks base capturan 20).
- **OpenMeteo:** solo las 5 variables listadas (se omite `wind_direction_10m` del base).
- **AQICN:** solo `PM2_5`, `PM10`, `O3`, `NO2` (se omite `SO2`); la columna se nombra `PM2_5` (no `PM2.5`) para evitar problemas con el punto en Spark.
- Nombres de vistas SQL: `openmeteo_data` y `aqicn_data`.

## Robustez añadida
- Timeout y manejo de excepciones en las llamadas HTTP.
- Reintentos acotados hasta completar los 5 registros.
- AQICN: se descartan registros sin alguno de los 4 contaminantes (evita `NULL` en el promedio).
- `assert` de cantidad de registros y checks finales en el resumen.

## Integración
`unionByName(..., allowMissingColumns=True)` une ambas fuentes aunque sus esquemas difieran (columnas ausentes quedan en `NULL`), más una columna `fuente`.

## Advertencias
- AQICN con token `demo`: hasta donde se sabe, suele devolver una estación fija (p. ej. Shanghái) sin importar `city`. No afecta el objetivo de la actividad.
- OpenMeteo entrega valores "current" que se actualizan cada ~15 min; es normal que varios registros consecutivos repitan valores.
- Seguridad: no subir tokens ni URIs con credenciales al repositorio (el notebook base de MongoDB contiene una URI; aquí no se usa ni se incluye).
