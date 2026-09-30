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