from application.controller import *


@jwt_required()
def add_course():
    
    data = request.get_json()
    check_course = course_table.query.filter_by(college_id=data['college_id']).all()
    for course in check_course:
        if course.name == data['name']:
            return jsonify({"message":"Duplicate entry is not allowed!"}) ,409
        else:
            continue

    if data['name']!="" and data['duration']!="" and data['eligibility']!="" and data['application_begain']!="" and data['application_end']!="" and data['status']!=""  and data['university_id']!="":
        current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        temp = course_table(name=data['name'],duration=data['duration'],eligibility=data['eligibility'],application_begain=data['application_begain'],application_end=data['application_end'],created_at=current,updated_at=current,status=data['status'],college_id=data['college_id'],university_id=data['university_id'])
        db.session.add(temp)
        db.session.commit()
        return jsonify({"message":"Course data is successfully saved!"}) ,200
    else:
        return jsonify({"message":"Required fields are mandatory to fill!"}) ,401


        
@jwt_required()
def update_course(course_id):
        
        item = course_table.query.get_or_404(course_id)
        schema = course_tableschema()
        try:
            updated_data = schema.load(request.json, partial =True)
        except ValidationError as e:
            return jsonify ({'error':e.messages})
        
        for key,value in updated_data.items():
            if value is not None:
                setattr(item,key,value) 

        current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        course_table.query.filter_by(course_id=course_id).update({"updated_at":current})
        db.session.commit()

        course_data = schema.dump(item)
        return jsonify({"message":"Course data is successfully updated!","course_data":course_data}) ,200
         
    

@jwt_required()
def delete_course(course_id):
        
    course_table.query.filter_by(course_id=course_id).update({"status":"inactive"})
    db.session.commit()
    return jsonify({"messsage":"Course data is successfully deleted!"}) ,200



@jwt_required()
def show_course_data(course_id):
     
    check_course = course_table.query.filter_by(course_id=course_id).first()
    schema = course_tableschema()
    course_data = schema.dump(check_course)
    return jsonify({"message":"Course data is!","course_data":course_data}) ,200
    