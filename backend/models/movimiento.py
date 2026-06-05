from app import db

class Movimiento(db.Model):

    __tablename__ = "movimientos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    tipo = db.Column(
        db.String(20),
        nullable=False
    )

    monto = db.Column(
        db.Float,
        nullable=False
    )

    descripcion = db.Column(
        db.String(255)
    )

    fecha = db.Column(
        db.Date
    )

    usuario_id = db.Column(
        db.Integer,
        nullable=False
    )
