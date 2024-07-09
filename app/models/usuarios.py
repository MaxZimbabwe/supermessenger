from datetime import datetime
from ..extension import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    idusuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    sobrenome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    responsavel = db.relationship('Colaboradores', foreign_keys='Colaboradores.idusuario', back_populates='colaborando')
    colaborador = db.relationship('Colaboradores', foreign_keys='Colaboradores.idusuariocolaborador', back_populates='colaboradores')
    moderacoes = db.relationship('Moderacao', uselist=True, back_populates='usuario')

    def __init__(self, idusuario, idproduto, titulo, descricao):
        self.idusuario = idusuario
        self.idproduto = idproduto
        self.titulo = titulo
        self.descricao = descricao

    def __repr__(self):
        return f'<Usuario {self.idusuario}>'
