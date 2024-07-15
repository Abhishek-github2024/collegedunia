from application.controller import *


@jwt_required()
def add_question():
    jti = get_jwt()['jti']
    user_id = get_jwt()['sub']['user_id']
    check_user = user_table.query.filter_by(user_id=user_id).first()
    if check_user and check_user.jti == jti:
        return jsonify({"message":"Only login person is ask question"})
    else:
        data = request.get_json()
        if data['question']!="" :
            current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
            temp = question_table(question=data['question'],college_id=data['college_id'],created_at=current,updated_at=current,status='active',user_id=data['user_id'])
            db.session.add(temp)
            db.session.commit()
            return jsonify({"message":"Question is successfully uploaded!"})
        else:
            return jsonify({"message":"Required fields are mandatory to fill!"})  


# @jwt_required()
# def update_question():
#     jti = get_jwt()['jti']
#     user_id = get_jwt()['sub']['user_id']
#     check_user = user_table.query.filter_by(user_id=user_id).first()
#     if check_user and check_user.jti == jti:   
#         return jsonify({"message":"Only login person have permission!"})  
#     else:
#         data = request.get_json()
        
#         question_table.query.filter_by(question_id=data['question_id']).update({"question":data['question']})

#         current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
#         question_table.query.filter_by(question_id=data['question_id']).update({"updated_at":current})
#         db.session.commit()
#         return jsonify({"message":"Question is successfully updated!"})
            


# @jwt_required()
# def delete_question():
#     jti = get_jwt()['jti']
#     user_id = get_jwt()['sub']['user_id']
#     check_user = user_table.query.filter_by(user_id=user_id).first()
#     if check_user and check_user.jti == jti:   
#         return jsonify({"message":"Only login person have permission!"})  
#     else:
#         data = request.get_json()
#         question_table.query.filter_by(question_id=data['question_id']).update({"status":"inactive"})
#         db.session.commit()
#         return jsonify({"message":"Question is successfully deleted!"}) 