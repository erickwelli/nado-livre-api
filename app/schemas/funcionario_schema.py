from marshmallow import Schema, fields


class FuncionarioSchema(Schema):
    id_funcionario = fields.Int(dump_only=True)

    nome = fields.Str(attribute="usuario.nome", dump_only=True)
    cpf = fields.Str(attribute="usuario.cpf", dump_only=True)
    telefone = fields.Str(attribute="usuario.telefone", dump_only=True)
    email = fields.Email(attribute="usuario.email", dump_only=True)