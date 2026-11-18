from flask import Blueprint, request
from datetime import datetime
from app.schemas.movimentacao_schema import MovimentacaoSchema
from app.controllers.movimentacao_controller import (
    criar_movimentacao, devolver_toalha, listar_movimentacoes,
    buscar_movimentacao, historico_toalha, movimentacoes_em_aberto,
    movimentacao_aberta_da_toalha
)

movimentacoes_bp = Blueprint("movimentacoes", __name__)
movimentacao_schema = MovimentacaoSchema()
movimentacoes_schema = MovimentacaoSchema(many=True)


@movimentacoes_bp.route("/movimentacoes", methods=["POST"])
def registrar_retirada():
    dados = request.get_json(silent=True) or {}
    obrigatorios = ["id_funcionario", "id_nadador", "id_toalha"]
    if any(campo not in dados for campo in obrigatorios):
        return {"erro": "Informe id_funcionario, id_nadador e id_toalha"}, 400
    try:
        ids = [int(dados[campo]) for campo in obrigatorios]
    except (TypeError, ValueError):
        return {"erro": "Os identificadores devem ser números inteiros"}, 400
    data_hora = None
    if dados.get("dataHora"):
        try:
            data_hora = datetime.fromisoformat(dados["dataHora"])
        except (TypeError, ValueError):
            return {"erro": "dataHora deve estar no formato ISO (AAAA-MM-DDTHH:MM)"}, 400
    movimentacao, erro = criar_movimentacao(*ids, data_hora_retirada=data_hora)
    if erro:
        return {"erro": erro}, 400
    return movimentacao_schema.dump(movimentacao), 201


@movimentacoes_bp.route("/movimentacoes/<int:id_movimentacao>/devolucao", methods=["PUT"])
def registrar_devolucao(id_movimentacao):
    dados = request.get_json(silent=True) or {}
    data_hora = None
    if dados.get("dataHora"):
        try:
            data_hora = datetime.fromisoformat(dados["dataHora"])
        except (TypeError, ValueError):
            return {"erro": "dataHora deve estar no formato ISO (AAAA-MM-DDTHH:MM)"}, 400
    movimentacao, erro = devolver_toalha(id_movimentacao, data_hora)
    if erro:
        return {"erro": erro}, 404 if "não encontrada" in erro else 409
    return movimentacao_schema.dump(movimentacao), 200


@movimentacoes_bp.route("/toalhas/<int:id_toalha>/devolucao", methods=["PUT"])
def devolver_por_toalha(id_toalha):
    movimentacao = movimentacao_aberta_da_toalha(id_toalha)
    if not movimentacao:
        return {"erro": "Não existe retirada em aberto para esta toalha"}, 404
    dados = request.get_json(silent=True) or {}
    data_hora = None
    if dados.get("dataHora"):
        try:
            data_hora = datetime.fromisoformat(dados["dataHora"])
        except (TypeError, ValueError):
            return {"erro": "dataHora deve estar no formato ISO (AAAA-MM-DDTHH:MM)"}, 400
    movimentacao, erro = devolver_toalha(movimentacao.id_movimentacao, data_hora)
    if erro:
        return {"erro": erro}, 409
    return movimentacao_schema.dump(movimentacao), 200


@movimentacoes_bp.route("/movimentacoes", methods=["GET"])
def consultar_movimentacoes():
    return movimentacoes_schema.dump(listar_movimentacoes()), 200


@movimentacoes_bp.route("/movimentacoes/<int:id_movimentacao>", methods=["GET"])
def consultar_movimentacao(id_movimentacao):
    movimentacao = buscar_movimentacao(id_movimentacao)
    if not movimentacao:
        return {"erro": "Movimentação não encontrada"}, 404
    return movimentacao_schema.dump(movimentacao), 200


@movimentacoes_bp.route("/toalhas/<int:id_toalha>/historico", methods=["GET"])
def consultar_historico_toalha(id_toalha):
    return movimentacoes_schema.dump(historico_toalha(id_toalha)), 200


@movimentacoes_bp.route("/movimentacoes/em-aberto", methods=["GET"])
def consultar_movimentacoes_em_aberto():
    return movimentacoes_schema.dump(movimentacoes_em_aberto()), 200
