from marshmallow import Schema, fields


class ToalhaSchema(Schema):
    id = fields.Int(attribute="id_toalha", dump_only=True)
    codigo = fields.Str(required=True)
    status = fields.Method("obter_status")

    def obter_status(self, objeto):
        return "Em uso" if objeto.status == "em_uso" else "Disponível"
