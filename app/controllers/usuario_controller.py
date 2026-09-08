from app import db
from app.models.usuario import Usuario


def criar_usuario(dados):
    usuario = Usuario(
        nome=dados["nome"],
        cpf=dados["cpf"],
        telefone=dados["telefone"],
        email=dados["email"]
    )

    db.session.add(usuario)
    db.session.commit()

    return usuario


def listar_usuarios():
    return Usuario.query.all()


def buscar_usuario(id_usuario):
    return Usuario.query.get(id_usuario)