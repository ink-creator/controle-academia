from flask import Flask, redirect, url_for

from flask_login import LoginManager

from config import Config

from app.database.db import db

from flask_login import current_user

from app.models.usuario import Usuario
from app.models.plano import Plano
from app.models.treino import Treino
from app.models.exercicio import Exercicio


login_manager = LoginManager()

login_manager.login_view = "auth.login"


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    login_manager.init_app(app)

    # =========================
    # USER LOADER
    # =========================
    @login_manager.user_loader
    def load_user(user_id):

        return Usuario.query.get(
            int(user_id)
        )

    # =========================
    # BLUEPRINTS
    # =========================
    from app.routes.auth import auth_bp
    from app.routes.treinos import treinos_bp
    from app.routes.planos import planos_bp
    from app.routes.exercicios import exercicios_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(treinos_bp)
    app.register_blueprint(planos_bp)
    app.register_blueprint(exercicios_bp)

    # =========================
    # HOME
    # =========================
    @app.route("/")
    def home():

        if current_user.is_authenticated:
            return redirect(url_for("auth.dashboard"))

        return redirect(url_for("auth.login"))

    # =========================
    # BANCO
    # =========================
    with app.app_context():

        db.create_all()

        # =========================
        # PLANOS PADRÃO
        # =========================
        if not Plano.query.first():

            planos = [

                Plano(
                    nome="Mensal",
                    preco=89.90,
                    descricao="""
                    Acesso completo à academia,
                    musculação e cardio.
                    """,
                    duracao_meses=1
                ),

                Plano(
                    nome="Trimestral",
                    preco=79.90,
                    descricao="""
                    Melhor custo-benefício
                    para manter consistência.
                    """,
                    duracao_meses=3
                ),

                Plano(
                    nome="Anual",
                    preco=59.90,
                    descricao="""
                    Plano premium com o melhor valor.
                    """,
                    duracao_meses=12
                )

            ]

            db.session.add_all(planos)

            db.session.commit()

    return app