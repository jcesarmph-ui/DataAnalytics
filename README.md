# \# Data Analytics — Pipeline de Big Data

# 

# Projeto prático de Engenharia de Dados desenvolvido para aplicar conceitos de \*\*Big Data, processamento de dados em tempo real, Machine Learning, ETL, orquestração de pipelines e Business Intelligence\*\*.

# 

# O projeto simula o processamento de avaliações de clientes, desde a ingestão de dados até a geração de indicadores para análise no Power BI.

# 

# \## Objetivo

# 

# Construir um pipeline de dados integrado capaz de coletar, processar, classificar, armazenar e transformar avaliações de clientes, disponibilizando os resultados para análise e visualização.

# 

# \## Arquitetura do projeto

# 

# ```text

# Dados de avaliações

# &#x20;       |

# &#x20;       v

# Kafka Producer

# &#x20;       |

# &#x20;       v

# Apache Kafka

# &#x20;       |

# &#x20;       v

# Kafka Consumer

# &#x20;       |

# &#x20;       v

# NLP + Machine Learning

# &#x20;       |

# &#x20;       v

# MongoDB

# &#x20;       |

# &#x20;       v

# Python ETL

# &#x20;       |

# &#x20;       v

# CSV analítico

# &#x20;       |

# &#x20;       v

# Power BI

# ```

# 

# O Apache Airflow é utilizado para orquestrar a execução do ETL e automatizar sua programação.

# 

# \## Tecnologias utilizadas

# 

# | Tecnologia | Aplicação |

# |---|---|

# | Python | Processamento e transformação de dados |

# | Apache Kafka | Ingestão e comunicação de dados por eventos |

# | Machine Learning | Classificação de sentimentos |

# | NLP e TF-IDF | Representação e processamento de textos |

# | Logistic Regression | Modelo de classificação |

# | MongoDB | Armazenamento dos dados processados |

# | Pandas | Manipulação e preparação dos dados |

# | Apache Airflow | Orquestração e agendamento do ETL |

# | Docker | Execução do ambiente do Airflow |

# | Power BI | Visualização de indicadores e criação de dashboards |

# | Git e GitHub | Versionamento, documentação e portfólio |

# 

# \## Fluxo de processamento

# 

# 1\. \*\*Ingestão:\*\* o produtor envia avaliações para o Apache Kafka.

# 2\. \*\*Processamento:\*\* o consumidor recebe os eventos e utiliza o modelo de Machine Learning para classificar os sentimentos.

# 3\. \*\*Armazenamento:\*\* os registros processados são persistidos no MongoDB.

# 4\. \*\*ETL:\*\* um script Python consulta o banco, trata os dados e gera o arquivo `data/processed/reviews\_analytics.csv`.

# 5\. \*\*Orquestração:\*\* o Apache Airflow executa e agenda o processo de ETL.

# 6\. \*\*Visualização:\*\* o Power BI utiliza os dados analíticos para apresentar indicadores e gráficos.

# 

# \## Dashboard

# 

# O dashboard `DataAnalytics\_Dashboard.pbix` apresenta indicadores como:

# 

# \- Total de avaliações.

# \- Nota média dos clientes.

# \- Percentuais de sentimentos positivos, negativos e neutros.

# \- Distribuição de sentimentos.

# \- Quantidade de avaliações por categoria.

# \- Nota média por categoria.

# \- Filtros por categoria, sentimento e avaliação.

# 

# \## Estrutura do repositório

# 

# ```text

# DataAnalytics/

# ├── airflow/

# │   ├── dags/

# │   │   ├── primeira\_dag.py

# │   │   └── etl\_reviews\_dag.py

# │   ├── Dockerfile

# │   ├── docker-compose.yaml

# │   └── requirements.txt

# ├── data/

# │   ├── models/

# │   └── processed/

# ├── docs/

# │   ├── architecture.md

# │   └── project\_overview.md

# ├── notebooks/

# ├── src/

# │   ├── kafka\_producer.py

# │   ├── kafka\_consumer.py

# │   ├── sentiment\_analysis.py

# │   ├── sentiment\_model.py

# │   └── mongo\_to\_csv.py

# ├── .gitignore

# ├── DataAnalytics\_Dashboard.pbix

# └── README.md

# ```

# 

# Os diretórios de dados podem conter arquivos gerados durante a execução. Modelos treinados e dados locais não precisam ser versionados no GitHub.

# 

# \## Como executar o ETL com Airflow

# 

# \### Pré-requisitos

# 

# \- Docker Desktop com suporte ao Docker Compose.

# \- MongoDB em execução e acessível pelo ambiente do Airflow.

# \- Python e dependências do projeto para executar os componentes fora do Docker.

# 

# \### Iniciar o Airflow

# 

# No terminal, entre na pasta `airflow` e execute:

# 

# ```powershell

# docker compose up -d

# ```

# 

# Acesse a interface web:

# 

# http://localhost:8080

# 

# A DAG `etl\_reviews\_mongodb\_csv` executa o script `src/mongo\_to\_csv.py`, que consulta a coleção `reviews\_processed` do banco `data\_analytics` e gera o CSV analítico.

# 

# Para parar o ambiente:

# 

# ```powershell

# docker compose down

# ```

# 

# A configuração atual agenda o ETL diariamente às 08h, horário de Brasília, considerando o Airflow configurado em UTC. O computador, o Docker, o Airflow e o MongoDB precisam estar disponíveis no horário programado.

# 

# \## Limitações e próximos passos

# 

# O projeto permanece em desenvolvimento. Entre as melhorias previstas estão:

# 

# \- Melhorar e avaliar a qualidade do classificador de sentimentos.

# \- Expandir o conjunto de dados e criar testes automatizados.

# \- Implementar monitoramento e tratamento de falhas no pipeline.

# \- Evoluir a automação e a atualização do dashboard.

# \- Documentar a governança e os cuidados com dados pessoais, incluindo LGPD.

# \- Aprimorar a reprodutibilidade do ambiente e as instruções de instalação.

# 

# Os resultados do modelo dependem dos dados utilizados no treinamento e devem ser avaliados antes de aplicações reais.

# 

# \## Documentação complementar

# 

# \- \[Visão geral do projeto](docs/project\_overview.md)

# \- \[Arquitetura técnica](docs/architecture.md)

# 

# \## Autor

# 

# Projeto desenvolvido como parte de um portfólio prático de Engenharia de Dados, Big Data, Machine Learning e Analytics.

# 

# Repositório: \[DataAnalytics — GitHub](https://github.com/jcesarmph-ui/DataAnalytics)



