from marshmallow import Schema, fields


class NadadorSchema(Schema):
    id_nadador = fields.Int(dump_only=True)