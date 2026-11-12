# Procedimiento (fiel a la guía de Canvas)

> Actividad grupal · sin nota · 2 intentos · no se sube ningún archivo.
> Disponible 11-nov 00:00 → 15-nov 23:59.

## Paso 1 — Revisar los archivos de ejemplo (≈5 min)
Revisar `BaseEjemploOpenMeteo.ipynb` y `BaseEjemploAQICN.ipynb` y responder:
- **¿URL base?** OpenMeteo: `https://api.open-meteo.com/v1/forecast` · AQICN: `http://api.waqi.info/feed/{city}/?token={token}`.
- **¿Variables?** OpenMeteo: temperatura, humedad, precipitación, viento, UV · AQICN: PM2.5, PM10, O3, NO2 (+SO2 en el base).
- **¿Cómo se procesa el JSON?** OpenMeteo: `.json().get("current")` · AQICN: `data["data"]["iaqi"]`.

Revisar además (referencia sumativa, no se usan): `BaseEjemploMongoDB.ipynb`, `BaseEjemploMysqlPHP_APIRest.ipynb`.

## Paso 2 — Abrir el notebook en Colab
1. <https://colab.research.google.com> → cargar `MCDI502_S3_EvaluacionFormativa.ipynb`.
2. Archivo > Guardar una copia en Drive.
3. Renombrar: `MCDI502_S3_EvaluacionFormativa_[NombreGrupo]`.

## Paso 3 — Partes 1 y 2 (instalación y configuración)
- Instalar dependencias (2–3 min) → ✅ Instalación completada.
- Configurar entorno → ✅ Entorno configurado.
- Crear SparkSession → ✅ SparkSession creada.

## Paso 4 — Ingesta OpenMeteo
- Conecta a la API, obtiene **5** registros, crea DataFrame Spark.
- Variables: `temperature_2m`, `relative_humidity_2m`, `precipitation`, `wind_speed_10m`, `uv_index`.
- Verificar: ✅ DataFrame OpenMeteo: 5 registros · ✅ tabla con 5 registros.

## Paso 5 — Ingesta AQICN
- Conecta a la API, obtiene **5** registros, crea DataFrame Spark.
- Variables: `PM2_5`, `PM10`, `O3`, `NO2`.
- Verificar: ✅ DataFrame AQICN: 5 registros · ✅ tabla con 5 registros.

## Paso 6 — Transformaciones
| Columna | Fórmula | Redondeo |
|---|---|---|
| `temperatura_fahrenheit` | (°C × 9/5) + 32 | 2 decimales |
| `promedio_contaminantes` | (PM2_5 + PM10 + O3 + NO2) / 4 | 2 decimales |

Verificar: ✅ columnas creadas · ✅ valores mostrados.

## Paso 7 — Consultas SQL
```sql
-- Consulta 1: Estadísticas de temperatura
SELECT MAX(temperature_2m) AS temp_maxima,
       MIN(temperature_2m) AS temp_minima,
       ROUND(AVG(temperature_2m), 2) AS temp_promedio
FROM openmeteo_data;

-- Consulta 2: Promedio de contaminantes
SELECT ROUND(AVG(promedio_contaminantes), 2) AS promedio_general
FROM aqicn_data;

-- Consulta 3: Humedad relativa promedio
SELECT ROUND(AVG(relative_humidity_2m), 2) AS humedad_promedio
FROM openmeteo_data;
```

## Paso 8 — Integración básica
DataFrame unificado con ambas fuentes y resumen por fuente:

| fuente | registros |
|---|---|
| OpenMeteo | 5 |
| AQICN | 5 |

## Paso 9 — Resumen final
Ejecutar la celda final y verificar el mensaje **ACTIVIDAD FORMATIVA COMPLETADA**.

## Recomendaciones de la guía
- **Antes:** revisar los 4 ejemplos, entender cada conexión, tener internet.
- **Durante:** ejecutar en orden sin saltarse celdas; esperar a que cada una termine; ante errores, leer el mensaje y consultar al docente.
- **Después:** revisar resultados, guardar en Drive, compartir el enlace con el docente, grabar el video explicativo.
- **Posterior:** tras publicarse el solucionario (Anuncio en Canvas), responder el Cuestionario de Autoevaluación.

## Qué prepara para la Sumativa (Taller II)
4 fuentes (en lugar de 2) · 20 registros por fuente (en lugar de 5) · 2 columnas calculadas más complejas · 7 consultas SQL más avanzadas · integración completa con `UNION ALL`.
