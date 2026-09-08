from datetime import datetime

from app import db
from app.models.movimentacao import Movimentacao
from app.models.funcionario import Funcionario
from app.models.nadador import Nadador
from app.models.toalha import Toalha


def criar_movimentacao(id_funcionario, id_nadador, id_toalha):
    funcionario = Funcionario.query.get(id_funcionario)

    if not funcionario:
        return None, "Funcionário não encontrado"

    nadador = Nadador.query.get(id_nadador)

    if not nadador:
        return None, "Nadador não encontrado"

    toalha = Toalha.query.get(id_toalha)

    if not toalha:
        return None, "Toalha não encontrada"

    if toalha.status == "em_uso":
        return None, "Toalha já está em uso"

    movimentacao = Movimentacao(
        id_funcionario=id_funcionario,
        id_nadador=id_nadador,
        id_toalha=id_toalha,
        data_hora_retirada=datetime.now()
    )

    toalha.status = "em_uso"

    db.session.add(movimentacao)
    db.session.commit()

    return movimentacao, None


def devolver_toalha(id_movimentacao):
    movimentacao = Movimentacao.query.get(id_movimentacao)

    if not movimentacao:
        return None, "Movimentação não encontrada"

    if movimentacao.data_hora_devolucao:
        return None, "Toalha já foi devolvida"

    movimentacao.data_hora_devolucao = datetime.now()

    movimentacao.toalha.status = "disponivel"

    db.session.commit()

    return movimentacao, None


def listar_movimentacoes():
    return Movimentacao.query.all()


def buscar_movimentacao(id_movimentacao):
    return Movimentacao.query.get(id_movimentacao)


def historico_toalha(id_toalha):
    return Movimentacao.query.filter_by(
        id_toalha=id_toalha
    ).order_by(
        Movimentacao.data_hora_retirada.desc()
    ).all()


def movimentacoes_em_aberto():
    return Movimentacao.query.filter(
        Movimentacao.data_hora_devolucao.is_(None)
    ).all()