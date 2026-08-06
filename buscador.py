import requests
import unicodedata
from pyUFbr.baseuf import ufbr

AREAS = {
    "1": {
        "nome": "RPA / Automacao",
        "palavras_chave": ["rpa", "automacao", "automação", "hiperautomacao", "hiperautomação", "uipath", "automation anywhere", "blue prism", "power automate", "robot framework"]
    },
    "2": {
        "nome": "Dev Fullstack",
        "palavras_chave": ["fullstack", "full stack", "full-stack"]
    },
    "3": {
        "nome": "Dev Frontend",
        "palavras_chave": ["frontend", "front-end", "front end"]
    },
    "4": {
        "nome": "Dev Backend",
        "palavras_chave": ["backend", "back-end", "back end"]
    },
    "5": {
        "nome": "Cybersecurity",
        "palavras_chave": ["cybersecurity", "seguranca da informacao", "segurança da informação", "pentest", "soc analista"]
    },
    "6": {
        "nome": "Dados / BI / Analytics",
        "palavras_chave": ["analista de dados", "engenheiro de dados", "cientista de dados", "business intelligence", "analytics"]
    },
    "7": {
        "nome": "DevOps / Cloud",
        "palavras_chave": ["devops", "cloud engineer", "sre", "platform engineer"]
    },
    "8": {
        "nome": "Mobile",
        "palavras_chave": ["mobile", "desenvolvedor android", "desenvolvedor ios", "flutter"]
    },
    "9": {
        "nome": "QA / Testes",
        "palavras_chave": ["quality assurance", "qa engineer", "analista de testes", "testes automatizados"]
    },
    "10": {
        "nome": "Redes / Infraestrutura",
        "palavras_chave": ["redes", "infraestrutura ti", "network engineer", "administrador de redes"]
    },
    "11": {
        "nome": "IA / Machine Learning",
        "palavras_chave": ["machine learning", "inteligencia artificial", "inteligência artificial", "nlp", "deep learning", "llm"]
    }
}

NIVEIS_DISPLAY = {
    "estagio": "Estagio",
    "estágio": "Estagio",
    "estagiario": "Estagio",
    "estagiário": "Estagio",
    "junior": "Junior",
    "júnior": "Junior",
    "jr": "Junior",
    "pleno": "Pleno",
    "senior": "Senior",
    "sênior": "Senior",
    "sr": "Senior",
    "analista": "Analista",
    "desenvolvedor": "Desenvolvedor",
    "engenheiro": "Engenheiro",
    "cientista": "Cientista",
    "consultor": "Consultor",
    "arquiteto": "Arquiteto",
    "pesquisador": "Pesquisador",
    "administrador": "Administrador"
}

SIGLA_PARA_NOME = {
    "AC": "Acre", "AL": "Alagoas", "AM": "Amazonas", "AP": "Amapá",
    "BA": "Bahia", "CE": "Ceará", "DF": "Distrito Federal", "ES": "Espírito Santo",
    "GO": "Goiás", "MA": "Maranhão", "MG": "Minas Gerais", "MS": "Mato Grosso do Sul",
    "MT": "Mato Grosso", "PA": "Pará", "PB": "Paraíba", "PE": "Pernambuco",
    "PI": "Piauí", "PR": "Paraná", "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte",
    "RO": "Rondônia", "RR": "Roraima", "RS": "Rio Grande do Sul", "SC": "Santa Catarina",
    "SE": "Sergipe", "SP": "São Paulo", "TO": "Tocantins"
}

def normalizar(texto):
    return unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode("ascii").lower()

def exibir_menu_areas():
    print("\nROBO BUSCADOR DE VAGAS DE TI")
    print("=" * 40)
    print("Que area voce quer buscar?\n")
    for numero, area in AREAS.items():
        print(f"  {numero}. {area['nome']}")
    print("\n  0. Todas as areas")
    print("=" * 40)
    escolha = input("Digite os numeros separados por virgula (ex: 1, 2, 5): ")
    return escolha

def exibir_menu_estados():
    print("\nQual estado voce quer buscar?\n")
    lista_uf = ufbr.list_uf
    for i, sigla in enumerate(lista_uf, start=1):
        nome = SIGLA_PARA_NOME.get(sigla, sigla)
        print(f"  {i}. {sigla} - {nome}")
    print("\n  0. Todos os estados")
    print("=" * 40)
    escolha = input("Digite o numero do estado: ").strip()
    return escolha, lista_uf

