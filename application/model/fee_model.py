from application.model import *


class fee_table(db.Model):
    __tablename__ = 'fee_table'
    fee_id = db.Column(db.Integer,primary_key=True,nullable=False)
    year_wise = db.Column(db.Integer)
    min_fee = db.Column(db.Integer,nullable=False)
    max_fee = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    course_id = db.Column(db.Integer,db.ForeignKey('course_table.course_id'),nullable=False)
    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)
    # university_id = db.Column(db.Integer,db.ForeignKey('university_table.university_id'),nullable=True)


class fee_tableschema(ma.Schema):
    fee_id = fields.Integer()
    year_wise = fields.Integer()
    min_fee = fields.Integer()
    max_fee = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()
    
    course_id = fields.Integer()
    college_id = fields.Integer()
    # university_id = fields.Integer()