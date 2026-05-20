# Pipeline ETL com Python para Ciência de Dados

Projeto prático desenvolvido para demonstrar um fluxo completo de ETL usando Python, com foco em extração, transformação e carregamento de dados.

O objetivo é simular um cenário real em que dados de usuários são extraídos de um arquivo CSV, transformados em mensagens personalizadas e carregados em um novo arquivo estruturado.

## Visão Geral

Este projeto segue o fluxo clássico de ETL:

| Etapa | Descrição |
|---|---|
| Extract | Leitura dos dados de entrada a partir de um arquivo CSV |
| Transform | Tratamento dos dados e geração de mensagens personalizadas |
| Load | Salvamento dos dados transformados em um novo arquivo CSV |

## Tecnologias Utilizadas

- Python 3
- Pandas
- CSV
- Git e GitHub

## Estrutura do Projeto

```text
etl-python-portfolio/
│
├── data/
│   ├── usuarios.csv
│   └── usuarios_transformados.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Dados de Entrada

Arquivo: `data/usuarios.csv`

```csv
id,nome,conta,cartao,segmento
1,Rafael,12345-6,Gold,Tecnologia
2,Mariana,78945-1,Platinum,Empreendedora
3,João,45678-9,Black,Investidor
```

## Exemplo de Saída

Arquivo gerado: `data/usuarios_transformados.csv`

```csv
id,nome,conta,cartao,segmento,mensagem
1,Rafael,12345-6,Gold,Tecnologia,"Olá Rafael, analisamos seu perfil..."
```

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/etl-python-portfolio.git
cd etl-python-portfolio
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o pipeline:

```bash
python src/main.py
```

## Resultado Esperado

Ao final da execução, o arquivo `usuarios_transformados.csv` será criado dentro da pasta `data`, contendo os dados originais e uma nova coluna com mensagens personalizadas.

## Conceitos Aplicados

- Manipulação de dados com Pandas
- Organização de projeto Python
- Separação de responsabilidades por módulos
- Pipeline ETL
- Simulação de transformação inteligente de dados
- Boas práticas para projetos de portfólio

## Possíveis Melhorias Futuras

- Integração com uma API real
- Uso da API da OpenAI para gerar mensagens com IA
- Carregamento dos dados em banco PostgreSQL
- Criação de logs de execução
- Dockerização do projeto
- Testes automatizados com Pytest

## Autor

Desenvolvido por Rafael SV como projeto prático de Ciência de Dados e Python.
