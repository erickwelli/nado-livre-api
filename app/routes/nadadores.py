from flask import Blueprint, request
from app.schemas.nadador_schema import NadadorSchema
from app.controllers.nadador_controller import (
    criar_nadador,
    listar_nadadores,
    buscar_nadador
)

nadadores_bp = Blueprint("nadadores", __name__)

nadador_schema = NadadorSchema()
nadadores_schema = NadadorSchema(many=True)


@nadadores_bp.route("/nadadores", methods=["POST"])
def cadastrar_nadador():
    dados = request.get_json()

    if not dados:
        return {"erro": "Dados são obrigatórios"}, 400

    campos_obrigatorios = ["nome", "cpf", "telefone", "email"]

    for campo in campos_obrigatorios:
        if campo not in dados:
            return {"erro": f"{campo} é obrigatório"}, 400

    nadador, erro = criar_nadador(
        dados["nome"],
        dados["cpf"],
        dados["telefone"],
        dados["email"]
    )

    if erro:
        return {"erro": erro}, 400

    return nadador_schema.dump(nadador), 201


@nadadores_bp.route("/nadadores", methods=["GET"])
def consultar_nadadores():
    nadadores = listar_nadadores()

    return nadadores_schema.dump(nadadores), 200


@nadadores_bp.route(
    "/nadadores/<int:id_nadador>",
    methods=["GET"]
)
def consultar_nadador(id_nadador):
    nadador = buscar_nadador(id_nadador)

    if not nadador:
        return {"erro": "Nadador não encontrado"}, 404

    return nadador_schema.dump(nadador), 200