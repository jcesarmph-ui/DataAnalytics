import pandas as pd
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# Caminhos
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "reviews_processed.csv"


# Carregar dados
df = pd.read_csv(INPUT_FILE)


# Remover registros sem comentário
df = df.dropna(subset=["comentario"])


# Criar variável alvo
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


# Transformar textos em números
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["comentario"])
y = df["sentimento"]


# Separar treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


# Criar modelo
model = LogisticRegression(
    max_iter=1000
)


# Treinar
model.fit(X_train, y_train)


# Fazer previsões
y_pred = model.predict(X_test)


# Avaliar
accuracy = accuracy_score(y_test, y_pred)

print("\nAcurácia:", round(accuracy, 4))

print("\nRelatório de classificação:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)