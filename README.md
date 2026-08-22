# Robô Buscador de Vagas de TI

Robô em Python que busca vagas de TI e desenvolvimento na API pública da Gupy, com filtro interativo por área, estado e cidade, detecção automática de nível, salvamento em banco SQLite e abertura automática de vagas novas no navegador via Selenium.

Fiz esse projeto pra treinar automação com Python aplicando conceitos de RPA — consumir uma API real, processar e filtrar dados automaticamente, e estruturar um robô que executa um processo completo do início ao fim sem intervenção manual.

## Como Rodar

```bash
git clone https://github.com/brunofaomoura-max/robo-buscador-vagas.git
cd robo-buscador-vagas
pip install -r requirements.txt
python buscador.py
```

O robô vai fazer perguntas interativas no terminal: qual área de TI buscar, em qual estado e cidade. A busca é feita diretamente na API da Gupy e os resultados aparecem no terminal com empresa, localização, nível e link direto da vaga. Vagas novas são salvas no banco e abertas automaticamente no Chrome.

## O que ele faz

1. Exibe um menu com 11 áreas de TI para o usuário escolher (pode combinar várias)
2. Pergunta o estado usando a lista oficial de UFs brasileiras
3. Pergunta a cidade com busca dinâmica — é só digitar as primeiras letras e as opções aparecem automaticamente
4. Busca as vagas direto na API pública da Gupy usando as palavras-chave de cada área
5. Percorre todas as páginas de resultados automaticamente via paginação
6. Filtra os resultados por estado e cidade
7. Remove vagas duplicadas automaticamente pelo ID
8. Detecta o nível da vaga pelo título (Estágio, Junior, Pleno, Sênior)
9. Salva todas as vagas encontradas no banco SQLite
10. Detecta quais vagas são novas em relação às execuções anteriores
11. Exibe os resultados com empresa, localização, nível e link direto
12. Pergunta se deseja abrir as vagas novas automaticamente no Chrome via Selenium

## Tecnologias

| Tecnologia | Finalidade |
|---|---|
| Python 3 | Linguagem principal |
| Requests | Requisições HTTP para a API REST da Gupy |
| Prompt Toolkit | Interface interativa com autocomplete no terminal |
| pyUFBr | Lista oficial de estados e cidades brasileiras |
| Unicodedata | Normalização de textos para filtros sem diferença de acentuação |
| SQLite3 | Banco local para salvar vagas e detectar novidades |
| Selenium | Abre vagas novas automaticamente no Chrome |
| WebDriver Manager | Gerencia a instalação do ChromeDriver automaticamente |
| Flask | API REST para integração com dashboards externos |
| API Pública da Gupy | Fonte dos dados de vagas |

## Estrutura do Projeto
robo-buscador-vagas/
## Estrutura do Projeto

```
robo-buscador-vagas/
│
├── buscador.py          # Robô principal — busca, filtra e exibe
├── database.py          # Lógica SQLite — salva e detecta vagas novas
├── selenium_opener.py   # Abre vagas novas no Chrome automaticamente
├── api.py               # API Flask para consumo externo dos dados
├── requirements.txt     # Dependências do projeto
├── .gitignore
└── README.md
```

## Instalação

Clone o repositório.

```bash
git clone https://github.com/brunofaomoura-max/robo-buscador-vagas.git
```

Entre na pasta do projeto.

```bash
cd robo-buscador-vagas
```

Instale as dependências.

```bash
pip install -r requirements.txt
```

## Execução

Execute o programa.

```bash
python buscador.py
```

Durante a execução serão solicitados:

- Área(s) de TI desejada(s)
- Estado
- Cidade

Após definir os filtros, o robô consulta a API, percorre todas as páginas disponíveis, salva as vagas novas no banco e pergunta se deseja abri-las no Chrome.

## Exemplo de Saída
ROBO BUSCADOR DE VAGAS DE TI

Que area voce quer buscar?

RPA / Automacao
Dev Fullstack
...
Todas as areas
========================================
Digite os numeros separados por virgula: 1

Qual estado voce quer buscar?
18. PR - Paraná
...
Digite o numero do estado: 18

Digite o nome da cidade em Paraná:
(va digitando que as opcoes aparecem, ENTER para todas)
Cidade: Curitiba

Buscando vagas de: RPA / Automacao
Estado: Paraná
Cidade: Curitiba
Aguarde...

Vagas encontradas: 1

[NOVA] [10582233] Estágio em Automação
Empresa: Centro de Excelência Votorantim
Local: Curitiba/Paraná
Nivel: Estagio
Link: https://votorantimcoe.gupy.io/...

Novas: 1 | Ja vistas: 0

Deseja abrir as 1 vaga(s) nova(s) no navegador? (s/n): s
Abrindo 1 vaga(s) no navegador...
Pressione ENTER quando terminar de ver as vagas...

## Conceitos Aplicados

- Consumo de APIs REST com paginação automática
- Automação de Processos (RPA)
- Manipulação de dados JSON
- Filtragem e processamento de informações
- Normalização de textos
- Tratamento de erros com try/except
- Gerenciamento de banco de dados local com SQLite
- Detecção de registros duplicados
- Interface interativa no terminal com autocomplete
- Automação de navegador com Selenium

## Possíveis Melhorias Futuras

- [ ] Exportação para CSV e Excel
- [ ] Alerta de novas vagas por e-mail
- [ ] Dashboard web para visualizar vagas salvas
- [ ] Containerização com Docker
- [ ] Testes automatizados
- [ ] Pipeline de CI/CD

## Autor

Bruno — estudante de tecnologia em transição para automação e RPA.
Portfólio: [github.com/brunofaomoura-max](https://github.com/brunofaomoura-max)
