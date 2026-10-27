import pandas as pd
from pathlib import Path


# Caminhos dos arquivos
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw" / "reviews.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_processed.csv"


# Carregar os dados
df = pd.read_csv(INPUT_FILE)


# Limpeza dos dados
df = df.drop_duplicates()

df["comentario"] = df["comentario"].fillna("").str.strip()

df["categoria"] = df["categoria"].fillna("não informado")

df["avaliacao"] = pd.to_numeric(
    df["avaliacao"],
    errors="coerce"
)


# Remover registros sem avaliação
df = df.dropna(subset=["avaliacao"])


# Criar classificação simples da avaliação
def classificar_avaliacao(avaliacao):
    if avaliacao >= 4:
        return "positivo"
    elif avaliacao == 3:
        return "neutro"
    else:
        return "negativo"


df["sentimento_inicial"] = df["avaliacao"].apply(
    classificar_avaliacao
)


# Salvar os dados processados
df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)


print("Processamento concluído!")
print(f"Registros processados: {len(df)}")
print(f"Arquivo gerado: {OUTPUT_FILE}")