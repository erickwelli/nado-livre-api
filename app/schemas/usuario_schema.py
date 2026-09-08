from marshmallow import Schema, fields


class UsuarioSchema(Schema):
    id_usuario = fields.Int(dump_only=True)

    nome = fields.Str(required=True)
    cpf = fields.Str(required=True)
    telefone = fields.Str(required=True)
    email = fields.Email(required=True)