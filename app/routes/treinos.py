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

from app.models.treino import Treino

treinos_bp = Blueprint(
    "treinos",
    __name__,
    url_prefix="/treinos"
)

# ====================================
# LISTAR TREINOS
# ====================================
@treinos_bp.route("/")
@login_required
def lista():

    treinos = Treino.query.filter_by(
        usuario_id=current_user.id
    ).all()

    return render_template(
        "treinos/lista.html",
        treinos=treinos
    )


# ====================================
# CRIAR TREINO
# ====================================
@treinos_bp.route("/criar", methods=["GET", "POST"])
@login_required
def criar():

    if request.method == "POST":

        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        categoria = request.form.get("categoria")

        novo_treino = Treino(
            nome=nome,
            descricao=descricao,
            categoria=categoria,
            usuario_id=current_user.id
        )

        db.session.add(novo_treino)

        db.session.commit()

        flash(
            "Treino criado com sucesso!",
            "success"
        )

        return redirect(
            url_for("treinos.lista")
        )

    return render_template(
        "treinos/criar.html"
    )


# ====================================
# EDITAR TREINO
# ====================================
@treinos_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):

    treino = Treino.query.filter_by(
        id=id,
        usuario_id=current_user.id
    ).first_or_404()

    if request.method == "POST":

        treino.nome = request.form.get("nome")
        treino.descricao = request.form.get("descricao")
        treino.categoria = request.form.get("categoria")

        db.session.commit()

        flash(
            "Treino atualizado!",
            "success"
        )

        return redirect(
            url_for("treinos.lista")
        )

    return render_template(
        "treinos/editar.html",
        treino=treino
    )


# ====================================
# EXCLUIR TREINO
# ====================================
@treinos_bp.route("/excluir/<int:id>")
@login_required
def excluir(id):

    treino = Treino.query.filter_by(
        id=id,
        usuario_id=current_user.id
    ).first_or_404()

    db.session.delete(treino)

    db.session.commit()

    flash(
        "Treino removido com sucesso!",
        "info"
    )

    return redirect(
        url_for("treinos.lista")
    )