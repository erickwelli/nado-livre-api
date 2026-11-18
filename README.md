# Nado Livre API

API REST em Flask para o sistema de controle de toalhas de uma escola de natação.

## Tecnologias

- Python
- Flask
- Flask-SQLAlchemy
- Marshmallow
- SQLite

## Executar no Windows (CMD)

Na pasta `nado-livre-api`, execute:

```cmd
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
py app.py
```

A API será iniciada em `http://127.0.0.1:5000`. O banco `instance/nado_livre.db` é criado automaticamente.

Para verificar, acesse `http://127.0.0.1:5000`. A API deve retornar uma mensagem de funcionamento.

## Endpoints

| Método | Endpoint | Função |
|---|---|---|
| GET, POST | `/funcionarios` | Listar e cadastrar funcionários |
| GET, PATCH, PUT, DELETE | `/funcionarios/<id>` | Consultar, editar e excluir funcionário |
| GET, POST | `/nadadores` | Listar e cadastrar nadadores |
| GET, PATCH, PUT, DELETE | `/nadadores/<id>` | Consultar, editar e excluir nadador |
| GET, POST | `/toalhas` | Listar e cadastrar toalhas |
| GET, PATCH, PUT, DELETE | `/toalhas/<id>` | Consultar, editar e excluir toalha |
| GET | `/toalhas/disponiveis` | Listar toalhas disponíveis |
| GET | `/toalhas/em-uso` | Listar toalhas em uso |
| GET, POST | `/movimentacoes` | Listar movimentações e registrar retirada |
| PUT | `/movimentacoes/<id>/devolucao` | Registrar devolução por ID da movimentação |
| PUT | `/toalhas/<id>/devolucao` | Registrar devolução por ID da toalha |
| GET | `/movimentacoes/em-aberto` | Listar retiradas não devolvidas |
| GET | `/toalhas/<id>/historico` | Consultar histórico de uma toalha |

## Formato dos dados

Cadastro de funcionário ou nadador:

```json
{
  "nome": "Nome de exemplo",
  "cpf": "000.000.000-00",
  "telefone": "(84) 90000-0000",
  "email": "exemplo@email.com"
}
```

Cadastro de toalha:

```json
{
  "codigo": "T001"
}
```

Retirada:

```json
{
  "id_funcionario": 1,
  "id_nadador": 2,
  "id_toalha": 1,
  "dataHora": "2026-11-10T14:30"
}
```

A API controla o status da toalha. Uma retirada cria uma movimentação e altera o status para `em_uso`. A devolução preenche `data_hora_devolucao` na mesma movimentação e altera o status para `disponivel`.

## Integração com o frontend

O frontend é executado separadamente (por exemplo, com Live Server ou `py -m http.server 5501`) e consome esta API pela URL `http://127.0.0.1:5000`. O CORS está habilitado para permitir essa comunicação durante o desenvolvimento.
