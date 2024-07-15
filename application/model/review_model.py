from application.model import*


class review_table(db.Model):
    __tablename__='review_table'
    review_id = db.Column(db.Integer,primary_key=True,nullable=False)
    like = db.Column(db.String(255),nullable=False)
    dislike = db.Column(db.String(255))
    course_curriculum_overview  = db.Column(db.String(255),nullable=False)
    internship_opportunities = db.Column(db.String(255),nullable=False)
    placement_experience = db.Column(db.String(255),nullable=False)
    loan_scholarship_provisions = db.Column(db.String(255),nullable=False)
    campus_life = db.Column(db.String(255),nullable=False)
    hostel_facilities = db.Column(db.String(255),nullable=False)
    admission = db.Column(db.String(255),nullable=False)
    classroom_size = db.Column(db.Integer,nullable=True)
    fee = db.Column(db.Integer,nullable=False)
    placement = db.Column(db.Integer,nullable=True)
    college = db.Column(db.Integer,nullable=True)
    internship = db.Column(db.Integer,nullable=True)
    course = db.Column(db.Integer,nullable=True)
    hostel = db.Column(db.Integer,nullable=True)
    campus = db.Column(db.Integer,nullable=True)
    created_at = db.Column(db.DateTime,nullable=False)
    updated_at = db.Column(db.DateTime,nullable=False)
    status = db.Column(db.String(50),nullable=False)

    college_id = db.Column(db.Integer,db.ForeignKey('college_table.college_id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user_table.user_id'),nullable=False)



class review_tableschema(ma.Schema):
    review_id = fields.Integer()
    like = fields.String()
    dislike = fields.String()
    course_curriculum_overview  = fields.String()
    internship_opportunities = fields.String()
    placement_experience = fields.String()
    loan_scholarship_provisions = fields.String()
    campus_life = fields.String()
    hostel_facilities = fields.String()
    admission = fields.String()
    classroom_size = fields.Integer()
    fee = fields.Integer()
    placement = fields.Integer()
    college = fields.Integer()
    internship = fields.Integer()
    course = fields.Integer()
    hostel = fields.Integer()
    campus = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    status = fields.String()

    college_id = fields.Integer()
    user_id = fields.Integer()
