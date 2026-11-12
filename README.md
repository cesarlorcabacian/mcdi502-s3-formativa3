# MCDI502 · Semana 3 · Formativa 3 — Preparación para el Taller II

[![validate](https://github.com/cesarlorcabacian/mcdi502-s3-formativa3/actions/workflows/validate.yml/badge.svg)](https://github.com/cesarlorcabacian/mcdi502-s3-formativa3/actions/workflows/validate.yml)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cesarlorcabacian/mcdi502-s3-formativa3/blob/main/notebooks/MCDI502_S3_EvaluacionFormativa.ipynb)

> Repositorio: <https://github.com/cesarlorcabacian/mcdi502-s3-formativa3> · Autor: [@cesarlorcabacian](https://github.com/cesarlorcabacian)
> El botón de Colab funciona si el repositorio es **público**; si es privado, descarga el `.ipynb` y súbelo manualmente.

Curso: MCDI502 Gestión de Datos y Tecnologías Big Data, Magíster en Ciencia de Datos (UNAB)

Integrantes: Fernanda Ovalle Román · Sebastián Cajales Cid · Jorge Álvarez Ossandón ·  César Lorca Bacián

Actividad **grupal, sin nota (0%)** del curso *Gestión de Datos y Tecnologías Big Data* (UNAB).
Practica el flujo de ingesta → transformación → consulta SQL → integración con **Apache Spark** usando dos APIs públicas.

## Qué hace

| Etapa | Descripción | Resultado esperado |
|---|---|---|
| 1. Instalación | `requests`, `pandas`, `pyspark`, `findspark` | ✅ Instalación completada |
| 2. Configuración | Imports, constantes y `SparkSession` | ✅ Entorno configurado · ✅ SparkSession creada |
| 3. OpenMeteo | 5 registros (temperatura, humedad, precipitación, viento, UV) | DataFrame de 5 registros |
| 4. AQICN | 5 registros (PM2_5, PM10, O3, NO2) | DataFrame de 5 registros |
| 5. Transformaciones | `temperatura_fahrenheit`, `promedio_contaminantes` | Columnas nuevas, 2 decimales |
| 6. Consultas SQL | 3 consultas sobre vistas temporales | Estadísticas de temperatura, promedio de contaminantes, humedad promedio |
| 7. Integración básica | DataFrame unificado + resumen por fuente | OpenMeteo 5 · AQICN 5 |
| 8. Resumen final | Checks automáticos | **ACTIVIDAD FORMATIVA COMPLETADA** |

## Estructura del repositorio

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── MCDI502_S3_EvaluacionFormativa.ipynb   # entregable principal (Google Colab)
├── src/
│   └── formativa3.py                           # misma lógica como script ejecutable
├── docs/
│   ├── 01_procedimiento.md                     # paso a paso fiel a la guía
│   ├── 02_decisiones_y_notas.md                # decisiones de diseño y discrepancias
│   ├── 03_checklist_entrega.md                 # checklist de cierre y autoevaluación
│   └── 04_publicacion_github.md                # cómo publicar este repo en tu cuenta
└── .github/workflows/
    └── validate.yml                            # valida notebook y script en cada push
```

## Cómo ejecutarlo

### Opción A — Google Colab (recomendada, es lo que pide la guía)
1. Abre <https://colab.research.google.com> → **Archivo > Subir cuaderno** → `notebooks/MCDI502_S3_EvaluacionFormativa.ipynb`.
2. **Archivo > Guardar una copia en Drive** y renombra a `MCDI502_S3_EvaluacionFormativa_[NombreGrupo]`.
3. Ejecuta **todas las celdas en orden**, esperando que cada una termine.

### Opción B — Local (clonando el repo)
```bash
git clone https://github.com/cesarlorcabacian/mcdi502-s3-formativa3.git && cd mcdi502-s3-formativa3
```

#### Requisitos locales (Java 8/11/17)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/formativa3.py            # 5 registros por fuente
python src/formativa3.py --n 3      # prueba rápida
```

## Fuentes de datos
- **OpenMeteo** — `https://api.open-meteo.com/v1/forecast` (Viña del Mar: -33.02457, -71.55183).
- **AQICN / WAQI** — `http://api.waqi.info/feed/{city}/?token=demo`.

> No se incluyen credenciales. MongoDB y MySQL/PHP son solo referencia para la sumativa y **no** se usan aquí.

## Integridad académica
El trabajo debe ser de autoría propia del grupo, citando las fuentes utilizadas (notebooks base del curso y documentación de las APIs). Este repositorio es una guía de trabajo: revisa y adapta el código antes de entregarlo.

## Integrantes
- César Antonio Lorca Bacian ([@cesarlorcabacian](https://github.com/cesarlorcabacian))
- [Resto de integrantes del grupo]

## Curso
- MCDI502 · Universidad Andrés Bello · Semana 3 (plazo: domingo 15-nov-2026, 23:59)
