from marshmallow import Schema, fields


class NadadorSchema(Schema):
    id = fields.Int(attribute="id_nadador", dump_only=True)
    nome = fields.Method("obter_nome")
    cpf = fields.Method("obter_cpf")
    telefone = fields.Method("obter_telefone")
    email = fields.Method("obter_email")

    def obter_nome(self, obj): return obj.usuario.nome
    def obter_cpf(self, obj): return obj.usuario.cpf
    def obter_telefone(self, obj): return obj.usuario.telefone
    def obter_email(self, obj): return obj.usuario.email
