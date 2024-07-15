from application.controller import *
otp = random.randint(1000,9999)

import bcrypt 

def user_registration():
    data = request.get_json()
    if not re.match(r'[^@]+@[^@]+\.[^@]+', data['email']):
        return jsonify({"message":"Please enter valied email"})
    elif not re.match(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$", data['password']):
        return jsonify({"message":"Please enter strong password"})
    else:
        check_email = user_table.query.filter_by(email=data['email']).first()
        if check_email:
            return jsonify({"message":"You are already register!"})
            # return user_login()
        else:
            if data['name']!="" and data['city']!="" and data['city']!="" and data['mobile_no']!="" and data['intrestedin_course']!="" and data['gender']!="" and data['tenth_board']!="" and data['tenthpass_year']!="" and data['tenth_percentage']!="" and data['tenth_schoolname']!="" and data['twelfth_board']!="" and data['twelfthpass_year']!="" and data['twelfth_percentage']!="" and data['twelfth_schoolname']!="" and data['specializationin']!="":
                recipient = data['email']
                msg = Message('Hello',recipients = [recipient]) 
                # msg = Message('Hello',recipients=recipient)
                msg.body = str(otp)
                asd = str(otp)
                mail.send(msg) 
                link = request.url
                # hashed_password =  bcrypt.generate_password_hash(data['password']).decode('utf-8') 
                hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
                temp = user_table(name=data['name'],email=data['email'],password=hashed_password,city=data['city'],mobile_no=data['mobile_no'],intrestedin_course=data['intrestedin_course'],gender=data['gender'],link=link,tenth_board=data['tenth_board'],tenthpass_year=data['tenthpass_year'],tenth_percentage=data['tenth_percentage'],tenth_schoolname=data['tenth_schoolname'],twelfth_board=data['twelfth_board'],twelfthpass_year=data['twelfthpass_year'],twelfth_percentage=data['twelfth_percentage'],twelfth_schoolname=data['twelfth_schoolname'],specializationin=data['specializationin'],otp=asd,is_active=0)
                db.session.add(temp)
                db.session.commit()
                return jsonify({"message":"OTP is send your email!"})
            else:
                return jsonify({"message":"Required fields are mandatory to fill!"})
            

def varify_account():
    data = request.get_json()
    check_user = user_table.query.filter_by(email=data['email']).first()
    # if check_user.is_active == 1:
    #     # return user_login()
    # else:
  
    
    if check_user.otp == data['otp']:
        user_table.query.filter_by(email=data['email']).update({"otp":0,"is_active":1})
        db.session.commit()
        return jsonify({"message":"Account is successfully varify!"})
    else:
        return jsonify({"message":"Enter correct OTP!"})
        

def user_login():
    data = request.get_json()
    check_user = user_table.query.filter_by(email=data['email']).first()
    if check_user:
        # recipient = data['email']
        # msg = Message('Hello',recipients = [recipient]) 
        # msg.body = str(otp)
        # asd = str(otp)
        # mail.send(msg)
        # user_table.query.filter_by(email=data['email']).update({"otp":asd})
        # return varify_account()
        check_password = bcrypt.checkpw(data['password'].encode('utf_8'),(check_user.password).encode('utf_8'))
        if check_password:
            result = {
                "email" : check_user.email,
                "user_id" : check_user.user_id
            }

            access_token = create_access_token(result)
            return jsonify({"message":"You are successfully logedin!","access_token":access_token})
        else:
            return jsonify({"message":"Enter correct password!"})
    else:
        return jsonify({"message":"Only register person are login!"})    
    

@jwt_required()
def user_logout():
    jti = get_jwt()['jti']
    user_id = get_jwt()['sub']['user_id']
    check_user = user_table.query.filter_by(user_id=user_id).first()
    if check_user:
        user_table.query.filter_by(user_id=user_id).update({"jti":jti})
        db.session.commit()
        return jsonify({"message":"You are successfully logout!"})
    else:
        return jsonify({"message":"Something went wrong!"})
