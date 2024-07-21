from datetime import datetime
from ..extension import db

class Logs(db.Model):
    __tablename__ = 'logs'

    idlogs = db.Column(db.Integer, primary_key=True)    
    log = db.Column(db.String(255), nullable=False)    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, log):
        self.log = log

    def __repr__(self):
        return f'<Logs {self.idlogs}>'
