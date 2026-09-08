from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY",
        "chave-desenvolvimento-nado-livre"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nado_livre.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes import (
        usuarios_bp,
        funcionarios_bp,
        nadadores_bp,
        toalhas_bp,
        movimentacoes_bp
    )

    app.register_blueprint(usuarios_bp)
    app.register_blueprint(funcionarios_bp)
    app.register_blueprint(nadadores_bp)
    app.register_blueprint(toalhas_bp)
    app.register_blueprint(movimentacoes_bp)

    from app.models import (
        Usuario,
        Funcionario,
        Nadador,
        Toalha,
        Movimentacao
    )

    with app.app_context():
        db.create_all()

    @app.route("/")
    def inicio():
        return {
            "mensagem": "Nado Livre API funcionando!"
        }

    return app