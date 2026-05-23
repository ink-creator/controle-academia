from app.database.db import db


class Plano(db.Model):

    __tablename__ = "planos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    preco = db.Column(
        db.Float,
        nullable=False
    )

    descricao = db.Column(
        db.Text
    )

    duracao_meses = db.Column(
        db.Integer,
        nullable=False
    )

    ativo = db.Column(
        db.Boolean,
        default=True
    )

    usuarios = db.relationship(
        "Usuario",
        backref="plano",
        lazy=True
    )

    def __repr__(self):
        return f"<Plano {self.nome}>"