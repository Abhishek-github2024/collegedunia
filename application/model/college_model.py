from application.model import *
from application.model.university_model import *
# import flask_whooshalchemy as wa

class college_table(db.Model):
    __tablename__ = 'college_table'
    # __searchable__ = ['name']
    college_id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(100),nullable=False)
    about = db.Column(db.String(255),nullable=False)
    city = db.Column(db.String(100),nullable=False)
    state = db.Column(db.String(50),nullable=False)
    type = db.Column(db.String(100),nullable=False)
    estd = db.Column(db.Integer,nullable=False)
    aicte = db.Column(db.String(50))
    mhrd = db.Column(db.String(50))
    created_at = db.Column(db.DateTime,nullable=False)
    updated_at = db.Column(db.DateTime,nullable=False)
    status = db.Column(db.String(50),nullable=False)

    university_id = db.Column(db.Integer,db.ForeignKey('university_table.university_id'),nullable=False)
    # info_id = db.Column(db.Integer,db.ForeignKey('info_table.info_id'),nullable=False)
   


    courses = db.relationship('course_table',backref='college_table',lazy=True)
    placements = db.relationship('placement_table',backref='college_table',lazy=True)
    # fees = db.relationship('fee_table',backref='college_table',lazy=True)
    hostels = db.relationship('hostel_table',backref='college_table',lazy=True)
    gallarys = db.relationship('gallery_table',backref='college_table',lazy=True)
    infos = db.relationship('info_table',backref='college_table',lazy=True)
    cutoffs = db.relationship('cutoff_table',backref='college_table',lazy=True)
    reviews = db.relationship('review_table',backref='college_table',lazy=True)
    admissions = db.relationship('admission_table',backref='college_table',lazy=True)
    questions = db.relationship('question_table',backref='college_table',lazy=True)
    ranks = db.relationship('rank_table',backref='college_table',lazy=True)
    news = db.relationship('news_table',backref='college_table',lazy=True)
    answers = db.relationship('answer_table',backref='college_table',lazy=True)

# wa.whoosh_index(app,college_table)

class college_tableschema(ma.Schema):
    college_id = fields.Integer()
    name = fields.String()
    about = fields.String()
    city = fields.String()
    state = fields.String()
    type = fields.String()
    estd = fields.Integer()
    aicte = fields.String()
    mhrd = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()

    university_id = fields.Integer()
    # info_id = fields.Integer
