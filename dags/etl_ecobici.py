from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import os
import subprocess

default_args = {"owner": "airflow", "start_date": datetime(2024, 1, 1)}

with DAG("etl_ecobici",
         default_args=default_args,
         schedule_interval=None,
         catchup=False) as dag:

    # Tarea 1: Descargar CSV crudo
    def descargar_csv():
        import requests
        os.makedirs("data/raw", exist_ok=True)
        url = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/usuarios_ecobici_2024.csv"
        r = requests.get(url)
        with open("data/raw/usuarios_ecobici_2024.csv", "wb") as f:
            f.write(r.content)

    # Tarea 3: Subir a MinIO
    def subir_a_minio():
        subprocess.run(["python", "dags/scripts/subir_minio.py"], check=True)

    # Operator 1: Descargar CSV
    descargar = PythonOperator(
        task_id="descargar_csv",
        python_callable=descargar_csv
    )

    # ✅ Operator 2: Ejecutar spark-submit dentro del contenedor spark que ya está corriendo
    procesar = BashOperator(
        task_id="procesar_datos",
        bash_command="docker exec spark spark-submit /app/dags/scripts/procesar_ecobici.py",
    )

    # Operator 3: Subir a MinIO
    subir = PythonOperator(
        task_id="subir_minio",
        python_callable=subir_a_minio
    )

    # Dependencias
    descargar >> procesar >> subir

