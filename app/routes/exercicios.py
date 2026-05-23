from flask import Blueprint, render_template

from flask_login import login_required

exercicios_bp = Blueprint(
    "exercicios",
    __name__,
    url_prefix="/exercicios"
)


@exercicios_bp.route("/")
@login_required
def lista():

    return render_template(
        "exercicios/lista.html"
    )