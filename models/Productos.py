from utils.db import db, BaseModelData
from sqlalchemy import Enum

# Definición correcta de la enumeración
categoria_enum = Enum('Web', 'Blog', 'StoreWeb', 'CustomWeb', 'Portfolio', name='categoria_enum')

class Producto(db.Model, BaseModelData):
    __tablename__ = 'Producto'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    categoria = db.Column(categoria_enum, nullable=False)  # Usar la enumeración aquí

    def __repr__(self):
        return '<Producto %r>' % self.nombre

    def __init__(self, **datos):
        self.nombre = datos.get('nombre')
        self.precio = datos.get('precio')
        self.descripcion = datos.get('descripcion')
        self.estado = datos.get('estado')
        self.codigo = datos.get('codigo')
        self.categoria = datos.get('categoria')  # Inicializar la categoría correctamente
