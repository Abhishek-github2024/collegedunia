from application.model import *


class temp(db.Model):
    __tablename__='temp'
    id = db.Column(db.Integer,primary_key=True)
    image = db.Column(db.String())


class tempschema(ma.Schema):
    id = fields.Integer()
    image = fields.String()
