from app.database.db import db


class Treino(db.Model):

    __tablename__ = "treinos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    descricao = db.Column(
        db.Text
    )

    categoria = db.Column(
        db.String(100)
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    usuario = db.relationship(
        "Usuario",
        backref="treinos"
    )

    def __repr__(self):

        return f"<Treino {self.nome}>"