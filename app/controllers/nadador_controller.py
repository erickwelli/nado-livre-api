from app import db
from app.models.nadador import Nadador
from app.models.usuario import Usuario


def criar_nadador(nome, cpf, telefone, email):
    usuario = Usuario.query.filter(
        (Usuario.cpf == cpf) | (Usuario.email == email)
    ).first()

    if usuario:
        return None, "CPF ou e-mail já cadastrado"

    usuario = Usuario(
        nome=nome,
        cpf=cpf,
        telefone=telefone,
        email=email
    )

    db.session.add(usuario)
    db.session.flush()

    nadador = Nadador(
        id_nadador=usuario.id_usuario
    )

    db.session.add(nadador)
    db.session.commit()

    return nadador, None


def listar_nadadores():
    return Nadador.query.all()


def buscar_nadador(id_nadador):
    return Nadador.query.get(id_nadador)