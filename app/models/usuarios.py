from datetime import datetime
from ..extension import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    idusuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    sobrenome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    createad_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, idusuario, idproduto, titulo, descricao):
        self.idusuario = idusuario
        self.idproduto = idproduto
        self.titulo = titulo
        self.descricao = descricao

    def __repr__(self):
        return f'<Usuario {self.idusuario} - {self.email}>'
