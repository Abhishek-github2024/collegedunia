from application.model import *


class cutoff_table(db.Model):
    __tablename__='cutoff_table'
    cutoff_id = db.Column(db.Integer,primary_key=True,nullable=False)
    comments = db.Column(db.String(255))
    test = db.Column(db.String(50))
    year = db.Column(db.Integer)
    course = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    quota = db.Column(db.String(100))
    open = db.Column(db.Integer)
    close = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)



class cutoff_tableschema(ma.Schema):
    cutoff_id = fields.Integer()
    comments = fields.String()
    test = fields.String()
    year = fields.Integer()
    course = fields.String()
    branch = fields.String()
    quota = fields.String()
    open = fields.Integer()
    close = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()
    
    college_id = fields.Integer()

    