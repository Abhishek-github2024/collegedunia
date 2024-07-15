from application.controller import *

@jwt_required()
def add_college():
    data = request.get_json()
    university_id = data.get('university_id',None)
    name = data.get('name',None)
    about = data.get('about',None)
    city = data.get('city',None)
    state = data.get('state',None)
    type = data.get('type',None)
    estd = data.get('estd',None)
    aicte = data.get('aicte',None)
    mhrd = data.get('mhrd',None)
    status = data.get('status',None)
    
    check_college = college_table.query.filter_by(university_id=university_id).all()

    for college in check_college:
        if college.name == name and college.state == state and college.city == city:
            return jsonify({"message":"Duplicate entry are not allowed!"}) ,409
        else:
            continue

    if name and about and city and state and type and estd and aicte and mhrd and status:
        current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        temp = college_table(name=name, about=about, city=city, state=state, type=type, estd=estd, aicte=aicte, mhrd=mhrd, created_at=current, updated_at=current, status=status, university_id=university_id)
        db.session.add(temp)
        db.session.commit()
        return jsonify({"message":"College data is successfully added!"}) ,200
    else:
        return jsonify({"message":"Required fields are mandatory to fill!"}) ,400
    


@jwt_required()
def update_college(college_id):

    check_college = college_table.query.filter_by(college_id=college_id).first()
    if check_college:
        item = college_table.query.get_or_404(college_id)
        schema = college_tableschema()
        try:
            updated_data = schema.load(request.json, partial =True)
        except ValidationError as e:
            return jsonify ({'error':e.messages})
    
        for key,value in updated_data.items():
            if value is not None:
                setattr(item,key,value) 

        current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        college_table.query.filter_by(college_id=college_id).update({"updated_at":current})
        db.session.commit()

        college_data = schema.dump(check_college)
        return jsonify({"message":"College data is successfully updated!","updated_data":college_data}), 200

    else:
        return jsonify({"message":"Something went wrong!"}) ,401
    
    

@jwt_required()
def delete_college(college_id):
    college_table.query.filter_by(college_id=college_id).update({"status":"inactive"})
    db.session.commit()
    return jsonify({"messsage":"College data is successfully deleted!"}) ,200



@jwt_required()
def show_college_data(college_id):
    check_college = college_table.query.filter_by(college_id=college_id).first()
    schema = college_tableschema()
    college_data = schema.dump(check_college)
    return jsonify({"message":"college data is!","college_data":college_data}) ,200
