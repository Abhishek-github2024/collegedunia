from application.controller import *


@jwt_required()
def add_answer():
    try:
        jti = get_jwt()['jti']
        user_id = get_jwt()['sub']['user_id']
    except:
        return jsonify({"message":"Internal Error!"}) ,501
        
    check_user = user_table.query.filter_by(user_id=user_id).first()
    if check_user and check_user.jti == jti:
        return jsonify({"message":"Unauthorized"}) ,401
    else:
        data = request.get_json()
        answer = data.get('answer',None)
        question_id = data.get('question_id',None)
        college_id = data.get('college_id',None)
        if answer:
            current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
            temp = answer_table(answer=answer, question_id=question_id, user_id=user_id, created_at=current, updated_at=current, status='active', college_id=college_id)
            db.session.add(temp)
            db.session.commit()
            return jsonify({"message":"Answer is successfully uploaded!"}) ,200
        else:
            return jsonify({"message":"Required field is mandataory to fill!"}) ,400
        


@jwt_required()
def update_answer(answer_id):
    jti = get_jwt()['jti']
    user_id = get_jwt()['sub']['user_id']
    check_user = user_table.query.filter_by(user_id=user_id).first()
    if check_user.jti == jti:
        return jsonify({"message":"Unauthorized!"}) ,401

    else:
        data = request.get_json()
        answer = data.get('answer',None)
        if answer:
            current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
            answer_table.query.filter_by(answer_id=answer_id).update({"answer":answer,"updated_at":current}) ,200
            db.session.commit()
            return jsonify({"message":"Answer is successfully updated!"}) ,200
        else:
            return jsonify({"message":"Required fields are mandatory to fill!"}) ,400
        


# @jwt_required()
# def delete_answer():
#     try:
#         jti = get_jwt()['jti']
#         user_id = get_jwt()['sub']['user_id']
#     except:
#         return jsonify({"message":"Internal Error!"}) ,501  
      
#     check_user = user_table.query.filter_by(user_id=user_id).first()
#     if check_user and check_user.jti == jti:
#         return jsonify({"message":"Unauthorized!"}) ,401
#     else:
#         data = request.get_json()
#         answer_id = data.get('answer_id',None)
#         answer_table.query.filter_by(answer_id=answer_id).update({"status":"inactive"})
#         db.session.commit()
#         return jsonify({"message":"Answer is successfully updated!"}) ,200