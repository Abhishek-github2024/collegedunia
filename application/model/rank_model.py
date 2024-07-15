from application.model import *

class rank_table(db.Model):
    __tablename__='rank_table'
    rank_id = db.Column(db.Integer,primary_key=True,nullable=False)
    rank = db.Column(db.Integer,nullable=False)
    course = db.Column(db.String(100))
    by = db.Column(db.String(100))
    year = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)
    university_id = db.Column(db.Integer,db.ForeignKey('university_table.university_id'),nullable=False)



class rank_tableschema(ma.Schema):
    rank_id = fields.Integer()
    rank = fields.Integer()
    course = fields.String()
    by = fields.String()
    year = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()

    college_id = fields.Integer()
    university_id = fields.Integer()

