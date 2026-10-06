import json
from kafka import KafkaProducer


# ============================================================
# PRODUCER KAFKA
# ============================================================

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(
        value,
        ensure_ascii=False
    ).encode("utf-8")
)


# ============================================================
# EVENTOS DE TESTE
# ============================================================

eventos = [
    {
        "id": 1,
        "categoria": "produto",
        "avaliacao": 5,
        "comentario": "Produto excelente e chegou rapidamente"
    },
    {
        "id": 2,
        "categoria": "produto",
        "avaliacao": 1,
        "comentario": "Produto chegou quebrado e muito atrasado"
    },
    {
        "id": 3,
        "categoria": "produto",
        "avaliacao": 3,
        "comentario": "O produto é razoável, nada demais"
    },
    {
        "id": 4,
        "categoria": "atendimento",
        "avaliacao": 5,
        "comentario": "Atendimento muito bom e equipe muito prestativa"
    },
    {
        "id": 5,
        "categoria": "atendimento",
        "avaliacao": 1,
        "comentario": "Péssimo atendimento e demoraram para responder"
    },
    {
        "id": 6,
        "categoria": "entrega",
        "avaliacao": 4,
        "comentario": "A entrega foi rápida e o produto chegou bem"
    },
    {
        "id": 7,
        "categoria": "entrega",
        "avaliacao": 2,
        "comentario": "A entrega demorou muito e a embalagem estava ruim"
    },
    {
        "id": 8,
        "categoria": "produto",
        "avaliacao": 4,
        "comentario": "Gostei bastante do produto e recomendo"
    },
    {
        "id": 9,
        "categoria": "produto",
        "avaliacao": 2,
        "comentario": "Não gostei da qualidade do produto"
    },
    {
        "id": 10,
        "categoria": "atendimento",
        "avaliacao": 3,
        "comentario": "Atendimento normal, poderia ser melhor"
    }
]


# ============================================================
# ENVIAR EVENTOS
# ============================================================

for evento in eventos:

    producer.send(
        "reviews",
        evento
    )

    print("Evento enviado para o Kafka!")
    print(evento)
    print("-" * 50)


# ============================================================
# GARANTIR ENVIO
# ============================================================

producer.flush()

producer.close()