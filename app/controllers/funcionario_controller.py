from app import db
from app.models.funcionario import Funcionario
from app.models.usuario import Usuario


def criar_funcionario(nome, cpf, telefone, email):
    usuario = Usuario.query.filter((Usuario.cpf == cpf) | (Usuario.email == email)).first()
    if usuario:
        return None, "CPF ou e-mail já cadastrado"
    usuario = Usuario(nome=nome, cpf=cpf, telefone=telefone, email=email)
    db.session.add(usuario)
    db.session.flush()
    funcionario = Funcionario(id_funcionario=usuario.id_usuario)
    db.session.add(funcionario)
    db.session.commit()
    return funcionario, None


def listar_funcionarios():
    return Funcionario.query.all()


def buscar_funcionario(id_funcionario):
    return db.session.get(Funcionario, id_funcionario)


def atualizar_funcionario(id_funcionario, dados):
    funcionario = buscar_funcionario(id_funcionario)
    if not funcionario:
        return None, "Funcionário não encontrado"
    usuario = funcionario.usuario
    cpf = dados.get("cpf", usuario.cpf)
    email = dados.get("email", usuario.email)
    duplicado = Usuario.query.filter(
        ((Usuario.cpf == cpf) | (Usuario.email == email)) & (Usuario.id_usuario != usuario.id_usuario)
    ).first()
    if duplicado:
        return None, "CPF ou e-mail já cadastrado por outro usuário"
    for campo in ("nome", "cpf", "telefone", "email"):
        if campo in dados:
            setattr(usuario, campo, dados[campo])
    db.session.commit()
    return funcionario, None


def excluir_funcionario(id_funcionario):
    funcionario = buscar_funcionario(id_funcionario)
    if not funcionario:
        return False, "Funcionário não encontrado"
    if funcionario.movimentacoes:
        return False, "Não é possível excluir funcionário vinculado a movimentações"
    usuario = funcionario.usuario
    db.session.delete(funcionario)
    db.session.delete(usuario)
    db.session.commit()
    return True, None
