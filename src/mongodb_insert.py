import pandas as pd
from pymongo import MongoClient
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_processed.csv"

# Conexão com o MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Banco e coleção
db = client["data_analytics"]
collection = db["reviews"]

# Ler CSV
df = pd.read_csv(INPUT_FILE)

# Converter registros para documentos
documents = df.to_dict(orient="records")

# Inserir no MongoDB
collection.insert_many(documents)

print("Dados inseridos com sucesso!")
print(f"Registros inseridos: {len(documents)}")