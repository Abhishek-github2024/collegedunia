from application.controller import *


@jwt_required()
def add_admission():
    data = request.get_json()
    branch = data.get('branch',None)
    course = data.get('course',None)
    about = data.get('about',None)
    year = data.get('year',None)
    status = data.get('status',None)
    seats = data.get('seats',None)
    eligibility = data.get('eligibility',None)
    college_id = data.get('college_id',None)

    check_admission = admission_table.query.filter_by(college_id=college_id).all()
    for admission in check_admission:
        if admission.year == year and admission.branch == branch and admission.course == course:
            return jsonify({"message":"Duplicate value are not allowed"}) ,409
        else:
            continue
    else:
        if about and course and branch and year and status:
            current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
            temp = admission_table(about=about, seats=seats, course=course, branch=branch, eligibility=eligibility, year=year, created_at=current, updated_at=current, status=status, college_id=college_id)
            db.session.add(temp)
            db.session.commit()
            return jsonify({"message":"Admission data is successfully added!"}) ,200
        else:
            return jsonify({"message":"Required fields are mandatory to fill!"}) ,400



@jwt_required()
def update_admission(admission_id):

    item = admission_table.query.get_or_404(admission_id)
    schema = admission_tableschema()
    try:
        updated_data = schema.load(request.json, partial =True)
    except ValidationError as e:
        return jsonify ({'error':e.messages})
    
    for key,value in updated_data.items():
        if value is not None:
            setattr(item,key,value) 

    current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    admission_table.query.filter_by(admission_id=admission_id).update({"updated_at":current})
    db.session.commit()

    admission_data = schema.dump(item)
    return jsonify({"message":"Admission data is successfully updated!","admission_data":admission_data}) ,200
    


@jwt_required()
def delete_admission(admission_id):

    admission_table.query.filter_by(admission_id=admission_id).update({"status":"inactive"})
    db.session.commit()
    return jsonify({"messsage":"Admission data is successfully deleted!"}) ,200


@jwt_required()
def show_admission_data(admission_id):

    check_admission_table = admission_table.query.filter_by(admission_id=admission_id).first()
    schema = admission_tableschema()
    admission_data = schema.dump(check_admission_table)
    return jsonify({"message":"Admission data is","admission_data":admission_data}) ,200