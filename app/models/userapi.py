from datetime import datetime
from ..extension import db

class Userapp(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    idusuarioapp = db.Column(db.Integer, db.ForeignKey('usuario.idusuario'), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    fcm_token = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Userapp {self.id} - {self.email}>'
