from app import db
from app.models.funcionario import Funcionario
from app.models.usuario import Usuario


def criar_funcionario(id_usuario):
    usuario = Usuario.query.get(id_usuario)

    if not usuario:
        return None, "Usuário não encontrado"

    if usuario.funcionario:
        return None, "Usuário já está cadastrado como funcionário"

    funcionario = Funcionario(
        id_funcionario=id_usuario
    )

    db.session.add(funcionario)
    db.session.commit()

    return funcionario, None


def listar_funcionarios():
    return Funcionario.query.all()


def buscar_funcionario(id_funcionario):
    return Funcionario.query.get(id_funcionario)