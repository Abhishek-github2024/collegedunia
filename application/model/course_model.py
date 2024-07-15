from application.model import *

class course_table(db.Model):
    __tablename__= 'course_table'
    course_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    eligibility = db.Column(db.String(255))
    application_begain = db.Column(db.DateTime)
    application_end = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime,nullable=False)
    updated_at = db.Column(db.DateTime,nullable=False)
    status = db.Column(db.String(50),nullable=False)

    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university_table.university_id'),nullable=False)

    # placements = db.relationship('placement_table',backref='course_table',lazy=True)
    fees = db.relationship('fee_table',backref='course_table',lazy=True)


class course_tableschema(ma.Schema):
    course_id = fields.Integer()
    name = fields.String()
    duration = fields.Integer()
    eligibility = fields.String()
    application_begain = fields.DateTime()
    application_end = fields.DateTime()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()

    college_id = fields.Integer()
    university_id = fields.Integer()