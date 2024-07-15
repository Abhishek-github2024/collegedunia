from application.controller import *


@jwt_required()
def add_rank():
    data = request.get_json()
    check_rank = rank_table.query.filter_by(college_id=data['college_id']).all()
    for rank in check_rank:
        if rank.course == data['course'] and rank.year == data['year'] and rank.by == data['by']:
            return jsonify({"message":"Duplicate entry is not allowed!"}) ,409
        else:
            continue
    if data['rank']!="" and data['status']!="" and data['university_id']!="":
        current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        temp = rank_table(rank=data['rank'],course=data['course'],by=data['by'],year=data['year'],created_at=current,updated_at=current,status=data['status'],college_id=data['college_id'],university_id=data['university_id'])
        db.session.add(temp)
        db.session.commit()
        return jsonify({"message":"Rank data is successfully saved!"}) ,200
    else:
        return jsonify({"message":"Required fields are mandatory to fill!"}) ,400 
    


@jwt_required()
def update_rank(rank_id):
    item = rank_table.query.get_or_404(rank_id)
    schema = rank_tableschema()
    try:
        updated_data = schema.load(request.json, partial =True)
    except ValidationError as e:
        return jsonify ({'error':e.messages})
    
    for key,value in updated_data.items():
        if value is not None:
            setattr(item,key,value) 

    current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    rank_table.query.filter_by(rank_id=rank_id).update({"updated_at":current})
    db.session.commit()
    rank_data = schema.dump(item)
    return jsonify({"message":"Rank data is successfully updated!","rank_data":rank_data}) ,200 
    


@jwt_required()
def delete_rank(rank_id):
    rank_table.query.filter_by(rank_id=rank_id).update({"status":"Inactive"})
    db.session.commit()
    return jsonify({"messsage":"Rank data is successfully deleted!"}) ,200



@jwt_required()
def show_rank_data(rank_id):
    check_rank = rank_table.query.filter_by(rank_id=rank_id).first()
    schema = rank_tableschema()
    rank_data = schema.dump(check_rank)
    return jsonify({"message":"Rank data is!","rank_data":rank_data}) ,200