from ..extension import db

class ModeracaoStatus(db.Model):
    __tablename__ = 'moderacao_status'

    idstatus = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)

    def __init__(self, descricao):
        self.descricao = descricao

    def __repr__(self):
        return f'<ModeracaoStatus {self.descricao}>'