from app import db
from app.models.nadador import Nadador
from app.models.usuario import Usuario


def criar_nadador(id_usuario):
    usuario = Usuario.query.get(id_usuario)

    if not usuario:
        return None, "Usuário não encontrado"

    if usuario.nadador:
        return None, "Usuário já está cadastrado como nadador"

    nadador = Nadador(
        id_nadador=id_usuario
    )

    db.session.add(nadador)
    db.session.commit()

    return nadador, None


def listar_nadadores():
    return Nadador.query.all()


def buscar_nadador(id_nadador):
    return Nadador.query.get(id_nadador)