import json
from pathlib import Path

import joblib
from kafka import KafkaConsumer
from pymongo import MongoClient


# ============================================================
# CAMINHOS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_FILE = (
    BASE_DIR
    / "data"
    / "models"
    / "sentiment_model.pkl"
)

VECTORIZER_FILE = (
    BASE_DIR
    / "data"
    / "models"
    / "tfidf_vectorizer.pkl"
)


# ============================================================
# CARREGAR MODELO
# ============================================================

print("Carregando modelo de sentimento...")

model = joblib.load(MODEL_FILE)

vectorizer = joblib.load(
    VECTORIZER_FILE
)

print("Modelo carregado com sucesso.")
print()


# ============================================================
# CONEXÃO COM MONGODB
# ============================================================

print("Conectando ao MongoDB...")

mongo_client = MongoClient(
    "mongodb://localhost:27017/"
)

database = mongo_client["data_analytics"]

collection = database["reviews_processed"]

print("MongoDB conectado com sucesso.")
print()


# ============================================================
# CONSUMER KAFKA
# ============================================================

consumer = KafkaConsumer(
    "reviews",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="data-analytics-consumer-ml",
    value_deserializer=lambda value: json.loads(
        value.decode("utf-8")
    )
)


# ============================================================
# AGUARDAR EVENTOS
# ============================================================

print("Consumer iniciado.")
print("Aguardando novos eventos...\n")


for mensagem in consumer:

    evento = mensagem.value

    comentario = evento["comentario"]


    # ========================================================
    # TRANSFORMAR COMENTÁRIO EM TF-IDF
    # ========================================================

    comentario_tfidf = vectorizer.transform(
        [comentario]
    )


    # ========================================================
    # PREVER SENTIMENTO
    # ========================================================

    sentimento = model.predict(
        comentario_tfidf
    )[0]


    # ========================================================
    # CRIAR DOCUMENTO PARA O MONGODB
    # ========================================================

    documento = {
        "id": evento["id"],
        "categoria": evento["categoria"],
        "avaliacao": evento["avaliacao"],
        "comentario": evento["comentario"],
        "sentimento": sentimento
    }


    # ========================================================
    # SALVAR NO MONGODB
    # ========================================================

    collection.insert_one(documento)


    # ========================================================
    # EXIBIR RESULTADO
    # ========================================================

    print("Novo evento recebido:")
    print(f"ID: {evento['id']}")
    print(f"Categoria: {evento['categoria']}")
    print(f"Avaliação: {evento['avaliacao']}")
    print(f"Comentário: {evento['comentario']}")
    print(f"Sentimento previsto: {sentimento}")
    print("Salvo no MongoDB!")
    print("-" * 50)