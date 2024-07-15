from application.controller import *


@jwt_required()
def add_faculty():
        
    data = request.get_json()
    check_faculty = faculty_table.query.filter_by(college_id=data['college_id']).all()

    for faculty in check_faculty:
        if faculty.name == data['name'] and faculty.department == data['department']:
            return jsonify({"message":"Duplicate entry are not allowed!"}) ,409
        else:
            continue
    
    if data['name']!="" and data['department']!="" and data['status']!="" and  data['university_id']!="":
        current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        temp = faculty_table(name=data['name'],department=data['department'],qualification=data['qualification'],email=data['email'],created_at=current,updated_at=current,status=data['status'],college_id=data['college_id'],university_id=data['university_id'])
        db.session.add(temp)
        db.session.commit()
        return jsonify({"message":"Faculty data is successfully added!"}) ,200
    else:
        return jsonify({"message":"Required fields are mandatory to fill!"}) ,401



@jwt_required()
def update_faculty(faculty_id):

    data = request.get_json()
    item = faculty_table.query.get_or_404(faculty_id)
    schema = faculty_tableschema()
    try:
        updated_data = schema.load(request.json, partial =True)
    except ValidationError as e:
        return jsonify ({'error':e.messages})
    
    for key,value in updated_data.items():
        if value is not None:
            setattr(item,key,value) 

    current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    faculty_table.query.filter_by(faculty_id=faculty_id).update({"updated_at":current})
    db.session.commit()

    faculty_data = schema.dump(item)
    return jsonify({"message":"Faculty data is successfully updated!","faculty_data":faculty_data}) ,200


@jwt_required()
def delete_faculty(faculty_id):
    faculty_table.query.filter_by(faculty_id=faculty_id).update({"status":"inactive"})
    db.session.commit()
    return jsonify({"messsage":"Faculty data is successfully deleted!"}) ,200
     

@jwt_required()
def show_faculty_data(faculty_id):
    check_faculty = faculty_table.query.filter_by(faculty_id=faculty_id).first()
    schema = faculty_tableschema()
    faculty_data = schema.dump(check_faculty)
    return jsonify({"message":"Faculty data is!","faculty_data":faculty_data}) ,200