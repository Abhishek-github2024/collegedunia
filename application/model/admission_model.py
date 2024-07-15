from application.model import *


class admission_table(db.Model):
    __tablename__ = 'admission_table'
    admission_id = db.Column(db.Integer,primary_key=True,nullable=False)
    about = db.Column(db.String(255))
    seats = db.Column(db.Integer,nullable=True)
    course = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    eligibility = db.Column(db.String(255),nullable=True)
    year = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)


class admission_tableschema(ma.Schema):
    admission_id = fields.Integer()
    about = fields.String()
    seats = fields.Integer()
    course = fields.String()
    branch = fields.String()
    eligibility = fields.String()
    year = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()

    college_id = fields.Integer()