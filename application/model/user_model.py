from application.model import *



class user_table(db.Model):
    __tablename__='user_table'
    user_id = db.Column(db.Integer,primary_key=True,nullable=False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    mobile_no = db.Column(db.Integer)
    city = db.Column(db.String(100))
    intrestedin_course = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    link = db.Column(db.String(150))
    tenth_board = db.Column(db.String(100))
    tenthpass_year = db.Column(db.Integer)
    tenth_percentage = db.Column(db.Float)
    tenth_schoolname = db.Column(db.String(150))
    twelfth_board = db.Column(db.String(100))  
    twelfthpass_year = db.Column(db.Integer)
    twelfth_percentage = db.Column(db.Float)
    twelfth_schoolname = db.Column(db.String(150))
    specializationin = db.Column(db.String(50))
    otp = db.Column(db.String(255))
    is_active = db.Column(db.Integer)
    jti = db.Column(db.String(255))


    answer = db.relationship('answer_table',backref='user_table',lazy=True)
    question = db.relationship('question_table',backref='user_table',lazy=True)



class user_tableschema(ma.Schema):
    user_id = fields.Integer()
    name = fields.String()
    email = fields.String()
    password = fields.String()
    mobile_no = fields.Integer()
    city = fields.String()
    intrestedin_course = fields.String()
    gender = fields.String()
    link = fields.String()
    tenth_board = fields.String()
    tenthpass_year = fields.Integer()
    tenth_percentage = fields.Float()
    tenth_schoolname = fields.String()
    twelfth_board = fields.String() 
    twelfthpass_year = fields.Integer()
    twelfth_percentage = fields.Float()
    twelfth_schoolname = fields.String()
    specializationin = fields.String()
    otp = fields.String()
    is_active = fields.Integer()
    jti = fields.String()