from application.model import *

class university_table(db.Model):
    __tablename__ = 'university_table'
    university_id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(255))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    pincode = db.Column(db.Integer)
    aicte = db.Column(db.String(50))
    ugc = db.Column(db.String(50))
    mhrd = db.Column(db.String(50))
    estd= db.Column(db.Integer)
    type = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(255))

    colleges = db.relationship('college_table',backref='university_table',lazy=True)
    course = db.relationship('course_table',backref='university_table',lazy=True)
    faculty = db.relationship('faculty_table',backref='university_table',lazy=True)
    gallery = db.relationship('gallery_table',backref='university_table',lazy=True)
    rank = db.relationship('rank_table',backref='university_table',lazy=True)
    # fee = db.relationship('fee_table',backref='university_table',lazy=True)
    


class university_tableschema(ma.Schema):
    university_id = fields.Integer()
    name = fields.String()
    city = fields.String()
    state = fields.String()
    pincode = fields.Integer()
    aicte = fields.String()
    ugc = fields.String()
    mhrd = fields.String()
    estd= fields.Integer()
    type = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()