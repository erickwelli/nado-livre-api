# Nado Livre — API de Controle de Toalhas

API desenvolvida para o controle de retirada e devolução de toalhas em uma escola de natação.

## Tecnologias utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Marshmallow
* Postman
* Git/GitHub

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/erickwelli/nado-livre-api.git
```

### 2. Entrar na pasta do projeto

```bash
cd nado-livre-api
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a API

```bash
python app.py
```

A API estará disponível em:

```text
http://127.0.0.1:5000
```

## Testando a API

A API pode ser testada utilizando o Postman.

Para requisições `POST` que necessitam de dados, selecione:

**Body → raw → JSON**

e informe os campos necessários para cada endpoint.

## Principais endpoints

### Usuários

| Método | Endpoint         | Função            |
| ------ | ---------------- | ----------------- |
| POST   | `/usuarios`      | Cadastrar usuário |
| GET    | `/usuarios`      | Listar usuários   |
| GET    | `/usuarios/<id>` | Buscar usuário    |

### Funcionários

| Método | Endpoint             | Função                |
| ------ | -------------------- | --------------------- |
| POST   | `/funcionarios`      | Cadastrar funcionário |
| GET    | `/funcionarios`      | Listar funcionários   |
| GET    | `/funcionarios/<id>` | Buscar funcionário    |

### Nadadores

| Método | Endpoint          | Função            |
| ------ | ----------------- | ----------------- |
| POST   | `/nadadores`      | Cadastrar nadador |
| GET    | `/nadadores`      | Listar nadadores  |
| GET    | `/nadadores/<id>` | Buscar nadador    |

### Toalhas

| Método | Endpoint               | Função                        |
| ------ | ---------------------- | ----------------------------- |
| POST   | `/toalhas`             | Cadastrar toalha              |
| GET    | `/toalhas`             | Listar toalhas                |
| GET    | `/toalhas/<id>`        | Buscar toalha                 |
| GET    | `/toalhas/disponiveis` | Consultar toalhas disponíveis |
| GET    | `/toalhas/em-uso`      | Consultar toalhas em uso      |

### Movimentações

| Método | Endpoint                        | Função                            |
| ------ | ------------------------------- | --------------------------------- |
| POST   | `/movimentacoes`                | Registrar retirada                |
| GET    | `/movimentacoes`                | Listar movimentações              |
| GET    | `/movimentacoes/<id>`           | Buscar movimentação               |
| PUT    | `/movimentacoes/<id>/devolucao` | Registrar devolução               |
| GET    | `/movimentacoes/em-aberto`      | Consultar movimentações em aberto |
| GET    | `/toalhas/<id>/historico`       | Consultar histórico da toalha     |

## Banco de dados

O sistema utiliza **SQLite** como banco de dados.

O banco é criado automaticamente pela aplicação quando ela é executada.

## Funcionalidades

O sistema permite:

* Cadastrar usuários;
* Cadastrar funcionários;
* Cadastrar nadadores;
* Cadastrar toalhas;
* Consultar toalhas disponíveis e em uso;
* Registrar retirada de toalhas;
* Registrar devolução de toalhas;
* Impedir que uma toalha em uso seja retirada novamente;
* Consultar movimentações;
* Consultar movimentações em aberto;
* Consultar o histórico de uma toalha.

## Projeto

**Nado Livre — Controle de Toalhas em uma Escola de Natação**

Projeto desenvolvido como atividade acadêmica.
