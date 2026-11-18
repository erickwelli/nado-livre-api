from flask import Blueprint, request
from app.schemas.funcionario_schema import FuncionarioSchema
from app.controllers.funcionario_controller import (
    criar_funcionario, listar_funcionarios, buscar_funcionario,
    atualizar_funcionario, excluir_funcionario
)

funcionarios_bp = Blueprint("funcionarios", __name__)
funcionario_schema = FuncionarioSchema()
funcionarios_schema = FuncionarioSchema(many=True)


@funcionarios_bp.route("/funcionarios", methods=["POST"])
def cadastrar_funcionario():
    dados = request.get_json(silent=True) or {}
    obrigatorios = ["nome", "cpf", "telefone", "email"]
    faltantes = [campo for campo in obrigatorios if not dados.get(campo)]
    if faltantes:
        return {"erro": f"Campos obrigatórios: {', '.join(faltantes)}"}, 400
    funcionario, erro = criar_funcionario(*(dados[campo] for campo in obrigatorios))
    if erro:
        return {"erro": erro}, 400
    return funcionario_schema.dump(funcionario), 201


@funcionarios_bp.route("/funcionarios", methods=["GET"])
def consultar_funcionarios():
    return funcionarios_schema.dump(listar_funcionarios()), 200


@funcionarios_bp.route("/funcionarios/<int:id_funcionario>", methods=["GET"])
def consultar_funcionario(id_funcionario):
    funcionario = buscar_funcionario(id_funcionario)
    if not funcionario:
        return {"erro": "Funcionário não encontrado"}, 404
    return funcionario_schema.dump(funcionario), 200


@funcionarios_bp.route("/funcionarios/<int:id_funcionario>", methods=["PATCH", "PUT"])
def editar_funcionario(id_funcionario):
    dados = request.get_json(silent=True) or {}
    funcionario, erro = atualizar_funcionario(id_funcionario, dados)
    if erro:
        return {"erro": erro}, 404 if funcionario is None and erro.endswith("não encontrado") else 400
    return funcionario_schema.dump(funcionario), 200


@funcionarios_bp.route("/funcionarios/<int:id_funcionario>", methods=["DELETE"])
def remover_funcionario(id_funcionario):
    sucesso, erro = excluir_funcionario(id_funcionario)
    if erro:
        return {"erro": erro}, 404 if "não encontrado" in erro else 409
    return {"mensagem": "Funcionário excluído com sucesso"}, 200
