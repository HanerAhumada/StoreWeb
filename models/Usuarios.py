from utils.db import db, BaseModelData
from sqlalchemy import Enum

categoria_enum = Enum('Admin', 'Cliente', name='rol_enum')

class Usuarios(db.Model, BaseModelData):
    __tablename__ = 'Usuarios'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=True)
    direccion = db.Column(db.String(50), nullable=True)
    telefono = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    rol = db.Column(categoria_enum, nullable=False)

    def __repr__(self):
        return '<Usuario %r>' % self.id

    def __init__(self, **datos):
        self.nombre = datos.get('nombre')
        self.apellido = datos.get('apellido')
        self.direccion = datos.get('direccion')
        self.telefono = datos.get('telefono')
        self.email = datos.get('email')
        self.password = datos.get('password')
        self.estado = datos.get('estado')


