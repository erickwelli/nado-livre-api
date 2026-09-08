# Nado Livre API

API desenvolvida para o controle de toalhas de uma escola de natação, permitindo o cadastro de usuários, funcionários, nadadores e toalhas, além do registro e consulta de movimentações.

## Tecnologias

* Python
* Flask
* Flask-SQLAlchemy
* Marshmallow
* SQLite
* Postman

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/erickwelli/nado-livre-api.git
cd nado-livre-api
```

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a API

```bash
python app.py
```

A API estará disponível em:

`http://127.0.0.1:5000`

O banco de dados utilizado é o SQLite e é criado automaticamente na pasta `instance/`.

## Endpoints principais

| Método | Endpoint                        | Função                         |
| ------ | ------------------------------- | ------------------------------ |
| POST   | `/usuarios`                     | Cadastrar usuário              |
| GET    | `/usuarios`                     | Listar usuários                |
| GET    | `/usuarios/<id>`                | Buscar usuário                 |
| POST   | `/funcionarios`                 | Cadastrar funcionário          |
| GET    | `/funcionarios`                 | Listar funcionários            |
| GET    | `/funcionarios/<id>`            | Buscar funcionário             |
| POST   | `/nadadores`                    | Cadastrar nadador              |
| GET    | `/nadadores`                    | Listar nadadores               |
| GET    | `/nadadores/<id>`               | Buscar nadador                 |
| POST   | `/toalhas`                      | Cadastrar toalha               |
| GET    | `/toalhas`                      | Listar toalhas                 |
| GET    | `/toalhas/<id>`                 | Buscar toalha                  |
| GET    | `/toalhas/disponiveis`          | Listar toalhas disponíveis     |
| GET    | `/toalhas/em-uso`               | Listar toalhas em uso          |
| POST   | `/movimentacoes`                | Registrar retirada             |
| GET    | `/movimentacoes`                | Listar movimentações           |
| GET    | `/movimentacoes/<id>`           | Buscar movimentação            |
| PUT    | `/movimentacoes/<id>/devolucao` | Registrar devolução            |
| GET    | `/movimentacoes/em-aberto`      | Listar movimentações em aberto |
| GET    | `/toalhas/<id>/historico`       | Consultar histórico da toalha  |

## Dados necessários para cadastro

* **Usuário:** nome, CPF, telefone e e-mail.
* **Funcionário:** ID do usuário.
* **Nadador:** ID do usuário.
* **Toalha:** código. Ex: (T001)
* **Movimentação:** ID do funcionário, ID do nadador e ID da toalha.
* **Devolução:** não possui dados no Body; utiliza o ID da movimentação na URL.

## Testes com Postman

Para as requisições `POST`, utilizar:

**Body → raw → JSON**

Os IDs utilizados nas requisições devem corresponder aos registros existentes no banco de dados.

## Funcionalidades

* Cadastro de usuários, funcionários e nadadores.
* Cadastro e consulta de toalhas.
* Controle do status das toalhas.
* Registro de retirada e devolução.
* Bloqueio de retirada de toalhas que já estão em uso.
* Consulta de toalhas disponíveis e em uso.
* Histórico de movimentações.

## Projeto acadêmico

Projeto desenvolvido como atividade acadêmica para simulação do desenvolvimento de uma API.
