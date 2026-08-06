# Robô Buscador de Vagas

Aplicação desenvolvida em Python para automatizar a busca de vagas de Tecnologia da Informação utilizando a API pública da Gupy. O robô permite pesquisar oportunidades por área de atuação, estado e cidade, realizando automaticamente a consulta, filtragem, organização e exibição dos resultados.

O projeto foi desenvolvido com foco na aplicação prática de conceitos de automação de processos (RPA), consumo de APIs REST e processamento de dados, simulando um fluxo de automação semelhante ao encontrado em aplicações corporativas.

---

## Objetivo

O principal objetivo deste projeto é automatizar uma tarefa repetitiva: pesquisar vagas de emprego de acordo com critérios específicos.

Durante o desenvolvimento foram aplicados conceitos importantes como:

- Consumo de APIs REST
- Automação de processos (RPA)
- Manipulação de dados JSON
- Filtragem e processamento de informações
- Normalização de textos
- Interface interativa para terminal
- Organização de código em Python

---

## Demonstração

Fluxo simplificado da aplicação:

```text
Usuário
   │
   ▼
Seleciona uma ou mais áreas de TI
   │
   ▼
Seleciona o estado
   │
   ▼
Seleciona a cidade
   │
   ▼
Consulta a API pública da Gupy
   │
   ▼
Recebe os resultados
   │
   ├── Remove vagas duplicadas
   ├── Filtra por localização
   ├── Detecta o nível da vaga
   │
   ▼
Exibe as vagas encontradas
```

---

# Funcionalidades

- Consulta automática à API pública da Gupy
- Busca de vagas por múltiplas áreas da Tecnologia da Informação
- Seleção simultânea de diferentes áreas
- Filtragem por estado
- Filtragem por cidade
- Autocomplete para seleção de cidades
- Remoção automática de vagas duplicadas
- Identificação automática do nível da vaga
- Normalização de textos para comparação sem diferenças de acentuação
- Exibição organizada das informações no terminal
- Link direto para a vaga original

---

# Como Funciona

1. O usuário seleciona uma ou mais áreas de atuação.
2. O sistema solicita o estado desejado.
3. A cidade é escolhida utilizando busca dinâmica com autocomplete.
4. O robô consulta a API pública da Gupy para cada área selecionada.
5. Todos os resultados são processados.
6. Registros duplicados são removidos automaticamente.
7. O nível da vaga é identificado analisando o título da oportunidade.
8. Apenas as vagas compatíveis com os filtros informados são exibidas.

---

# Arquitetura

```text
                 Usuário
                     │
                     ▼
          Interface via Terminal
                     │
                     ▼
        Entrada dos filtros de busca
                     │
                     ▼
          Consulta à API da Gupy
                     │
                     ▼
        Processamento dos resultados
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
 Normalização   Deduplicação   Classificação
 de textos       das vagas      por nível
        │            │            │
        └────────────┼────────────┘
                     ▼
           Exibição dos resultados
```

---

# Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| Python 3 | Linguagem principal |
| Requests | Consumo da API REST |
| Prompt Toolkit | Interface interativa com autocomplete |
| pyUFBr | Estados e cidades brasileiras |
| Unicodedata | Normalização de textos |
| API Pública da Gupy | Fonte das vagas |

---

# Estrutura do Projeto

```text
robo-buscador-vagas/
│
├── buscador.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Instalação

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

---

# Execução

Execute o programa.

```bash
python buscador.py
```

Durante a execução serão solicitados:

- Área de atuação
- Estado
- Cidade

Após a definição dos filtros, o robô realiza automaticamente a consulta na API e apresenta as vagas encontradas.

---

# Exemplo de Saída

```text
==================================================

Empresa:
Empresa Exemplo

Cargo:
Desenvolvedor Backend Python Pleno

Nível:
Pleno

Localização:
São Paulo/SP

Link:
https://portal.gupy.io/jobs/xxxxxxxx

==================================================
```

---

# Conceitos Aplicados

Este projeto utiliza diversos conceitos importantes do desenvolvimento de software:

- Consumo de APIs REST
- Automação de Processos (RPA)
- Manipulação de JSON
- Processamento de dados
- Filtragem de informações
- Normalização de textos
- Estruturas de dados
- Interface interativa para terminal
- Deduplicação de registros
- Organização de código

---

# Decisões de Implementação

Algumas decisões foram adotadas durante o desenvolvimento para tornar a aplicação mais robusta.

- Utilização da API pública da Gupy como fonte oficial dos dados.
- Remoção de registros duplicados utilizando o identificador único da vaga.
- Normalização de textos para evitar inconsistências causadas por acentos.
- Classificação automática do nível da vaga com base no título informado pela empresa.
- Interface totalmente baseada em terminal para reduzir dependências e facilitar a execução.

---

# Melhorias Futuras

Algumas funcionalidades que podem ser incorporadas ao projeto:

- Paginação automática para recuperar todas as vagas disponíveis.
- Exportação dos resultados para CSV.
- Exportação para Excel.
- Banco de dados SQLite para armazenamento das vagas.
- Comparação entre execuções para identificar novas oportunidades.
- Notificações por e-mail.
- Interface gráfica.
- Dashboard Web.
- Containerização utilizando Docker.
- Testes automatizados.
- Pipeline de Integração Contínua (CI/CD).

---

# Aprendizados

O desenvolvimento deste projeto proporcionou experiência prática na construção de uma automação completa utilizando Python.

Além do consumo de uma API pública, foram explorados conceitos relacionados ao processamento de dados, integração entre sistemas, automação de tarefas, tratamento de informações e desenvolvimento de aplicações orientadas à linha de comando.

O projeto também reforçou a importância da organização do código, da separação de responsabilidades e da criação de soluções reutilizáveis para automatizar tarefas repetitivas.

---

# Licença

Este projeto foi desenvolvido para fins de estudo e composição de portfólio.
