import pandas as pd
from pathlib import Path


# Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_tfidf.csv"


# Carregar os dados
df = pd.read_csv(INPUT_FILE)


# Remover o ID para analisar apenas os termos
tfidf_data = df.drop(columns=["id"])


# Calcular a média do TF-IDF de cada termo
mean_tfidf = tfidf_data.mean().sort_values(ascending=False)


# Mostrar os 10 termos mais relevantes
print("\n10 termos com maior relevância média:\n")

for termo, valor in mean_tfidf.head(10).items():
    print(f"{termo}: {valor:.4f}")