import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer


# Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_nlp.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_tfidf.csv"


# Carregar dados
df = pd.read_csv(INPUT_FILE)


# Criar o modelo TF-IDF
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words=None
)


# Transformar os comentários em valores numéricos
tfidf_matrix = vectorizer.fit_transform(
    df["comentario"]
)


# Criar DataFrame com os valores TF-IDF
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=vectorizer.get_feature_names_out()
)


# Adicionar ID do comentário
tfidf_df.insert(
    0,
    "id",
    df["id"].values
)


# Salvar resultado
tfidf_df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"S
)


print("TF-IDF concluído!")
print(f"Documentos processados: {len(df)}")
print(f"Termos identificados: {len(vectorizer.get_feature_names_out())}")
print(f"Arquivo gerado: {OUTPUT_FILE}")
