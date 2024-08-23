from datetime import datetime
from ..extension import db

class Integracao(db.Model):
    __tablename__ = 'integracoes'

    idintegracoes = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuarios.idusuario'), primary_key=True)
    idtipointegracao = db.Column(db.Integer, primary_key=True)
    apelido = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(255), nullable=False)
    permitido = db.Column(db.String(1), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Integracao {self.id}>'
