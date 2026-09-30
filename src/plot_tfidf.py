import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_tfidf.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"


# Carregar dados
df = pd.read_csv(INPUT_FILE)

# Remover ID
tfidf_data = df.drop(columns=["id"])

# Calcular média do TF-IDF
mean_tfidf = (
    tfidf_data
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# Criar gráfico
plt.figure(figsize=(10, 6))

mean_tfidf.sort_values().plot(
    kind="barh"
)

plt.title("10 termos com maior relevância média - TF-IDF")
plt.xlabel("TF-IDF médio")
plt.ylabel("Termo")

plt.tight_layout()


# Salvar gráfico
OUTPUT_FILE = OUTPUT_DIR / "tfidf_top_terms.png"

plt.savefig(
    OUTPUT_FILE,
    dpi=300
)

plt.show()

print("Gráfico criado com sucesso!")
print(f"Arquivo: {OUTPUT_FILE}")