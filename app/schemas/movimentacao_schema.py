from marshmallow import Schema, fields


class MovimentacaoSchema(Schema):
    id_movimentacao = fields.Int(dump_only=True)

    data_hora_retirada = fields.DateTime(
        dump_only=True
    )

    data_hora_devolucao = fields.DateTime(
        dump_only=True,
        allow_none=True
    )

    id_funcionario = fields.Int(required=True)
    id_nadador = fields.Int(required=True)
    id_toalha = fields.Int(required=True)