from app import db
from app.models.funcionario import Funcionario
from app.models.usuario import Usuario


def criar_funcionario(nome, cpf, telefone, email):
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

    funcionario = Funcionario(
        id_funcionario=usuario.id_usuario
    )

    db.session.add(funcionario)
    db.session.commit()

    return funcionario, None


def listar_funcionarios():
    return Funcionario.query.all()


def buscar_funcionario(id_funcionario):
    return Funcionario.query.get(id_funcionario)