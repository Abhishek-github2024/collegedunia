from application.model import *


class admin_table(db.Model):
    admin_id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    jti = db.Column(db.String(255))
    
    infos = db.relationship('info_table',backref='admin_table',lazy=True)
    

class admin_tableschema(ma.Schema):
    admin_id = fields.Integer
    name = fields.String()
    email = fields.String()
    password = fields.String()
    jti = fields.String()
    