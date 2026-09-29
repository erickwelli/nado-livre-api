Nado Livre API

API desenvolvida para o controle de toalhas de uma escola de natação, permitindo o cadastro de funcionários, nadadores e toalhas, além do registro e consulta de movimentações.

Tecnologias

* Python
* Flask
* Flask-SQLAlchemy
* Marshmallow
* SQLite
* Postman

Como executar

1. Clonar o repositório

git clone https://github.com/erickwelli/nado-livre-api.git
cd nado-livre-api

2. Criar o ambiente virtual

python -m venv venv

3. Ativar o ambiente virtual

No Windows:

venv\Scripts\activate

4. Instalar as dependências

pip install -r requirements.txt

5. Executar a API

python app.py

A API estará disponível em:

"http://127.0.0.1:5000"

O banco de dados utilizado é o SQLite e é criado automaticamente na pasta "instance/".

Endpoints principais

Método| Endpoint| Função
POST| "/funcionarios"| Cadastrar funcionário
GET| "/funcionarios"| Listar funcionários
GET| "/funcionarios/<id>"| Buscar funcionário
POST| "/nadadores"| Cadastrar nadador
GET| "/nadadores"| Listar nadadores
GET| "/nadadores/<id>"| Buscar nadador
POST| "/toalhas"| Cadastrar toalha
GET| "/toalhas"| Listar toalhas
GET| "/toalhas/<id>"| Buscar toalha
GET| "/toalhas/disponiveis"| Listar toalhas disponíveis
GET| "/toalhas/em-uso"| Listar toalhas em uso
POST| "/movimentacoes"| Registrar retirada
GET| "/movimentacoes"| Listar movimentações
GET| "/movimentacoes/<id>"| Buscar movimentação
PUT| "/movimentacoes/<id>/devolucao"| Registrar devolução
GET| "/movimentacoes/em-aberto"| Listar movimentações em aberto
GET| "/toalhas/<id>/historico"| Consultar histórico da toalha

Dados necessários para cadastro

* Funcionário: nome, CPF, telefone e e-mail.
* Nadador: nome, CPF, telefone e e-mail.
* Toalha: código. Ex: (T001)
* Movimentação: ID do funcionário, ID do nadador e ID da toalha.
* Devolução: não possui dados no Body; utiliza o ID da movimentação na URL.

Testes com Postman

Para as requisições "POST", utilizar:

Body → raw → JSON

Os IDs utilizados nas requisições devem corresponder aos registros existentes no banco de dados.

Para requisições "GET", não é necessário enviar dados no Body.

Funcionalidades

* Cadastro de funcionários e nadadores.
* Cadastro e consulta de toalhas.
* Controle do status das toalhas.
* Registro de retirada e devolução.
* Bloqueio de retirada de toalhas que já estão em uso.
* Consulta de toalhas disponíveis e em uso.
* Histórico de movimentações.

Projeto acadêmico

Projeto desenvolvido como atividade acadêmica para simulação do desenvolvimento de uma API.
