from flask import Blueprint, request
from app.schemas.movimentacao_schema import MovimentacaoSchema
from app.controllers.movimentacao_controller import (
    criar_movimentacao,
    devolver_toalha,
    listar_movimentacoes,
    buscar_movimentacao,
    historico_toalha,
    movimentacoes_em_aberto
)

movimentacoes_bp = Blueprint("movimentacoes", __name__)

movimentacao_schema = MovimentacaoSchema()
movimentacoes_schema = MovimentacaoSchema(many=True)


@movimentacoes_bp.route("/movimentacoes", methods=["POST"])
def registrar_retirada():
    dados = request.get_json()

    try:
        dados_validados = movimentacao_schema.load(dados)
    except Exception as erro:
        return {"erro": erro.messages}, 400

    movimentacao, erro = criar_movimentacao(
        dados_validados["id_funcionario"],
        dados_validados["id_nadador"],
        dados_validados["id_toalha"]
    )

    if erro:
        return {"erro": erro}, 400

    return movimentacao_schema.dump(movimentacao), 201


@movimentacoes_bp.route(
    "/movimentacoes/<int:id_movimentacao>/devolucao",
    methods=["PUT"]
)
def registrar_devolucao(id_movimentacao):
    movimentacao, erro = devolver_toalha(
        id_movimentacao
    )

    if erro:
        return {"erro": erro}, 400

    return movimentacao_schema.dump(movimentacao), 200


@movimentacoes_bp.route(
    "/movimentacoes",
    methods=["GET"]
)
def consultar_movimentacoes():
    movimentacoes = listar_movimentacoes()

    return movimentacoes_schema.dump(movimentacoes), 200


@movimentacoes_bp.route(
    "/movimentacoes/<int:id_movimentacao>",
    methods=["GET"]
)
def consultar_movimentacao(id_movimentacao):
    movimentacao = buscar_movimentacao(
        id_movimentacao
    )

    if not movimentacao:
        return {"erro": "Movimentação não encontrada"}, 404

    return movimentacao_schema.dump(movimentacao), 200


@movimentacoes_bp.route(
    "/toalhas/<int:id_toalha>/historico",
    methods=["GET"]
)
def consultar_historico_toalha(id_toalha):
    movimentacoes = historico_toalha(id_toalha)

    return movimentacoes_schema.dump(
        movimentacoes
    ), 200


@movimentacoes_bp.route(
    "/movimentacoes/em-aberto",
    methods=["GET"]
)
def consultar_movimentacoes_em_aberto():
    movimentacoes = movimentacoes_em_aberto()

    return movimentacoes_schema.dump(
        movimentacoes
    ), 200