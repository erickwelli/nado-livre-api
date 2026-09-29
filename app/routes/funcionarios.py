from flask import Blueprint, request
from app.schemas.funcionario_schema import FuncionarioSchema
from app.controllers.funcionario_controller import (
    criar_funcionario,
    listar_funcionarios,
    buscar_funcionario
)

funcionarios_bp = Blueprint("funcionarios", __name__)

funcionario_schema = FuncionarioSchema()
funcionarios_schema = FuncionarioSchema(many=True)


@funcionarios_bp.route("/funcionarios", methods=["POST"])
def cadastrar_funcionario():
    dados = request.get_json()

    if not dados:
        return {"erro": "Dados são obrigatórios"}, 400

    campos_obrigatorios = ["nome", "cpf", "telefone", "email"]

    for campo in campos_obrigatorios:
        if campo not in dados:
            return {"erro": f"{campo} é obrigatório"}, 400

    funcionario, erro = criar_funcionario(
        dados["nome"],
        dados["cpf"],
        dados["telefone"],
        dados["email"]
    )

    if erro:
        return {"erro": erro}, 400

    return funcionario_schema.dump(funcionario), 201


@funcionarios_bp.route("/funcionarios", methods=["GET"])
def consultar_funcionarios():
    funcionarios = listar_funcionarios()

    return funcionarios_schema.dump(funcionarios), 200


@funcionarios_bp.route(
    "/funcionarios/<int:id_funcionario>",
    methods=["GET"]
)
def consultar_funcionario(id_funcionario):
    funcionario = buscar_funcionario(id_funcionario)

    if not funcionario:
        return {"erro": "Funcionário não encontrado"}, 404

    return funcionario_schema.dump(funcionario), 200
