from application.controller import *



@jwt_required()
def add_university():
    data = request.get_json()
    if data['name']!="" and data['city']!="" and data['state']!="" and data['pincode']!="" and data['aicte'] and data['ugc']!="" and data['mhrd']!="" and data['estd']!="" and data['type']!="" and data['status']!="":
        check_university = university_table.query.filter_by(name=data['name']).all()
        for university in check_university:
            if university.name == data['name'] and university.state==data['state']:
                return jsonify({"message":"Duplicate entry are not allowed!"}),409
            else:
                continue

        current = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        temp = university_table(name=data['name'],city=data['city'],state=data['state'],pincode=data['pincode'],aicte=data['aicte'],ugc=data['ugc'],mhrd=data['mhrd'],estd=data['estd'],type=data['type'],created_at=current,updated_at=current,status=data['status'])
        db.session.add(temp)
        db.session.commit()
        return jsonify({"message":"University is successfully addded!"}) ,200
    else:
        return jsonify({"message":"Required fields are mandatory to fill!"}) ,400  
    


@jwt_required()
def update_university(university_id):
    item = university_table.query.get_or_404(university_id)
    schema = university_tableschema()
    try:
        updated_data = schema.load(request.json, partial =True)
    except ValidationError as e:
        return jsonify ({'error':e.messages})
    
    for key,value in updated_data.items():
        if value is not None:
            setattr(item,key,value) 

    current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    university_table.query.filter_by(university_id=university_id).update({"updated_at":current})
    db.session.commit()
    return jsonify({"message":"University data is successfully updated!"}) ,200
         
    

@jwt_required()
def delete_university(university_id):
    university_table.query.filter_by(university_id=university_id).update({"status":"Inactive"})
    db.session.commit()
    return jsonify({"messsage":"University data is successfully deleted!"}) ,200


@jwt_required()
def show_university_data(university_id):
    check_university = university_table.query.filter_by(university_id=university_id).first()
    schema = university_tableschema()
    university_data = schema.dump(check_university)
    return jsonify({"message":"University data is!","university_data":university_data}) ,200
