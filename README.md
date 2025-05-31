# Projeto: API Weather - Coleta e Armazenamento de Dados Meteorológicos

Este projeto realiza a extração de dados meteorológicos utilizando a [API da Visual Crossing](https://www.visualcrossing.com/weather-api), convertendo as informações em arquivos CSV e organizando os dados em uma estrutura de diretórios limpa, ideal para pipelines de dados.

## 🔗 Objetivo

O objetivo é consumir uma API de previsão do tempo e salvar os dados brutos e tratados em arquivos `.csv`, separados por data, de forma organizada para futuras etapas do processo de engenharia de dados (como transformação e carga).

## 🌐 Tecnologias Utilizadas

* Python 3.10+
* [requests](https://docs.python-requests.org/en/latest/)
* [pandas](https://pandas.pydata.org/)
* [python-dotenv](https://saurabh-kumar.com/python-dotenv/)
* API: Visual Crossing Weather

## ⚖️ Funcionalidades

* Extração de previsão do tempo para os próximos 7 dias de uma cidade.
* Conversão dos dados JSON em DataFrame.
* Salvamento dos dados brutos e filtrados em arquivos CSV.
* Organização dos arquivos em pastas por data da consulta.

## 📂 Estrutura de Pastas

```bash
api_weather/
├── data/
│   ├── raw/
│   │   └── 2025-05-31_dados_brutos.csv
│   └── 2025-05-31/
│       ├── temperatura.csv
│       └── condicoes.csv
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── venv/
```

## 📅 Agendamento

Este script pode ser facilmente agendado com ferramentas como `cron`, `Task Scheduler` ou orquestradores como Airflow e Prefect.

## 📁 Exemplos de Saída

* **dados\_brutos.csv**: todas as colunas retornadas pela API.
* **temperatura.csv**: colunas `datetime`, `tempmin`, `temp`, `tempmax`.
* **condicoes.csv**: colunas `datetime`, `description`, `icon`.

## ✅ Como executar

1. Clone o repositório
2. Crie um `.env` com sua chave da API:

   ```env
   API_KEY=sua_chave_aqui
   ```
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```
4. Execute:

   ```bash
   python main.py
   ```

## 🚀 Possíveis melhorias

* Validação de inputs via linha de comando (ex: cidade)
* Integração com banco de dados
* Pipeline de ETL completo
* Monitoramento com logs

---

