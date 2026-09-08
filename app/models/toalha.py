from app import db


class Toalha(db.Model):
    __tablename__ = "toalha"

    id_toalha = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False, unique=True)
    status = db.Column(db.String(20), nullable=False, default="disponivel")

    movimentacoes = db.relationship(
        "Movimentacao",
        back_populates="toalha"
    )