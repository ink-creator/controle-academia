from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from app.database.db import db

from app.models.plano import Plano

planos_bp = Blueprint(
    "planos",
    __name__,
    url_prefix="/planos"
)


# ====================================
# LISTAR PLANOS
# ====================================
@planos_bp.route("/")
def lista():

    planos = Plano.query.filter_by(
        ativo=True
    ).all()

    return render_template(
        "planos/lista.html",
        planos=planos
    )


# ====================================
# ASSINAR PLANO
# ====================================
@planos_bp.route("/assinar/<int:id>")
@login_required
def assinar(id):

    plano = Plano.query.get_or_404(id)

    current_user.plano_id = plano.id

    db.session.commit()

    flash(
        f"Plano {plano.nome} assinado com sucesso!",
        "success"
    )

    return redirect(
        url_for("auth.dashboard")
    )