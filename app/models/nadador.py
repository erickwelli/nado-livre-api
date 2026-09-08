from app import db


class Nadador(db.Model):
    __tablename__ = "nadador"

    id_nadador = db.Column(
        db.Integer,
        db.ForeignKey("usuario.id_usuario"),
        primary_key=True
    )

    usuario = db.relationship(
        "Usuario",
        back_populates="nadador"
    )

    movimentacoes = db.relationship(
        "Movimentacao",
        back_populates="nadador"
    )