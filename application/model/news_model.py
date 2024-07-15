from application.model import *


class news_table(db.Model):
    __tablename__='news_table'
    news_id = db.Column(db.Integer,primary_key=True,nullable=False)
    tagline = db.Column(db.String(150),nullable=False)
    image = db.Column(db.String(),nullable=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(50))
    content = db.Column(db.String(255))
    name = db.Column(db.String(50),nullable=False)
    url = db.Column(db.String(150))
    
    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)


class news_tableschema(ma.Schema):
    news_id = fields.Integer()
    tagline = fields.String()
    image = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()
    content = fields.String()
    name = fields.String()
    url = fields.String()
    
    college_id = fields.Integer() 