from flask import Blueprint, request
from app.schemas.toalha_schema import ToalhaSchema
from app.controllers.toalha_controller import (
    criar_toalha, listar_toalhas, buscar_toalha, atualizar_toalha,
    excluir_toalha, listar_toalhas_disponiveis, listar_toalhas_em_uso
)

toalhas_bp = Blueprint("toalhas", __name__)
toalha_schema = ToalhaSchema()
toalhas_schema = ToalhaSchema(many=True)


@toalhas_bp.route("/toalhas", methods=["POST"])
def cadastrar_toalha():
    dados = request.get_json(silent=True) or {}
    codigo = str(dados.get("codigo", "")).strip()
    if not codigo:
        return {"erro": "Código da toalha é obrigatório"}, 400
    try:
        toalha = criar_toalha({"codigo": codigo})
    except Exception as erro:
        from sqlalchemy.exc import IntegrityError
        if isinstance(erro, IntegrityError):
            from app import db
            db.session.rollback()
            return {"erro": "Já existe uma toalha com esse código"}, 400
        raise
    return toalha_schema.dump(toalha), 201


@toalhas_bp.route("/toalhas", methods=["GET"])
def consultar_toalhas():
    return toalhas_schema.dump(listar_toalhas()), 200


@toalhas_bp.route("/toalhas/<int:id_toalha>", methods=["GET"])
def consultar_toalha(id_toalha):
    toalha = buscar_toalha(id_toalha)
    if not toalha:
        return {"erro": "Toalha não encontrada"}, 404
    return toalha_schema.dump(toalha), 200


@toalhas_bp.route("/toalhas/<int:id_toalha>", methods=["PATCH", "PUT"])
def editar_toalha(id_toalha):
    dados = request.get_json(silent=True) or {}
    toalha, erro = atualizar_toalha(id_toalha, dados)
    if erro:
        return {"erro": erro}, 404 if "não encontrada" in erro else 400
    return toalha_schema.dump(toalha), 200


@toalhas_bp.route("/toalhas/<int:id_toalha>", methods=["DELETE"])
def remover_toalha(id_toalha):
    sucesso, erro = excluir_toalha(id_toalha)
    if erro:
        return {"erro": erro}, 404 if "não encontrada" in erro else 409
    return {"mensagem": "Toalha excluída com sucesso"}, 200


@toalhas_bp.route("/toalhas/disponiveis", methods=["GET"])
def consultar_toalhas_disponiveis():
    return toalhas_schema.dump(listar_toalhas_disponiveis()), 200


@toalhas_bp.route("/toalhas/em-uso", methods=["GET"])
def consultar_toalhas_em_uso():
    return toalhas_schema.dump(listar_toalhas_em_uso()), 200
