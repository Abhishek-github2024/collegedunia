from application.model import *

class info_table(db.Model):
    __tablename__='info_table'
    info_id = db.Column(db.Integer,primary_key=True,nullable=False)
    about = db.Column(db.String(255))


    admin_id = db.Column(db.Integer,db.ForeignKey('admin_table.admin_id'),nullable=False)
    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)

    # colleges = db.relationship('college_table',backref='info_table',lazy=True)



class info_tableschema(ma.Schema):
    info_id = fields.Integer
    about = fields.String()


    admin_id = fields.Integer
    college_id = fields.Integer