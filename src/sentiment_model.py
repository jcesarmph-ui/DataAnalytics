import pandas as pd
from pathlib import Path
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# CAMINHOS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "processed"
    / "reviews_processed.csv"
)

MODEL_DIR = BASE_DIR / "data" / "models"

MODEL_FILE = MODEL_DIR / "sentiment_model.pkl"
VECTORIZER_FILE = MODEL_DIR / "tfidf_vectorizer.pkl"


# Criar pasta dos modelos
MODEL_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# CARREGAR DADOS
# ============================================================

df = pd.read_csv(INPUT_FILE)

df = df.dropna(
    subset=["comentario"]
)


# ============================================================
# CLASSIFICAÇÃO
# ============================================================

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


# ============================================================
# TF-IDF
# ============================================================

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(
    df["comentario"]
)

y = df["sentimento"]


# ============================================================
# TREINAMENTO E TESTE
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


# ============================================================
# MODELO
# ============================================================

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)


# ============================================================
# PREVISÃO
# ============================================================

y_pred = model.predict(
    X_test
)


# ============================================================
# AVALIAÇÃO
# ============================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nAcurácia:", round(accuracy, 4))

print("\nRelatório de classificação:")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# ============================================================
# SALVAR MODELO
# ============================================================

joblib.dump(
    model,
    MODEL_FILE
)

joblib.dump(
    vectorizer,
    VECTORIZER_FILE
)


print("\nModelo salvo em:")
print(MODEL_FILE)

print("\nVetorizador salvo em:")
print(VECTORIZER_FILE)