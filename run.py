import requests
import json

url = "https://rickandmortyapi.com/api/episode"

response = requests.get(url)

if response.status_code == 200:
    formatted_response = json.dumps(response.json(), indent=4, sort_keys=True)
    print("Sucesso:")
    print(formatted_response)
else:
    print("Erro:", response.status_code)
