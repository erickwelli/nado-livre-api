from marshmallow import Schema, fields


class ToalhaSchema(Schema):
    id_toalha = fields.Int(dump_only=True)

    codigo = fields.Str(required=True)

    status = fields.Str(
        dump_only=True
    )