from app import db
from app.models.toalha import Toalha


def criar_toalha(dados):
    toalha = Toalha(codigo=dados["codigo"].strip(), status="disponivel")
    db.session.add(toalha)
    db.session.commit()
    return toalha


def listar_toalhas():
    return Toalha.query.order_by(Toalha.id_toalha.asc()).all()


def buscar_toalha(id_toalha):
    return db.session.get(Toalha, id_toalha)


def atualizar_toalha(id_toalha, dados):
    toalha = buscar_toalha(id_toalha)
    if not toalha:
        return None, "Toalha não encontrada"
    if "codigo" in dados:
        codigo = dados["codigo"].strip()
        duplicada = Toalha.query.filter(Toalha.codigo == codigo, Toalha.id_toalha != id_toalha).first()
        if duplicada:
            return None, "Já existe uma toalha com esse código"
        toalha.codigo = codigo
    db.session.commit()
    return toalha, None


def excluir_toalha(id_toalha):
    toalha = buscar_toalha(id_toalha)
    if not toalha:
        return False, "Toalha não encontrada"
    if toalha.movimentacoes:
        return False, "Não é possível excluir toalha que possui movimentações"
    db.session.delete(toalha)
    db.session.commit()
    return True, None


def listar_toalhas_disponiveis():
    return Toalha.query.filter_by(status="disponivel").all()


def listar_toalhas_em_uso():
    return Toalha.query.filter_by(status="em_uso").all()
