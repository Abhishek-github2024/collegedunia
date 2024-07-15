from application.model import *

class faculty_table(db.Model):
    __tablename__='faculty_table'
    faculty_id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(100))
    department = db.Column(db.String(100))
    qualification = db.Column(db.String(100))
    email = db.Column(db.String(255),nullable=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(50),nullable=True)

    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)
    university_id = db.Column(db.Integer,db.ForeignKey('university_table.university_id'),nullable=False)



class faculty_tableschema(ma.Schema):
    faculty_id = fields.Integer()
    name = fields.String()
    department = fields.String()
    qualification = fields.String()
    email = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()

    college_id = fields.Integer()
    university_id = fields.Integer()  