
import os
from pathlib import Path

import pandas as pd
from pymongo import MongoClient

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "reviews_analytics.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# No Windows, usa localhost por padrão.
# No Docker, o endereço será configurado pela variável MONGODB_URI.
MONGODB_URI = os.getenv(
    "MONGODB_URI",
    "mongodb://localhost:27017/",
)

print("Conectando ao MongoDB...")
client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=10000)

try:
    database = client["data_analytics"]
    collection = database["reviews_processed"]

    print("Verificando conexão...")
    client.admin.command("ping")

    print("Extraindo dados do MongoDB...")
    documentos = list(collection.find({}, {"_id": 0}))

    if not documentos:
        print("Nenhum dado encontrado no MongoDB.")
        raise SystemExit(1)

    df = pd.DataFrame(documentos)

    if "avaliacao" in df.columns:
        df["avaliacao"] = pd.to_numeric(
            df["avaliacao"], errors="coerce"
        )

    if "id" in df.columns:
        df["id"] = pd.to_numeric(
            df["id"], errors="coerce"
        )

    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig",
    )

    print()
    print("ETL concluído com sucesso!")
    print(f"Registros exportados: {len(df)}")
    print("Arquivo criado em:")
    print(OUTPUT_FILE)

finally:
    client.close()
