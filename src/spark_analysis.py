from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_processed.csv"
OUTPUT_DIR = BASE_DIR / "data" / "analytics"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

spark = (
    SparkSession.builder
    .appName("DataAnalytics")
    .master("local[*]")
    .getOrCreate()
)

df = spark.read.csv(
    str(INPUT_FILE),
    header=True,
    inferSchema=True
)

print("\n=== TOTAL DE REGISTROS ===")
print(df.count())

# Análise por sentimento
sentimento = df.groupBy("sentimento_inicial").count()

print("\n=== AVALIAÇÕES POR SENTIMENTO ===")
sentimento.show()

sentimento.toPandas().to_csv(
    OUTPUT_DIR / "sentimento.csv",
    index=False,
    encoding="utf-8"
)

# Análise por categoria
categorias = df.groupBy("categoria").count()

print("\n=== REGISTROS POR CATEGORIA ===")
categorias.show()

categorias.toPandas().to_csv(
    OUTPUT_DIR / "categorias.csv",
    index=False,
    encoding="utf-8"
)

# Média de avaliação por categoria
avaliacao_categoria = df.groupBy("categoria").agg(
    avg("avaliacao").alias("media_avaliacao")
)

print("\n=== MÉDIA DE AVALIAÇÃO POR CATEGORIA ===")
avaliacao_categoria.show()

avaliacao_categoria.toPandas().to_csv(
    OUTPUT_DIR / "avaliacao_categoria.csv",
    index=False,
    encoding="utf-8"
)

print("\nArquivos analíticos gerados com sucesso!")

spark.stop()