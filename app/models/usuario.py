from app import db


class Usuario(db.Model):
    __tablename__ = "usuario"

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    funcionario = db.relationship(
        "Funcionario",
        back_populates="usuario",
        uselist=False
    )

    nadador = db.relationship(
        "Nadador",
        back_populates="usuario",
        uselist=False
    )