from app import db
from app.models.toalha import Toalha


def criar_toalha(dados):
    toalha = Toalha(
        codigo=dados["codigo"],
        status="disponivel"
    )

    db.session.add(toalha)
    db.session.commit()

    return toalha


def listar_toalhas():
    return Toalha.query.all()


def buscar_toalha(id_toalha):
    return Toalha.query.get(id_toalha)


def listar_toalhas_disponiveis():
    return Toalha.query.filter_by(
        status="disponivel"
    ).all()


def listar_toalhas_em_uso():
    return Toalha.query.filter_by(
        status="em_uso"
    ).all()