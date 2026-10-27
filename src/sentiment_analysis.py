import pandas as pd
from pathlib import Path


# Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_processed.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "sentiment_analysis.csv"


# Carregar dados
df = pd.read_csv(INPUT_FILE)


# Classificar sentimento pela avaliação
def classificar_sentimento(avaliacao):

    if avaliacao <= 2:
        return "negativo"

    elif avaliacao == 3:
        return "neutro"

    else:
        return "positivo"


df["sentimento"] = df["avaliacao"].apply(
    classificar_sentimento
)


# Contagem dos sentimentos
resultado = (
    df["sentimento"]
    .value_counts()
    .reset_index()
)

resultado.columns = [
    "sentimento",
    "quantidade"
]


# Salvar resultado
resultado.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)


print("\nAnálise de sentimento:")
print(resultado)

print("\nArquivo gerado:")
print(OUTPUT_FILE)