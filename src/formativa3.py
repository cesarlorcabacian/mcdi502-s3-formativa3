#!/usr/bin/env python3
"""MCDI502 · S3 · Formativa 3 — misma lógica del notebook, como script.

Uso:  python src/formativa3.py [--n 5]
Requiere Java instalado (para PySpark).
"""
import argparse
import time
from datetime import datetime

import pandas as pd
import requests
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

LATITUD, LONGITUD = -33.02457, -71.55183
VARIABLES = ["temperature_2m", "relative_humidity_2m", "precipitation",
             "wind_speed_10m", "uv_index"]
AQICN_URL = "http://api.waqi.info/feed/{city}/?token={token}"


def obtener_openmeteo():
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={LATITUD}"
           f"&longitude={LONGITUD}&current={','.join(VARIABLES)}"
           f"&timezone=America/Santiago")
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            return r.json().get("current", {})
    except requests.RequestException as e:
        print(f"⚠️ Error de conexión: {e}")
    return {}


def capturar_openmeteo(n, pausa=10):
    historico, intentos = [], 0
    while len(historico) < n and intentos < n * 3:
        intentos += 1
        actual = obtener_openmeteo()
        if actual:
            fila = {"tiempo": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            for v in VARIABLES:
                val = actual.get(v)
                fila[v] = float(val) if val is not None else None
            historico.append(fila)
            print(f"OpenMeteo {len(historico)}/{n}")
        if len(historico) < n:
            time.sleep(pausa)
    assert len(historico) == n, "No se capturaron los registros de OpenMeteo"
    return historico


def capturar_aqicn(n, city="santiago", token="demo", pausa=1):
    url, records, intentos = AQICN_URL.format(city=city, token=token), [], 0
    while len(records) < n and intentos < n * 4:
        intentos += 1
        try:
            data = requests.get(url, timeout=30).json()
        except (requests.RequestException, ValueError) as e:
            print(f"⚠️ Error de conexión/JSON: {e}")
            time.sleep(pausa)
            continue
        if data.get("status") == "ok":
            iaqi = data["data"]["iaqi"]
            fila = {"PM2_5": iaqi.get("pm25", {}).get("v"),
                    "PM10": iaqi.get("pm10", {}).get("v"),
                    "O3": iaqi.get("o3", {}).get("v"),
                    "NO2": iaqi.get("no2", {}).get("v")}
            if all(v is not None for v in fila.values()):
                records.append(fila)
                print(f"AQICN {len(records)}/{n}")
        if len(records) < n:
            time.sleep(pausa)
    assert len(records) == n, "No se capturaron los registros de AQICN"
    return records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=5, help="registros por fuente")
    n = ap.parse_args().n

    spark = (SparkSession.builder.master("local[*]")
             .appName("FormativaS3_MCDI502").getOrCreate())
    print("✅ SparkSession creada")

    df_om = spark.createDataFrame(pd.DataFrame(capturar_openmeteo(n)))
    print(f"✅ DataFrame OpenMeteo: {df_om.count()} registros")
    df_om.show(truncate=False)

    df_aq = spark.createDataFrame(pd.DataFrame(capturar_aqicn(n)).astype(float))
    print(f"✅ DataFrame AQICN: {df_aq.count()} registros")
    df_aq.show(truncate=False)

    df_om = df_om.withColumn("temperatura_fahrenheit",
                             F.round(F.col("temperature_2m") * 9 / 5 + 32, 2))
    df_aq = df_aq.withColumn(
        "promedio_contaminantes",
        F.round((F.col("PM2_5") + F.col("PM10") + F.col("O3") + F.col("NO2")) / 4, 2))
    df_om.select("temperature_2m", "temperatura_fahrenheit").show()
    df_aq.show()

    df_om.createOrReplaceTempView("openmeteo_data")
    df_aq.createOrReplaceTempView("aqicn_data")
    spark.sql("""SELECT MAX(temperature_2m) AS temp_maxima,
                        MIN(temperature_2m) AS temp_minima,
                        ROUND(AVG(temperature_2m), 2) AS temp_promedio
                 FROM openmeteo_data""").show()
    spark.sql("""SELECT ROUND(AVG(promedio_contaminantes), 2) AS promedio_general
                 FROM aqicn_data""").show()
    spark.sql("""SELECT ROUND(AVG(relative_humidity_2m), 2) AS humedad_promedio
                 FROM openmeteo_data""").show()

    unif = (df_om.withColumn("fuente", F.lit("OpenMeteo"))
            .unionByName(df_aq.withColumn("fuente", F.lit("AQICN")),
                         allowMissingColumns=True))
    (unif.groupBy("fuente").count().withColumnRenamed("count", "registros")
         .orderBy(F.desc("fuente")).show())

    ok = (df_om.count() == n and df_aq.count() == n
          and unif.count() == 2 * n)
    print("🎉 ACTIVIDAD FORMATIVA COMPLETADA" if ok
          else "⚠️ Revisar resultados")
    spark.stop()


if __name__ == "__main__":
    main()
