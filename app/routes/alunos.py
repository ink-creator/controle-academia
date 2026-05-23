from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from app.database.db import db

alunos_bp = Blueprint(
    "alunos",
    __name__,
    url_prefix="/alunos"
)


@alunos_bp.route("/perfil", methods=["GET", "POST"])
@login_required
def perfil():

    if request.method == "POST":

        current_user.nome = request.form.get("nome")
        current_user.idade = request.form.get("idade")
        current_user.peso = request.form.get("peso")
        current_user.altura = request.form.get("altura")
        current_user.objetivo = request.form.get("objetivo")

        db.session.commit()

        flash(
            "Perfil atualizado!",
            "success"
        )

        return redirect(
            url_for("alunos.perfil")
        )

    return render_template(
        "alunos/perfil.html"
    )