from datetime import datetime
from app import db
from app.models.movimentacao import Movimentacao
from app.models.funcionario import Funcionario
from app.models.nadador import Nadador
from app.models.toalha import Toalha


def criar_movimentacao(id_funcionario, id_nadador, id_toalha, data_hora_retirada=None):
    funcionario = db.session.get(Funcionario, id_funcionario)
    if not funcionario:
        return None, "Funcionário não encontrado"
    nadador = db.session.get(Nadador, id_nadador)
    if not nadador:
        return None, "Nadador não encontrado"
    toalha = db.session.get(Toalha, id_toalha)
    if not toalha:
        return None, "Toalha não encontrada"
    if toalha.status != "disponivel":
        return None, "Toalha não está disponível"
    movimentacao = Movimentacao(
        id_funcionario=id_funcionario,
        id_nadador=id_nadador,
        id_toalha=id_toalha,
        data_hora_retirada=data_hora_retirada or datetime.now()
    )
    toalha.status = "em_uso"
    db.session.add(movimentacao)
    db.session.commit()
    return movimentacao, None


def devolver_toalha(id_movimentacao, data_hora_devolucao=None):
    movimentacao = db.session.get(Movimentacao, id_movimentacao)
    if not movimentacao:
        return None, "Movimentação não encontrada"
    if movimentacao.data_hora_devolucao:
        return None, "Toalha já foi devolvida"
    movimentacao.data_hora_devolucao = data_hora_devolucao or datetime.now()
    movimentacao.toalha.status = "disponivel"
    db.session.commit()
    return movimentacao, None


def movimentacao_aberta_da_toalha(id_toalha):
    return Movimentacao.query.filter_by(id_toalha=id_toalha, data_hora_devolucao=None).first()


def listar_movimentacoes():
    return Movimentacao.query.order_by(Movimentacao.data_hora_retirada.desc()).all()


def buscar_movimentacao(id_movimentacao):
    return db.session.get(Movimentacao, id_movimentacao)


def historico_toalha(id_toalha):
    return Movimentacao.query.filter_by(id_toalha=id_toalha).order_by(Movimentacao.data_hora_retirada.desc()).all()


def movimentacoes_em_aberto():
    return Movimentacao.query.filter(Movimentacao.data_hora_devolucao.is_(None)).all()
