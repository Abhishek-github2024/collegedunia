from application.controller import *


@jwt_required()
def add_placementdata():
   
    data = request.get_json()
    check_placement = placement_table.query.filter_by(college_id=data['college_id']).all()
    for placement in check_placement:
        if placement.year == data['year'] and placement.company == data['company']:
            return jsonify({"message":"Duplicate entry are not allowed!"})
        else:
            continue
  
    if data['status']!="":
        current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        temp = placement_table(year=data['year'],company=data['company'],student_no = data['student_no'],avg=data['avg'],high=data['high'],created_at=current,updated_at=current,status=data['status'],college_id=data['college_id'])
        db.session.add(temp)
        db.session.commit()
        return jsonify({"message":"Placement data is successfully added!"}) ,200
    else:
        return jsonify({"message":"Required fields are mandatory to fill!"}) ,400
      


@jwt_required()
def update_placement(placement_id):
   
    data = request.get_json()
    item = placement_table.query.get_or_404(placement_id)
    schema = placement_tableschema()
    try:
        updated_data = schema.load(request.json, partial =True)
    except ValidationError as e:
        return jsonify ({'error':e.messages})
    
    for key,value in updated_data.items():
        if value is not None:
            setattr(item,key,value) 

    current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    placement_table.query.filter_by(placement_id=data['placement_id']).update({"updated_at":current})
    db.session.commit()
    return jsonify({"message":"Placement data is successfully updated!"}) ,200



@jwt_required()
def delete_placement(placement_id):
    placement_table.query.filter_by(placement_id=placement_id).update({"status":"inactive"})
    db.session.commit()
    return jsonify({"messsage":"Placement data is successfully deleted!"}) ,200


@jwt_required()
def show_placement_data(placement_id):
    check_placement = placement_table.query.filter_by(placement_id=placement_id).first()
    schema = placement_tableschema()
    placement_data = schema.dump(check_placement)
    return jsonify({"message":"Placement data is!","placement_data":placement_data}) ,200