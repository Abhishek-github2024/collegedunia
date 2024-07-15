from application.controller import *


@jwt_required()
def add_review():
    user_id = get_jwt()['sub']['user_id']
    check_user = user_table.query.filter_by(user_id=user_id).first()    
    if check_user is None:
        return jsonify({"message":"Unauthorized"}) ,401
    else:
        data = request.get_json()
        college_id = data.get('college_id',None)
        like = data.get('like',None)
        dislike = data.get('dislike',None)
        course_curriculum_overview= data.get('course_curriculum_overview',None)
        internship_opportunities = data.get('internship_opportunities',None)
        placement_experience = data.get('placement_experience',None)
        loan_scholarship_provisions = data.get('loan_scholarship_provisions',None)
        campus_life = data.get('campus_life',None)
        hostel_facilities = data.get('hostel_facilities',None)
        admission = data.get('admission',None)
        classroom_size = data.get('classroom_size',None)
        placement = data.get('placement',None)
        college = data.get('college',None)
        internship = data.get('internship',None)
        course = data.get('course',None)
        hostel = data.get('hostel',None)
        campus = data.get('fee',None)
        college_id = data.get('fee',None)
        user_id = data.get('fee',None)
        if check_user.college_id == college_id:
            return jsonify({"message":"Multiple time not write you review on a single college!"}) ,409
        else:
            if like and course_curriculum_overview and internship_opportunities and placement_experience and loan_scholarship_provisions and campus_life and hostel_facilities and admission and data['fee']!="" and data['college']!="" and data['course']!="":
                current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
                temp = review_table(like=data['like'],dislike=data['dislike'],course_curriculum_overview=data['course_curriculum_overview'],internship_opportunities=data['internship_opportunities'],placement_experience=data['placement_experience'],loan_scholarship_provisions=data['loan_scholarship_provisions'],campus_life=data['campus_life'],hostel_facilities=data['hostel_facilities'],admission=data['admission'],classroom_size=data['classroom_size'],fee=data['fee'],placement=data['placement'],college=data['college'],internship=data['internship'],course=data['course'],hostel=data['hostel'],campus=data['campus'],college_id=data['college_id'],user_id=data['user_id'],created_at=current,updated_at=current,status='active')
                db.session.add(temp)
                db.session.commit()
                return jsonify({"message":"Reviw is successfully saved!"})
            else:
                return jsonify({"message":"Required fileds are mandatory to fill!"})
            

@jwt_required()
def update_review():
    try:
        jti = get_jwt()['jti']
        user_id = get_jwt()['sub']['user_id']
    except:
        return jsonify({"message":"Something went wrong!"})
    
    check_user = user_table.query.filter_by(user_id=user_id).first()
    if check_user.jti == jti:
        return jsonify({"message":"Something went wrong!"})
    else:
        data = request.get_json()
        item = review_table.query.get_or_404(data['review_id'])
        schema = review_tableschema()
        try:
            updated_data = schema.load(request.json, partial =True)
        except ValidationError as e:
            return jsonify ({'error':e.messages})
        
        for key,value in updated_data.items():
            if value is not None:
                setattr(item,key,value) 

        current = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        review_table.query.filter_by(review_id=data['review_id']).update({"updated_at":current})
        db.session.commit()
        return jsonify({"message":"Review data is successfully updated!"})

