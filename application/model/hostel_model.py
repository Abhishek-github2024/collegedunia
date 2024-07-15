from application.model import *


class hostel_table(db.Model):
    __tablename__ = 'hostel_table'
    hostel_id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(255))
    min_fee = db.Column(db.Integer)
    max_fee = db.Column(db.Integer)
    created_at = db.Column(db.DateTime,nullable=False)
    updated_at = db.Column(db.DateTime,nullable=False)
    status = db.Column(db.String(50),nullable=False)

    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)
   


class hostel_tableschema(ma.Schema):
    hostel_id = fields.Integer()
    name = fields.String()
    min_fee = fields.Integer()
    max_fee = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()

    college_id = fields.Integer()