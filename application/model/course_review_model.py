from application.model import *

class course_review_table(db.Model):
    __tablename__= 'course_review_table'
    course_review_id = db.Column(db.Integer,primary_key=True,nullable=False) 
    name = db.Column(db.String(100),nullable=False)
    min_duration = db.Column(db.Integer())
    max_duration = db.Column(db.Integer())
    min_fee = db.Column(db.Integer(),nullable=False)
    max_fee = db.Column(db.Integer(),nullable=False)

    category_id = db.Column(db.String(100),nullable=False)


class course_review_tableschema(ma.Schema):
    course_review_id = fields.Integer()
    name = fields.String()
    
