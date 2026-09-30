import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from pathlib import Path


# Download do tokenizador
nltk.download("punkt")
nltk.download("punkt_tab")


# Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_processed.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_nlp.csv"


# Carregar dados processados
df = pd.read_csv(INPUT_FILE)


# Tokenização
df["tokens"] = df["comentario"].apply(
    lambda texto: word_tokenize(texto, language="portuguese")
)


# Quantidade de palavras por comentário
df["quantidade_tokens"] = df["tokens"].apply(len)


# Salvar resultado
df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)


print("Processamento NLP concluído!")
print(f"Comentários processados: {len(df)}")
print(f"Arquivo gerado: {OUTPUT_FILE}")