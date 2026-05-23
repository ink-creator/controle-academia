from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from app.database.db import db

from app.models.usuario import Usuario

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)

# =========================
# LOGIN
# =========================
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("auth.dashboard"))

    if request.method == "POST":

        email = request.form.get("email")
        senha = request.form.get("senha")

        usuario = Usuario.query.filter_by(
            email=email
        ).first()

        if usuario and usuario.verificar_senha(senha):

            login_user(usuario)

            flash(
                "Login realizado com sucesso!",
                "success"
            )

            return redirect(
                url_for("auth.dashboard")
            )

        flash(
            "E-mail ou senha inválidos.",
            "danger"
        )

    return render_template("auth/login.html")

# =========================
# CADASTRO
# =========================
@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        usuario_existente = Usuario.query.filter_by(
            email=email
        ).first()

        if usuario_existente:

            flash(
                "Este e-mail já está cadastrado.",
                "warning"
            )

            return redirect(
                url_for("auth.cadastro")
            )

        # SENHA FORTE
        if len(senha) < 8:

            flash(
                "A senha precisa ter pelo menos 8 caracteres.",
                "danger"
            )

            return redirect(
                url_for("auth.cadastro")
            )

        novo_usuario = Usuario(
            nome=nome,
            email=email
        )

        novo_usuario.definir_senha(senha)

        db.session.add(novo_usuario)

        db.session.commit()

        flash(
            "Conta criada com sucesso!",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template("auth/cadastro.html")

# =========================
# LOGOUT
# =========================
@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Você saiu da conta.",
        "info"
    )

    return redirect(
        url_for("auth.login")
    )

# =========================
# DASHBOARD
# =========================
@auth_bp.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "alunos/dashboard.html"
    )