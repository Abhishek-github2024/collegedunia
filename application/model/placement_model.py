from application.model import *

class placement_table(db.Model):
    __tablename__='placement_table'
    placement_id = db.Column(db.Integer,primary_key=True,nullable=False)
    year = db.Column(db.Integer,nullable=True)
    company = db.Column(db.String(255))
    student_no = db.Column(db.Integer)
    avg = db.Column(db.Float,nullable=True)
    high = db.Column(db.Float,nullable=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    # course_id = db.Column(db.Integer,db.ForeignKey('course_table.course_id'),nullable=True)
    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)



class placement_tableschema(ma.Schema):
    # class Meta:
        # fields = ("placement_id","year","company","avg","high","status","college_id")
    placement_id = fields.Integer()
    year = fields.Integer()
    company = fields.String()
    student_no = fields.Integer()
    avg = fields.Float()
    high = fields.Float()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()
    
    # course_id = fields.Integer()
    college_id = fields.Integer()
