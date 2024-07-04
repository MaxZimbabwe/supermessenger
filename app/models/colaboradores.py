from datetime import datetime
from ..extension import db

class Colaboradores(db.Model):
    __tablename__ = 'colaboradores'

    idcolaboradores = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuarios.idusuario'))
    idusuariocolaborador = db.Column(db.Integer, db.ForeignKey('usuarios.idusuario'))
    status = db.Column(db.Integer, nullable=False)
    excluido = db.Column(db.String(1), nullable=False)
    createad_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    usuario = db.relationship('Usuarios', foreign_keys=[idusuario], backref='colaboradores')
    colaborador = db.relationship('Usuarios', foreign_keys=[idusuariocolaborador], backref='colaborador')

    def __init__(self, idusuario, idusuariocolaborador):
        self.idusuario = idusuario
        self.idusuariocolaborador = idusuariocolaborador

    def __repr__(self):
        return f'<Colaboradores {self.idusuario} - {self.idcolaboradores}>'