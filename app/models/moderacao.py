from datetime import datetime
from ..extension import db

class Moderacao(db.Model):
    __tablename__ = 'moderacao'

    id = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, nullable=False)
    questao = db.Column(db.String(255), nullable=False)
    resposta = db.Column(db.String(255), nullable=False)
    idstatus = db.Column(db.Integer, db.ForeignKey('moderacao_status.idstatus'), nullable=False)
    datacadastro = db.Column(db.DateTime, default=datetime.utcnow)
    datamodicacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    status = db.relationship('ModeracaoStatus', backref='moderacoes')

    def __init__(self, idusuario, questao, resposta, idstatus):
        self.idusuario = idusuario
        self.questao = questao
        self.resposta = resposta
        self.idstatus = idstatus

    def __repr__(self):
        return f'<Moderacao {self.id} - {self.questao}>'
