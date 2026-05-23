from flask import Flask

from flask_login import LoginManager

from config import Config

from app.database.db import db

from flask import Flask, redirect, url_for

login_manager = LoginManager()

login_manager.login_view = "auth.login"

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    login_manager.init_app(app)

    from app.models.usuario import Usuario

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    from app.routes.auth import auth_bp

    app.register_blueprint(auth_bp)

    @app.route("/")
    def home():
        return redirect(url_for("auth.login"))

    with app.app_context():
        db.create_all()

    return app