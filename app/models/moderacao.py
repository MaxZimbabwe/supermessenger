from datetime import datetime
from ..extension import db

class Moderacao(db.Model):
    __tablename__ = 'moderacao'

    id = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuarios.idusuario'), nullable=False)
    idpergunta= db.Column(db.String(255), nullable=False)
    idresource= db.Column(db.String(255), nullable=False)
    idsubject = db.Column(db.String(255), nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    questao = db.Column(db.String(255), nullable=False)
    resposta = db.Column(db.String(255), nullable=False)
    idstatus = db.Column(db.Integer, nullable=False)
    datacadastro = db.Column(db.DateTime, default=datetime.utcnow)
    datamodicacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    status = db.relationship('ModeracaoStatus', uselist=False, back_populates='moderacao')
    usuario = db.relationship('Usuarios', uselist=False, back_populates='moderacoes')

    def __init__(self, idusuario, idpergunta, idresource, idsubject, titulo, questao, resposta, idstatus):
        self.idusuario = idusuario
        self.titulo = titulo
        self.questao = questao
        self.resposta = resposta
        self.idstatus = idstatus
        self.idsubject = idsubject
        self.idpergunta = idpergunta
        self.idresource = idresource

    def __repr__(self):
        return f'<Moderacao {self.id}>'
