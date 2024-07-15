from application.controller import *


@jwt_required()
def add_fee():
        
    data = request.get_json()
    check_fee = fee_table.query.filter_by(college_id=data['college_id']).all()
    for fee in check_fee:
        if fee.course_id == data['course_id'] and fee.year_wise == data['year_wise']:
            return jsonify({"message":"Duplicate entry is not allowed!"}) ,409
        else:
            continue
    
    if data['year_wise']!="" and data['max_fee']!="" and data['course_id']!="":
        current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        temp = fee_table(year_wise=data['year_wise'],min_fee=data['min_fee'],max_fee=data['max_fee'],created_at=current,updated_at=current,status=data['status'],course_id=data['course_id'],college_id=data['college_id'])
        db.session.add(temp)
        db.session.commit()
        return jsonify({"message":"Fee data is successfully added!"}) ,200
    else:
        return jsonify({"message":"Required fields are mandatory to fill!"}) ,401



@jwt_required()
def update_fee(fee_id):

    item = fee_table.query.get_or_404(fee_id)
    schema = fee_tableschema()
    try:
        updated_data = schema.load(request.json, partial =True)
    except ValidationError as e:
        return jsonify ({'error':e.messages})
    
    for key,value in updated_data.items():
        if value is not None:
            setattr(item,key,value) 

    current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    fee_table.query.filter_by(fee_id=fee_id).update({"updated_at":current})
    db.session.commit()

    fee_data = schema.dump(item)
    return jsonify({"message":"Fee data is successfully updated!","fee_data":fee_data}) ,200


@jwt_required()
def delete_fee(fee_id):
    fee_table.query.filter_by(fee_id=fee_id).update({"status":"inactive"})
    db.session.commit()
    return jsonify({"messsage":"Fee data is successfully deleted!"}) ,200


@jwt_required()
def show_fee_data(fee_id):
    check_fee = fee_table.query.filter_by(fee_id=fee_id).first()
    schema = fee_tableschema()
    fee_data = schema.dump(check_fee)
    return jsonify({"message":"Fee data is!","fee_data":fee_data}) ,200