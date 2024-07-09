from datetime import datetime
from ..extension import db

class ProductsModeration(db.Model):
    __tablename__ = 'produtos_moderacao'

    idproduto = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(db.Integer, db.ForeignKey('usuario.idusuario'), nullable=False)
    idproexterno = db.Column(db.String(255), nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    ativo = db.Column(db.String(1), nullable=False)
    datacadastro = db.Column(db.DateTime, default=datetime.utcnow)
    datamodicacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, idusuario, idproduto, idproexterno,titulo, descricao):
        self.idusuario = idusuario
        self.idproduto = idproduto
        self.idproexterno = idproexterno
        self.titulo = titulo
        self.descricao = descricao

    def __repr__(self):
        return f'<Produtos {self.idproduto}>'
