from application.model import *


class question_table(db.Model):
    __tablename__='question_table'
    question_id = db.Column(db.Integer,primary_key=True,nullable=False)
    question = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    
    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user_table.user_id'),nullable=False)

    answer = db.relationship('answer_table',backref='question_table',lazy=True)


class question_tableschema(ma.Schema):
    question_id = fields.Integer()
    question = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()

    college_id = fields.Integer()
    user_id = fields.Integer()