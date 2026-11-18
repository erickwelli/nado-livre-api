from marshmallow import Schema, fields


class MovimentacaoSchema(Schema):
    id = fields.Int(attribute="id_movimentacao", dump_only=True)
    dataHora = fields.DateTime(attribute="data_hora_retirada", dump_only=True)
    data_hora_retirada = fields.DateTime(dump_only=True)
    data_hora_devolucao = fields.DateTime(dump_only=True, allow_none=True)
    tipo = fields.Method("obter_tipo")
    id_funcionario = fields.Int(required=True, load_only=True)
    id_nadador = fields.Int(required=True, load_only=True)
    id_toalha = fields.Int(required=True, load_only=True)
    funcionarioId = fields.Int(attribute="id_funcionario", dump_only=True)
    funcionarioNome = fields.Method("obter_funcionario")
    nadadorId = fields.Int(attribute="id_nadador", dump_only=True)
    nadadorNome = fields.Method("obter_nadador")
    toalhaId = fields.Int(attribute="id_toalha", dump_only=True)
    toalhaCodigo = fields.Method("obter_toalha")

    def obter_tipo(self, obj):
        return "Devolução" if obj.data_hora_devolucao else "Retirada"
    def obter_funcionario(self, obj): return obj.funcionario.usuario.nome
    def obter_nadador(self, obj): return obj.nadador.usuario.nome
    def obter_toalha(self, obj): return obj.toalha.codigo
