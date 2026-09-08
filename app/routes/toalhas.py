from flask import Blueprint, request
from app.schemas.toalha_schema import ToalhaSchema
from app.controllers.toalha_controller import (
    criar_toalha,
    listar_toalhas,
    buscar_toalha,
    listar_toalhas_disponiveis,
    listar_toalhas_em_uso
)

toalhas_bp = Blueprint("toalhas", __name__)

toalha_schema = ToalhaSchema()
toalhas_schema = ToalhaSchema(many=True)


@toalhas_bp.route("/toalhas", methods=["POST"])
def cadastrar_toalha():
    dados = request.get_json()

    try:
        dados_validados = toalha_schema.load(dados)
    except Exception as erro:
        return {"erro": erro.messages}, 400

    toalha = criar_toalha(dados_validados)

    return toalha_schema.dump(toalha), 201


@toalhas_bp.route("/toalhas", methods=["GET"])
def consultar_toalhas():
    toalhas = listar_toalhas()

    return toalhas_schema.dump(toalhas), 200


@toalhas_bp.route(
    "/toalhas/<int:id_toalha>",
    methods=["GET"]
)
def consultar_toalha(id_toalha):
    toalha = buscar_toalha(id_toalha)

    if not toalha:
        return {"erro": "Toalha não encontrada"}, 404

    return toalha_schema.dump(toalha), 200


@toalhas_bp.route(
    "/toalhas/disponiveis",
    methods=["GET"]
)
def consultar_toalhas_disponiveis():
    toalhas = listar_toalhas_disponiveis()

    return toalhas_schema.dump(toalhas), 200


@toalhas_bp.route(
    "/toalhas/em-uso",
    methods=["GET"]
)
def consultar_toalhas_em_uso():
    toalhas = listar_toalhas_em_uso()

    return toalhas_schema.dump(toalhas), 200