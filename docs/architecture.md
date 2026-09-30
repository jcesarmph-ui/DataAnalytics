# Arquitetura do Data Analytics

## Visão geral

A arquitetura do Data Analytics foi projetada para receber dados de diferentes fontes e processá-los de forma escalável e resiliente.

O ambiente considera dois modos principais de ingestão:

- Batch: processamento de grandes volumes de dados acumulados;
- Streaming: processamento de eventos em tempo quase real.

## Fluxo geral

```text
Fontes de dados
      │
      ├─────────────── Batch
      │                  │
      │                  ↓
      │              Ingestão
      │
      └────────────── Streaming
                         │
                         ↓
                     Ingestão
                         │
                         ↓
                  Armazenamento
                         │
                         ↓
                   Processamento
                         │
                         ↓
                  Análise e ML
                         │
                         ↓
                    Dashboard
```
## Tecnologias escolhidas

| Etapa | Tecnologia | Função |
|---|---|---|
| Ingestão Batch | Python | Coleta e preparação inicial dos dados |
| Ingestão Streaming | Apache Kafka | Recebimento de eventos em tempo quase real |
| Armazenamento | MongoDB | Armazenamento de dados semiestruturados |
| Processamento | Apache Spark | Processamento distribuído dos dados |
| Orquestração | Apache Airflow | Automação e gerenciamento dos pipelines |
| Machine Learning | Python / Scikit-learn | Modelagem e análise dos dados |
| NLP | Python | Processamento e análise dos textos |
| Dashboard | Power BI | Visualização dos indicadores |

## Justificativa

### Python

Será utilizado na coleta, preparação e análise inicial dos dados. Também servirá como base para os componentes de Machine Learning e processamento de linguagem natural.

### Apache Kafka

Será utilizado para simular a ingestão de dados em streaming, permitindo o recebimento contínuo de eventos, como novos comentários, logs e registros de atendimento.

### MongoDB

Será utilizado para armazenar dados semiestruturados, especialmente documentos provenientes de comentários, avaliações e registros de atendimento.

### Apache Spark

Será utilizado para o processamento de grandes volumes de dados, permitindo demonstrar conceitos de processamento distribuído.

### Apache Airflow

Será utilizado posteriormente para orquestrar e automatizar os pipelines de processamento.

### Scikit-learn

Será utilizado para aplicar modelos de Machine Learning sobre os dados processados.

### NLP

Será utilizado para analisar os comentários e textos recebidos pela plataforma, incluindo técnicas de tokenização, representação textual e análise semântica.

### Power BI

Será utilizado para construir dashboards com indicadores de negócio e métricas relacionadas aos dados processados.