def exibir_menu_cidades(sigla_estado):
    print(f"\nQual cidade em {SIGLA_PARA_NOME.get(sigla_estado, sigla_estado)}?\n")
    cidades = ufbr.list_cidades(sigla_estado)
    for i, cidade in enumerate(cidades, start=1):
        print(f"  {i}. {cidade.title()}")
    print("\n  0. Todas as cidades")
    print("=" * 40)
    escolha = input("Digite o numero da cidade: ").strip()
    return escolha, cidades

def processar_areas(escolha):
    if escolha.strip() == "0":
        palavras = []
        for area in AREAS.values():
            palavras.extend(area["palavras_chave"])
        return palavras, "Todas as areas"

    numeros = [n.strip() for n in escolha.split(",")]
    palavras = []
    nomes = []

    for numero in numeros:
        if numero in AREAS:
            palavras.extend(AREAS[numero]["palavras_chave"])
            nomes.append(AREAS[numero]["nome"])
        else:
            print(f"Opcao '{numero}' invalida, ignorada.")

    return palavras, ", ".join(nomes)

def buscar_por_palavra(palavra_chave, estado_filtro=None, cidade_filtro=None, limit=50):
    url = "https://employability-portal.gupy.io/api/v1/jobs"
    params = {
        "jobName": palavra_chave,
        "limit": limit,
        "offset": 0
    }
    resposta = requests.get(url, params=params)
    dados = resposta.json()
    vagas = dados.get("data", [])

    if estado_filtro:
        vagas = [v for v in vagas if normalizar(estado_filtro) in normalizar(v.get("state", ""))]

    if cidade_filtro:
        vagas = [v for v in vagas if normalizar(cidade_filtro) in normalizar(v.get("city", ""))]

    return vagas

def extrair_campos(vaga):
    return {
        "id": vaga["id"],
        "titulo": vaga["name"],
        "empresa": vaga["careerPageName"],
        "cidade": vaga.get("city", ""),
        "estado": vaga.get("state", ""),
        "url": vaga["jobUrl"],
        "tipo": vaga["type"],
        "data_publicacao": vaga["publishedDate"],
        "descricao": vaga["description"]
    }

def detectar_nivel(titulo):
    titulo = titulo.lower()
    for chave, display in NIVEIS_DISPLAY.items():
        if chave in titulo:
            return display
    return "Nao identificado"

# -- Execucao principal --
escolha_area = exibir_menu_areas()
palavras_chave, areas_escolhidas = processar_areas(escolha_area)

escolha_estado, lista_uf = exibir_menu_estados()

estado_filtro = None
cidade_filtro = None
estado_nome = "Todos os estados"
cidade_nome = "Todas as cidades"

if escolha_estado != "0" and escolha_estado != "":
    idx = int(escolha_estado) - 1
    if 0 <= idx < len(lista_uf):
        sigla = lista_uf[idx]
        estado_filtro = SIGLA_PARA_NOME.get(sigla, sigla)
        estado_nome = estado_filtro

        escolha_cidade, lista_cidades = exibir_menu_cidades(sigla)

        if escolha_cidade != "0" and escolha_cidade != "":
            idx_cidade = int(escolha_cidade) - 1
            if 0 <= idx_cidade < len(lista_cidades):
                cidade_filtro = lista_cidades[idx_cidade].title()
                cidade_nome = cidade_filtro

print(f"\nBuscando vagas de: {areas_escolhidas}")
print(f"Estado: {estado_nome}")
print(f"Cidade: {cidade_nome}")
print("Aguarde...\n")

vagas_encontradas = {}

for palavra in palavras_chave:
    vagas = buscar_por_palavra(palavra, estado_filtro, cidade_filtro)
    for vaga in vagas:
        if vaga["id"] not in vagas_encontradas:
            vagas_encontradas[vaga["id"]] = extrair_campos(vaga)

resultado = list(vagas_encontradas.values())

print(f"Vagas encontradas: {len(resultado)}")
print("-" * 40)

for v in resultado:
    nivel = detectar_nivel(v["titulo"])
    print(f"[{v['id']}] {v['titulo']}")
    print(f"    Empresa: {v['empresa']}")
    print(f"    Local:   {v['cidade']}/{v['estado']}")
    print(f"    Nivel:   {nivel}")
    print(f"    Link:    {v['url']}")
    print()