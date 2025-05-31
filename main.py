import requests
import json
import os
from dotenv import load_dotenv
#import dotenv

# Carrega variáveis do .env
load_dotenv()

# Agora você pode acessar a chave
key = os.getenv("API_KEY")

# paramâmetros  
location = "Boston"


#url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/[location]/[date1]/[date2]?key=YOUR_API_KEY"
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/[location]?key={key}"


try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Tudo certo!!")
    else:
        print("Error: ", response.status_code)
        print(response.content)

except requests.exceptions.RequestException as e:
    print("Error: ", e)