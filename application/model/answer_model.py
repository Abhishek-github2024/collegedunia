from application.model import *

class answer_table(db.Model):
    __tablename__='answer_table'
    answer_id = db.Column(db.Integer,primary_key=True,nullable=False)
    answer = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    question_id = db.Column(db.Integer,db.ForeignKey('question_table.question_id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user_table.user_id'),nullable=False)
    # college_id = db.Column(db.Integer)
    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)



class answer_tableschema(ma.Schema):
    answer_id = fields.Integer()
    answer = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()

    question_id = fields.Integer()
    user_id = fields.Integer()
    college_id = fields.Integer()
