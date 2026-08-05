import requests

def buscar_vagas():
    resposta = requests.get("https://employability-portal.gupy.io/api/v1/jobs")
    dados = resposta.json()
    return dados

resultado = buscar_vagas()
print(resultado)