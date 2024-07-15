from application.controller import *



@jwt_required()
def add_cutoff():

    data = request.get_json()
    check_cutoff = cutoff_table.query.filter_by(college_id=data['college_id']).all()
    for cutoff in check_cutoff:
        if cutoff.course == data['course'] and cutoff.branch == data['branch'] and cutoff.year == data['year'] and cutoff.test == data['test']:
            return jsonify({"message":"Duplicate entry is not allowed!"}) ,409
        else:
            continue
        
    if data['year']!="" and data['course']!="" and data['branch']!="" and data['quota']!="" and data['close']!="" and data['status']!=""  and['test']!="":
        current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        temp = cutoff_table(comments=data['comments'],test=data['test'],year=data['year'],course=data['course'],branch=data['branch'],quota=data['quota'],open=data['open'],close=data['close'],created_at=current,updated_at=current,status=data['status'],college_id=data['college_id'])
        db.session.add(temp)
        db.session.commit()
        return jsonify({"message":"Cutoff data is successfully saved!"}) ,200
    else:
        return jsonify({"message":"Required fields are mandatory to fill!"}) ,401



@jwt_required()
def update_cutoff(cutoff_id):
        
    item = cutoff_table.query.get_or_404(cutoff_id)
    schema = cutoff_tableschema()
    try:
        updated_data = schema.load(request.json, partial =True)
    except ValidationError as e:
        return jsonify ({'error':e.messages})
    
    for key,value in updated_data.items():
        if value is not None:
            setattr(item,key,value) 

    current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    cutoff_table.query.filter_by(cutoff_id=cutoff_id).update({"updated_at":current})
    db.session.commit() 

    cutoff_data = schema.dump(item)
    return jsonify({"message":"Cutoff data is successfully updated!","cutoff_data":cutoff_data}) ,200 
           


@jwt_required()
def delete_cutoff(cutoff_id):
    cutoff_table.query.filter_by(cutoff_id=cutoff_id).update({"status":"Inactive"})
    db.session.commit()
    return jsonify({"messsage":"Cutoff data is successfully deleted!"}) ,200


@jwt_required()
def show_cutoff_data(cutoff_id):
    check_cutoff_table = cutoff_table.query.filter_by(cutoff_id=cutoff_id).first()
    schema = cutoff_tableschema()
    cutoff_data = schema.dump(check_cutoff_table)
    return jsonify({"message":"Cutoff data is","cutoff_data":cutoff_data}) ,200