from application.model import *


class gallery_table(db.Model):
    __tablename__='gallery_table'
    gallery_id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(255))
    photo = db.Column(db.LargeBinary)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)
    university_id = db.Column(db.Integer,db.ForeignKey('university_table.university_id'),nullable=False)



class gallery_tableschema(ma.Schema):
    class Meta:
        fields = ("gallery_id","name","photo","college_id","university_id")
    # gallery_id = fields.Integer()
    # name = fields.String()
    # photos = fields.LargeBinary()

    # college_id = fields.Integer()
    # university_id = fields.Integer()