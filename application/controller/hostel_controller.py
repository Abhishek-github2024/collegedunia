from application.controller import *



@jwt_required()
def add_hostel():
   
    data = request.get_json()
    check_hostel = hostel_table.query.filter_by(college_id = data['college_id']).all()

    for hostel in check_hostel:
        if hostel.name == data['name']:
            return jsonify({"message":"Duplicate entry is not allowed!"}) ,409
        else:
            continue

    if data['college_id']!="" and data['max_fee']!="":
        current = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        temp = hostel_table(name=data['name'],min_fee=data['min_fee'],max_fee=data['max_fee'],created_at=current,updated_at=current,status=data['status'],college_id=data['college_id'])
        db.session.add(temp)
        db.session.commit()
        return jsonify({"message":"Hostel data is successfully added!"}) ,200
    else:
        return jsonify({"message":"Required fields are mandatory to fill!"}) ,400
    


@jwt_required()
def update_hostel(hostel_id):
    
        item = hostel_table.query.get_or_404(hostel_id)
        schema = hostel_tableschema()
        try:
            updated_data = schema.load(request.json, partial =True)
        except ValidationError as e:
            return jsonify ({'error':e.messages})
        
        for key,value in updated_data.items():
            if value is not None:
                setattr(item,key,value) 

        current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        hostel_table.query.filter_by(hostel_id=hostel_id).update({"updated_at":current})
        db.session.commit()
        hostel_data = schema.dump(item)
        return jsonify({"message":"Hostel data is successfully updated!","hostel_data":hostel_data}) ,200


@jwt_required()
def delete_hostel(hostel_id):
    
    hostel_table.query.filter_by(hostel_id=hostel_id).update({"status":"inactive"})
    db.session.commit()
    return jsonify({"messsage":"Hostel data is successfully deleted!"}) ,200


@jwt_required()
def show_hostel_data(hostel_id):
    check_hostel = hostel_table.query.filter_by(hostel_id=hostel_id).first()
    schema = hostel_tableschema()
    hostel_data = schema.dump(check_hostel)
    return jsonify({"message":"Hostel data is!","hostel_data":hostel_data}) ,200
