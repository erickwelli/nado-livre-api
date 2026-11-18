from flask import Blueprint, request
from app.schemas.nadador_schema import NadadorSchema
from app.controllers.nadador_controller import (
    criar_nadador, listar_nadadores, buscar_nadador,
    atualizar_nadador, excluir_nadador
)

nadadores_bp = Blueprint("nadadores", __name__)
nadador_schema = NadadorSchema()
nadadores_schema = NadadorSchema(many=True)


@nadadores_bp.route("/nadadores", methods=["POST"])
def cadastrar_nadador():
    dados = request.get_json(silent=True) or {}
    obrigatorios = ["nome", "cpf", "telefone", "email"]
    faltantes = [campo for campo in obrigatorios if not dados.get(campo)]
    if faltantes:
        return {"erro": f"Campos obrigatórios: {', '.join(faltantes)}"}, 400
    nadador, erro = criar_nadador(*(dados[campo] for campo in obrigatorios))
    if erro:
        return {"erro": erro}, 400
    return nadador_schema.dump(nadador), 201


@nadadores_bp.route("/nadadores", methods=["GET"])
def consultar_nadadores():
    return nadadores_schema.dump(listar_nadadores()), 200


@nadadores_bp.route("/nadadores/<int:id_nadador>", methods=["GET"])
def consultar_nadador(id_nadador):
    nadador = buscar_nadador(id_nadador)
    if not nadador:
        return {"erro": "Nadador não encontrado"}, 404
    return nadador_schema.dump(nadador), 200


@nadadores_bp.route("/nadadores/<int:id_nadador>", methods=["PATCH", "PUT"])
def editar_nadador(id_nadador):
    dados = request.get_json(silent=True) or {}
    nadador, erro = atualizar_nadador(id_nadador, dados)
    if erro:
        return {"erro": erro}, 404 if "não encontrado" in erro else 400
    return nadador_schema.dump(nadador), 200


@nadadores_bp.route("/nadadores/<int:id_nadador>", methods=["DELETE"])
def remover_nadador(id_nadador):
    sucesso, erro = excluir_nadador(id_nadador)
    if erro:
        return {"erro": erro}, 404 if "não encontrado" in erro else 409
    return {"mensagem": "Nadador excluído com sucesso"}, 200
