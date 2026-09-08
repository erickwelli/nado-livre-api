from flask import Blueprint, request
from app.schemas.usuario_schema import UsuarioSchema
from app.controllers.usuario_controller import (
    criar_usuario,
    listar_usuarios,
    buscar_usuario
)

usuarios_bp = Blueprint("usuarios", __name__)

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)


@usuarios_bp.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    dados = request.get_json()

    try:
        dados_validados = usuario_schema.load(dados)
    except Exception as erro:
        return {"erro": erro.messages}, 400

    usuario = criar_usuario(dados_validados)

    return usuario_schema.dump(usuario), 201


@usuarios_bp.route("/usuarios", methods=["GET"])
def consultar_usuarios():
    usuarios = listar_usuarios()

    return usuarios_schema.dump(usuarios), 200


@usuarios_bp.route("/usuarios/<int:id_usuario>", methods=["GET"])
def consultar_usuario(id_usuario):
    usuario = buscar_usuario(id_usuario)

    if not usuario:
        return {"erro": "Usuário não encontrado"}, 404

    return usuario_schema.dump(usuario), 200