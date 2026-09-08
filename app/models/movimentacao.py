from app import db
from datetime import datetime


class Movimentacao(db.Model):
    __tablename__ = "movimentacao"

    id_movimentacao = db.Column(db.Integer, primary_key=True)

    data_hora_retirada = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now
    )

    data_hora_devolucao = db.Column(
        db.DateTime,
        nullable=True
    )

    id_funcionario = db.Column(
        db.Integer,
        db.ForeignKey("funcionario.id_funcionario"),
        nullable=False
    )

    id_nadador = db.Column(
        db.Integer,
        db.ForeignKey("nadador.id_nadador"),
        nullable=False
    )

    id_toalha = db.Column(
        db.Integer,
        db.ForeignKey("toalha.id_toalha"),
        nullable=False
    )

    funcionario = db.relationship(
        "Funcionario",
        back_populates="movimentacoes"
    )

    nadador = db.relationship(
        "Nadador",
        back_populates="movimentacoes"
    )

    toalha = db.relationship(
        "Toalha",
        back_populates="movimentacoes"
    )