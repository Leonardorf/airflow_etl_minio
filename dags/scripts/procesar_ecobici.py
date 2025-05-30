from pyspark.sql import SparkSession



# Crear sesión Spark con configuración para acceder a MinIO usando S3A
spark = SparkSession.builder \
    .appName("Procesar Ecobici y subir a MinIO") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "admin123") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .getOrCreate()

# Leer archivo crudo desde carpeta local
df_raw = spark.read.option("header", "true").csv("data/raw/usuarios_ecobici_2024.csv")

# Mostrar estructura inicial
df_raw.printSchema()
df_raw.show(5)

# Ejemplo simple de limpieza: eliminar filas con campos nulos
df_limpio = df_raw.dropna()

# Guardar resultado en MinIO
df_limpio.write.mode("overwrite") \
    .option("header", "true") \
    .csv("s3a://urban-mobility/usuarios/usuarios_ecobici_limpio.csv")

spark.stop()


