from app import db


class Funcionario(db.Model):
    __tablename__ = "funcionario"

    id_funcionario = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id_usuario"),
        primary_key=True
    )

    usuario = db.relationship(
        "Usuario",
        back_populates="funcionario"
    )

    movimentacoes = db.relationship(
        "Movimentacao",
        back_populates="funcionario"
    )