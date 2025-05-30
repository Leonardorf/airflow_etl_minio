# 🛠️ Proyecto ETL con Airflow, PySpark y MinIO

Este proyecto implementa un pipeline ETL utilizando Apache Airflow para orquestar tareas que descargan datos abiertos, los procesan con PySpark y los almacenan en MinIO, una solución local que emula un bucket S3.

💡 Fue desarrollado y probado en **Windows** usando **Docker Desktop**.

---

## 📊 Fuente de datos

Este proyecto utiliza un dataset de acceso público de la Ciudad Autónoma de Buenos Aires (CABA):

- **Usuarios del sistema de bicicletas públicas EcoBici**  
  Fuente: [datos abiertos CABA](https://data.buenosaires.gob.ar/dataset/bicicletas-publicas)  
  CSV directo: [usuarios_ecobici_2024.csv](https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/usuarios_ecobici_2024.csv)

🔎 **Uso sugerido**: análisis de patrones de uso por género, tipo de usuario (mensual / ocasional), comportamiento de movilidad sustentable, distribución temporal, etc.

---

## 🔍 Objetivo

Simular un entorno moderno de ingeniería de datos con herramientas de orquestación (Airflow), procesamiento distribuido (Spark) y almacenamiento tipo S3 (MinIO). Ideal para demostrar habilidades en proyectos ETL dentro de un portfolio de ciencia de datos.

---

## 🧰 Tecnologías utilizadas

- 🪂 **Apache Airflow**: Orquestación de workflows
- ⚡ **Apache Spark / PySpark**: Procesamiento de datos
- 📦 **MinIO**: Almacenamiento local estilo S3
- 🐳 **Docker + Docker Compose**: Contenedores para el entorno completo
- 🐍 **Python**
- 📊 (Opcional) Jupyter Notebook para análisis posterior

---

## 📁 Estructura del proyecto

```bash
airflow_etl_minio/
├── dags/
│   ├── etl_minio_dag.py              # DAG principal
│   └── scripts/
│       ├── descargar_datos.py        # Descarga datasets
│       ├── procesar_spark.py         # Procesamiento PySpark
│       └── subir_a_minio.py          # Carga a MinIO vía boto3
├── docker/
│   ├── docker-compose.yml            # Servicios: Airflow, Spark, MinIO
│   ├── Dockerfile.spark              # Imagen personalizada para Spark
│   └── requirements-airflow.txt      # Requisitos de Airflow
├── notebooks/
│   └── exploracion.ipynb             # Exploración y visualización
├── data/                             # (Opcional) Datos locales
├── .env.example                      # Variables de entorno
├── .gitignore
└── README.md
```

---

## 🚀 Cómo ejecutar el proyecto

### ✅ Requisitos previos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado en Windows
- Git

### 🧪 Instrucciones

1. **Cloná el repositorio**
   ```bash
   git clone https://github.com/Leonardorf/airflow_etl_minio.git
   cd airflow_etl_minio
   ```

2. **Configurá las variables de entorno**
   ```bash
   cp .env.example .env
   ```

3. **Levantá los servicios**
   ```bash
   docker-compose -f docker/docker-compose.yml up --build
   ```

4. **Accedé a las interfaces**
   - 🌬️ Airflow: [http://localhost:8080](http://localhost:8080)
   - 🪣 MinIO: [http://localhost:9001](http://localhost:9001)
     - Usuario: `minio`
     - Contraseña: `minio123`

---

## ⚙️ Detalles del DAG

El DAG `etl_minio_dag.py` define el siguiente flujo de trabajo:

1. **Descargar datos** desde una fuente pública (ej. movilidad urbana)
2. **Procesar datos** con PySpark (limpieza, transformación, agregados)
3. **Subir resultados** a un bucket en MinIO (como si fuera Amazon S3)

---

## 📓 Análisis y visualización

Podés explorar los datos procesados usando el notebook ubicado en `notebooks/exploracion.ipynb`, conectándote a MinIO o leyendo los archivos locales descargados.

---

## 📂 .env.example

```dotenv
# MinIO
MINIO_ACCESS_KEY=minio
MINIO_SECRET_KEY=minio123
S3_ENDPOINT=http://minio:9000
```

---

## 🛑 .gitignore recomendado

```gitignore
__pycache__/
*.pyc
.env
data/
tmp/
logs/
```

---

## 📄 Licencia

Este proyecto está disponible bajo la licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 👤 Autor

Desarrollado por **Leonardorf** como parte de su portfolio de ciencia de datos.  
GitHub: [github.com/Leonardorf](https://github.com/Leonardorf)

---

## 🏁 Estado del proyecto

✅ Funcional y probado localmente en Windows con Docker Desktop.  
🛠️ Puede expandirse para ejecutar sobre S3 real o incluir visualización automática.
