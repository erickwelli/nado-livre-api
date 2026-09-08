from marshmallow import Schema, fields


class FuncionarioSchema(Schema):
    id_funcionario = fields.Int(dump_only=True)