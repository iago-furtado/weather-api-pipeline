import requests
import json
import os
from os.path import join
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pandas as pd


def extract_from_api():
    # Carrega variáveis do .env
    load_dotenv()

    # Agora você pode acessar a chave
    key = os.getenv("API_KEY")

    # paramâmetros  


    # intervalo de datas
    data_inicio = datetime.today()
    data_fim = data_inicio + timedelta(days=7)

    # parâmetros
    data_inicio = data_inicio.strftime('%Y-%m-%d')
    data_fim = data_fim.strftime('%Y-%m-%d')
    location = 'Boston'


    # url test
    #url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/[location]?key={key}",
    url = join("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/",
            f"{location}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}")


    try:
        response = requests.get(url)

        if response.status_code == 200:
            #print("Tudo certo!!")
            data = response.json()
            
            # criando dataframe
            df = pd.DataFrame(data['days'])


            # caminho da pasta
            file_path_raw = f'/home/iago/Documents/api_weather/data/raw/{data_inicio}'
            file_path = f'/home/iago/Documents/api_weather/data/{data_inicio}'
            if not os.path.exists(file_path):
                os.mkdir(file_path)

            # passando os dados para csv
            # dados brutos
            df.to_csv(file_path_raw + '_dados_brutos.csv', index=False)
            #limpos
            df[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + '/temperatura.csv', index=False)
            df[['datetime', 'description', 'icon']].to_csv(file_path + '/condicoes.csv', index=False)



        else:
            print("Error: ", response.status_code)
            print(response.content)

    except Exception as e:
        print("Error: ", e)

