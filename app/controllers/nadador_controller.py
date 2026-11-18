from app import db
from app.models.nadador import Nadador
from app.models.usuario import Usuario


def criar_nadador(nome, cpf, telefone, email):
    usuario = Usuario.query.filter((Usuario.cpf == cpf) | (Usuario.email == email)).first()
    if usuario:
        return None, "CPF ou e-mail já cadastrado"
    usuario = Usuario(nome=nome, cpf=cpf, telefone=telefone, email=email)
    db.session.add(usuario)
    db.session.flush()
    nadador = Nadador(id_nadador=usuario.id_usuario)
    db.session.add(nadador)
    db.session.commit()
    return nadador, None


def listar_nadadores():
    return Nadador.query.all()


def buscar_nadador(id_nadador):
    return db.session.get(Nadador, id_nadador)


def atualizar_nadador(id_nadador, dados):
    nadador = buscar_nadador(id_nadador)
    if not nadador:
        return None, "Nadador não encontrado"
    usuario = nadador.usuario
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
    return nadador, None


def excluir_nadador(id_nadador):
    nadador = buscar_nadador(id_nadador)
    if not nadador:
        return False, "Nadador não encontrado"
    if nadador.movimentacoes:
        return False, "Não é possível excluir nadador vinculado a movimentações"
    usuario = nadador.usuario
    db.session.delete(nadador)
    db.session.delete(usuario)
    db.session.commit()
    return True, None
