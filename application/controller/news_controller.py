from application.controller import *

@jwt_required()
def add_news():
    name = get_jwt()['sub']['name']
    data = request.get_json()
    image = request.files['image']
    if data['tagline']!="" and data['college_id']!="" and data['content']!="":
        temp = request.base_url
        current = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
        temp = news_table(tagline=data['tagline'],image=image,created_at=current,updated_at=current,status=data['status'],content=data['content'],college_id=data['college_id'],name=name,url=temp)
        db.session.add(temp)
        db.session.commit()
        return jsonify({"message":"News data is successfully saved!"}) ,200
    else:
        return jsonify({"message":"Required fields are mandatory to fill!"}) ,400
        


@jwt_required()
def update_news(news_id):
   
    name = get_jwt()['sub']['name']
    item = news_table.query.get_or_404(news_id)
    schema = news_tableschema()
    try:
        updated_data = schema.load(request.json, partial =True)
    except ValidationError as e:
        return jsonify ({'error':e.messages})

    for key,value in updated_data.items():
        if value is not None:
            setattr(item,key,value) 

    current =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    news_table.query.filter_by(news_id=news_id).update({"updated_at":current,"name":name})
    db.session.commit()
    news_data = schema.dump(item)
    return jsonify({"message":"News data is successfully updated!","news_data":news_data}) ,200
    
    

@jwt_required()
def delete_news(news_id):
   
    name = get_jwt()['sub']['name']
    news_table.query.filter_by(news_id=news_id).update({"status":"inactive","name":name})
    db.session.commit()
    return jsonify({"message":"News is successfully deleted!"}) ,200
   

@jwt_required()
def show_news_data(news_id):
    check_news = news_table.query.filter_by(news_id=news_id).first()
    schema = news_tableschema()
    news_data = schema.dump(check_news)
    return jsonify({"message":"News data is!","news_data":news_data}) ,200    