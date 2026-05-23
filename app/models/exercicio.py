from app.database.db import db


class Exercicio(db.Model):

    __tablename__ = "exercicios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    series = db.Column(
        db.String(20)
    )

    repeticoes = db.Column(
        db.String(20)
    )

    descanso = db.Column(
        db.String(20)
    )

    carga = db.Column(
        db.String(20)
    )

    observacoes = db.Column(
        db.Text
    )

    treino_id = db.Column(
        db.Integer,
        db.ForeignKey("treinos.id"),
        nullable=False
    )

    treino = db.relationship(
        "Treino",
        backref="exercicios"
    )

    def __repr__(self):

        return f"<Exercicio {self.nome}>"