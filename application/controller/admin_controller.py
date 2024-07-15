from application.controller import *

def admin_login():
    data = request.get_json()
    email = data.get('email',None) 
    password = data.get('password',None)

    check_admin = admin_table.query.filter_by(email=email).first()
    
    if check_admin:
        if password == check_admin.password:
            result = {
                "name" : check_admin.name,
                "email" : check_admin.email
            }
            access_token = create_access_token(result)

            return jsonify({"data":result,"access_token":access_token}) ,200
        else:
            return jsonify({"message":"Wrong password!"}) ,401
    else:
        return jsonify({"message":"Unauthorized!"}) ,401 


@jwt_required()
def admin_logout():
    try:
        email = get_jwt()['sub']['email']
        jti = get_jwt()['jti']
    except:
        return jsonify({"message":"Internal Error!"}) ,501    
    admin_table.query.filter_by(email=email).update({"jti":jti})
    db.session.commit()
    return jsonify({"message":"You are successfully logout!"}) ,200



import json
def all_data_of_college(college_id):
   
    check_faculty = faculty_table.query.filter_by(college_id=college_id, status='active').all()
    schema = faculty_tableschema(many=True)
    faculty_data = schema.dump(check_faculty)

    check_college = college_table.query.filter_by(college_id=college_id, status='active').all()
    schema = college_tableschema(many=True)
    college_data = schema.dump(check_college)

    check_course = course_table.query.filter_by(college_id=college_id, status='active').all()
    # schema = course_tableschema(many=True)
    # course_data = schema.dump(check_course)
    course = {}
    for i in check_course:
        schema = course_tableschema()
        course_data = schema.dump(i)
        check_fee = fee_table.query.filter_by(course_id = i.course_id, status='active').all()
        schema = fee_tableschema(many=True)
        fee_data = schema.dump(check_fee)

        course[i.course_id] = {
            "course" : course_data,
            "fees" : fee_data
        }
        print(type(course))

    check_admission = admission_table.query.filter_by(college_id=college_id, status='active').all()
    schema = admission_tableschema(many=True)
    admission_data = schema.dump(check_admission)

    check_review = review_table.query.filter_by(college_id=college_id, status='active').all()
    schema = review_tableschema(many=True)
    review_data = schema.dump(check_review)

    check_cutoff = cutoff_table.query.filter_by(college_id=college_id, status='active').all()
    schema = cutoff_tableschema(many=True)
    cutoff_data = schema.dump(check_cutoff)

    check_placement = placement_table.query.filter_by(college_id=college_id, status='active').all()
    schema = placement_tableschema(many=True)
    placement_data = schema.dump(check_placement)

    # check_placement = placement_table.query.filter_by(college_id=data['college_id']).all()
    # schema = placement_tableschema(many=True)
    # placement_data = schema.dump(check_placement)

    check_hostel = hostel_table.query.filter_by(college_id=college_id, status='active').all()
    schema = hostel_tableschema(many=True)
    hostel_data = schema.dump(check_hostel)


    check_question = question_table.query.filter_by(college_id=college_id, status='active').all()
    # schema = question_tableschema(many=True)
    # question_data = schema.dump(check_question)
    temp = {}
    for q in check_question:
        schema = question_tableschema()
        qanda = schema.dump(q)
        check_question_answer = answer_table.query.filter_by(question_id=q.question_id, status='active').all()
        schema = answer_tableschema(many=True)
        question_answer_data = schema.dump(check_question_answer)
        temp[q.question_id] = {
            'question': qanda,
            'answer': question_answer_data
        }
        
    # check_answer = answer_table.query.filter_by(college_id=data['college_id'], status='active').all()
    # schema = answer_tableschema(many=True)
    # answer_data = schema.dump(check_answer)

    check_rank = rank_table.query.filter_by(college_id=college_id, status='active').all()
    schema = rank_tableschema(many=True)
    rank_data = schema.dump(check_rank)

    check_news = news_table.query.filter_by(college_id=college_id, status='active').all()
    schema = news_tableschema(many=True)
    news_data = schema.dump(check_news)

    return jsonify({"faculty_data":faculty_data,"college_data":college_data,"course_data":course,"admission_data":admission_data,"review_data":review_data,"cutoff_data":cutoff_data,"placement_data":placement_data,"hostel_data":hostel_data,"Q&A":temp,"rank_data":rank_data,"news_data":news_data})
    


def affiliated_colleges(university_id):
    check_colleges = college_table.query.filter_by(university_id=university_id,status='active').all()
    temp = {}
    for college in check_colleges:
        if college.college_id == university_id:
            continue
        else:
            schema = college_tableschema()
            college_data = schema.dump(college)
            temp[college.college_id]={
                "college" : college_data
            }
    temp1 = request.url        
    return jsonify({"affiliated_college":temp,"url":temp1})  
    


def searching_colleges_by_name(name):
    search = "%{}%".format(name)
    print(search)
    temp = college_table.query.filter(college_table.name.like(search))
    print(temp)
    schema = college_tableschema(many=True)
    temp = schema.dump(temp)
    return jsonify({"message":"College data  is!","data":temp})


def search_college_by_state_city_course():
    data = request.get_json()
    state = data.get('state',None)
    city = data.get('city',None)
    course = data.get('courses',None)
    if state and city and course:

        search1 = "%{}%".format(city)
        search2 = "%{}%".format(course)
        temp1 = college_table.query.filter(college_table.city.like(city))
        schema = college_tableschema(many=True)
        temp1 = schema.dump(temp1)
    
        temp2 = course_table.query.filter(course_table.name.like(search2))
        schema = course_tableschema(many=True)
        temp2 = schema.dump(temp2)

        temp5= {}   
        for college in temp1:
            for courses in temp2:
                if college['college_id'] == courses['college_id']:
                    temp3 = college_table.query.filter_by(college_id=college['college_id']).all()
                    schema = college_tableschema(many=True)
                    temp3 = schema.dump(temp3)
                    temp5[college['college_id']] = {
                        "college" : temp3
                    }  
                else:
                    continue       
           
        return jsonify({"colleges":temp5}) 
    

    if state and city:
        search = "%{}%".format(city)
        temp = college_table.query.filter(college_table.city.like(search))
        schema = college_tableschema(many=True)
        temp = schema.dump(temp)
        return jsonify({"colleges":temp})

    elif state and course:
        search1 = "%{}%".format(state)
        search2 = "%{}%".format(course)
        temp = college_table.query.filter(college_table.state.like(search1))
        schema = college_tableschema(many=True)
        temp = schema.dump(temp)

        temp1 = course_table.query.filter(course_table.name.like(search2))
        schema = course_tableschema(many=True)
        temp1 = schema.dump(temp1)

        temp3 = {}    
        for college in temp:
            for courses in temp1:
                if college['college_id'] == courses['college_id']:
                    temp2 = college_table.query.filter_by(college_id=college['college_id']).all()
                    schema = college_tableschema(many=True)
                    temp2 = schema.dump(temp2)
                    temp3[college['college_id']] = {
                        "college" : temp2
                    }  
                else:
                    continue       
           
        return jsonify({"colleges":temp})    

    elif city and course:
        search1 = "%{}%".format(state)
        search2 = "%{}%".format(course)
        temp = college_table.query.filter(college_table.state.like(search1))
        schema = college_tableschema(many=True)
        temp = schema.dump(temp)

        temp1 = course_table.query.filter(course_table.name.like(search2))
        schema = course_tableschema(many=True)
        temp1 = schema.dump(temp1)

        temp3 = {}    
        for college in temp:
            for courses in temp1:
                if college['college_id'] == courses['college_id']:
                    temp2 = college_table.query.filter_by(college_id=college['college_id']).all()
                    schema = college_tableschema(many=True)
                    temp2 = schema.dump(temp2)
                    temp3[college['college_id']] = {
                        "college" : temp2
                    }  
                else:
                    continue       
           
        return jsonify({"colleges":temp})  
    
    elif state:
        search = "%{}%".format(state)
        temp = college_table.query.filter(college_table.state.like(search))
        schema = college_tableschema(many=True)
        temp = schema.dump(temp)
        print(temp)
        return jsonify({"colleges":temp})
     

    elif course:
        search = "%{}%".format(course)
        temp = course_table.query.filter(course_table.name.like(search))
        schema = course_tableschema(many=True)
        temp = schema.dump(temp)

        for college in temp:
            temp3 = college_table.query.filter_by(college_id=college['college_id']).all()
            schema = college_tableschema(many=True)
            temp3 = schema.dump(temp3)

        return jsonify({"colleges":temp})

    
    elif data['city']:
        search = "%{}%".format(data['city'])
        temp = college_table.query.filter(college_table.city.like(search))
        schema = college_tableschema(many=True)
        temp = schema.dump(temp)
        return jsonify({"colleges":temp})




def college_compression():
     
    def college_data(id):
        # <-------------college data function------------>
        check_college = college_table.query.filter_by(college_id=id).all()
        schema = college_tableschema(many=True)
        college_data = schema.dump(check_college)

        check_placement = placement_table.query.filter_by(college_id = id).all()
        schema = placement_tableschema(many=True)
        placement_data = schema.dump(check_placement)

        check_rank = rank_table.query.filter_by(college_id = id).all()
        schema = rank_tableschema(many=True)
        rank_data = schema.dump(check_rank)

        check_course = course_table.query.filter_by(college_id=id).all()
        temp3 = {}
        for course in check_course:
            check_fee = fee_table.query.filter_by(course_id = course.course_id).first()
            schema = fee_tableschema()
            fee_data = schema.dump(check_fee)

            check_course = course_table.query.filter_by(course_id = course.course_id).first()
            schema = course_tableschema()
            course_data = schema.dump(check_course)


            temp3 [course.course_id] = {
                "course" : course_data,
                "fee" : fee_data
            }

        
        temp1 = {}
        temp1 ={
            "college" : college_data,
            "course" : temp3,
            "placement" : placement_data,
            "rank" : rank_data
        }
        return temp1
    

    data = request.get_json()

    id = data.get('id',None)
    count = 0

    for i in id:
        if i == 0:
            continue
        else:
            count = count + 1

    if count == 0 or count == 1:
        return jsonify({"message":"Please select at least two college!"})    
        
    elif count == 2:
        id1 = id[0]
        id2 = id[1]  

        temp1 = college_data(id1)
        temp2 = college_data(id2)
        return jsonify({"college1":temp1,"college2":temp2})  
     
    elif count == 3:
        id1 = id[0]
        id2 = id[1]
        id3 = id[2]

        temp1 = college_data(id1)
        temp2 = college_data(id2)
        temp3 = college_data(id3)
        return jsonify({"college1":temp1,"college2":temp2,"college3":temp3})  
    
    else:
        id1 = id[0]
        id2 = id[1]
        id3 = id[2]
        id4 = id[3]

        temp1 = college_data(id1)
        temp2 = college_data(id2)
        temp3 = college_data(id3)
        temp4 = college_data(id4)
        return jsonify({"college1":temp1,"college2":temp2,"college3":temp3,"college4":temp4}) 



# def college_compression():
#     data = request.get_json()
#     id = data['id']
#     count = 0
#     for i in id:
#         if i == 0:
#             continue
#         else:
#             count = count + 1

#     if count == 0 or count == 1:
#         return jsonify({"message":"Please select at least two college!"})    
        
#     elif count ==2:
#         id1 = data['id'][0]
#         id2 = data['id'][1]

#         # <-------------college1------------>
#         check_college = college_table.query.filter_by(college_id=id1).all()
#         schema = college_tableschema(many=True)
#         college_data = schema.dump(check_college)

#         check_placement = placement_table.query.filter_by(college_id = id1).all()
#         schema = placement_tableschema(many=True)
#         placement_data = schema.dump(check_placement)

#         # check_cutoff = cutoff_table.query.filter_by(college_id = id1).all()
#         # schema = cutoff_tableschema(many=True)
#         # cutoff_data = schema.dump(check_cutoff)

#         check_course = course_table.query.filter_by(college_id=id1).all()
#         temp3 = {}
#         for course in check_course:
#             check_fee = fee_table.query.filter_by(course_id = course.course_id).first()
#             schema = fee_tableschema()
#             fee_data = schema.dump(check_fee)

#             check_course = course_table.query.filter_by(course_id = course.course_id).first()
#             schema = course_tableschema()
#             course_data = schema.dump(check_course)


#             temp3 [course.course_id] = {
#                 "course" : course_data,
#                 "fee" : fee_data
#             }

        
#         temp1 = {}
#         temp1 ={
#             "college" : college_data,
#             "course" : temp3,
#             "placement" : placement_data,
#             # "cutoff" : cutoff_data
#         }

#         # <--------- college2 -------->
#         check_college = college_table.query.filter_by(college_id=id2).all()
#         schema = college_tableschema(many=True)
#         college_data = schema.dump(check_college)

#         check_placement = placement_table.query.filter_by(college_id = id2).all()
#         schema = placement_tableschema(many=True)
#         placement_data = schema.dump(check_placement)

#         check_course = course_table.query.filter_by(college_id=id2).all()
#         temp4 = {}
#         for course in check_course:
#             check_fee = fee_table.query.filter_by(course_id = course.course_id).first()
#             schema = fee_tableschema()
#             fee_data = schema.dump(check_fee)

#             check_course = course_table.query.filter_by(course_id = course.course_id).first()
#             schema = course_tableschema()
#             course_data = schema.dump(check_course)

#             temp4 [course.course_id] = {
#                 "course" : course_data,
#                 "fee" : fee_data,
#             }

#         temp2 = {}
#         temp2= { 
#             "college" : college_data,
#             "course" : temp4,
#             "placement" : placement_data
#         }

#         return jsonify({"college1":temp1,"college2":temp2})  
      
#     elif count == 3:
#         id1 = data['id'][0]
#         id2 = data['id'][1]
#         id3 = data['id'][2]

#         # <-------------college1------------>
#         check_college = college_table.query.filter_by(college_id=id1).all()
#         schema = college_tableschema(many=True)
#         college_data = schema.dump(check_college)

#         check_placement = placement_table.query.filter_by(college_id = id1).all()
#         schema = placement_tableschema(many=True)
#         placement_data = schema.dump(check_placement)

#         check_course = course_table.query.filter_by(college_id=id1).all()
#         temp3 = {}
#         for course in check_course:
#             check_fee = fee_table.query.filter_by(course_id = course.course_id).first()
#             schema = fee_tableschema()
#             fee_data = schema.dump(check_fee)

#             check_course = course_table.query.filter_by(course_id = course.course_id).first()
#             schema = course_tableschema()
#             course_data = schema.dump(check_course)


#             temp3 [course.course_id] = {
#                 "course" : course_data,
#                 "fee" : fee_data
#             }

        
#         temp1 = {}
#         temp1 ={
#             "college" : college_data,
#             "course" : temp3,
#             "placement" : placement_data
#         }

#         # <--------- college2 -------->
#         check_college = college_table.query.filter_by(college_id=id2).all()
#         schema = college_tableschema(many=True)
#         college_data = schema.dump(check_college)

#         check_placement = placement_table.query.filter_by(college_id = id2).all()
#         schema = placement_tableschema(many=True)
#         placement_data = schema.dump(check_placement)

#         check_course = course_table.query.filter_by(college_id=id2).all()
#         temp4 = {}
#         for course in check_course:
#             check_fee = fee_table.query.filter_by(course_id = course.course_id).first()
#             schema = fee_tableschema()
#             fee_data = schema.dump(check_fee)

#             check_course = course_table.query.filter_by(course_id = course.course_id).first()
#             schema = course_tableschema()
#             course_data = schema.dump(check_course)

#             temp4 [course.course_id] = {
#                 "course" : course_data,
#                 "fee" : fee_data,
#             }

#         temp2 = {}
#         temp2= { 
#             "college" : college_data,
#             "course" : temp4,
#             "placement" : placement_data
#         }

#         # <-----------college3---------->
#         check_college = college_table.query.filter_by(college_id=id3).all()
#         schema = college_tableschema(many=True)
#         college_data = schema.dump(check_college)

#         check_placement = placement_table.query.filter_by(college_id = id3).all()
#         schema = placement_tableschema(many=True)
#         placement_data = schema.dump(check_placement)

#         check_course = course_table.query.filter_by(college_id=id3).all()
#         temp6 = {}
#         for course in check_course:
#             check_fee = fee_table.query.filter_by(course_id = course.course_id).first()
#             schema = fee_tableschema()
#             fee_data = schema.dump(check_fee)

#             check_course = course_table.query.filter_by(course_id = course.course_id).first()
#             schema = course_tableschema()
#             course_data = schema.dump(check_course)

#             temp6 [course.course_id] = {
#                 "course" : course_data,
#                 "fee" : fee_data,
#             }

#         temp5 = {}
#         temp5= { 
#             "college" : college_data,
#             "course" : temp6,
#             "placement" : placement_data
#         }

#         return jsonify({"college1":temp1,"college2":temp2,"college3":temp5})  
#         # return jsonify({"id1":id1,"id2":id2,"id3":id3})
#     else:
#         id1 = data['id'][0]
#         id2 = data['id'][1]
#         id3 = data['id'][2]
#         id4 = data['id'][3]

#         # <-------------college1------------>
#         check_college = college_table.query.filter_by(college_id=id1).all()
#         schema = college_tableschema(many=True)
#         college_data = schema.dump(check_college)

#         check_placement = placement_table.query.filter_by(college_id = id1).all()
#         schema = placement_tableschema(many=True)
#         placement_data = schema.dump(check_placement)

#         check_course = course_table.query.filter_by(college_id=id1).all()
#         temp3 = {}
#         for course in check_course:
#             check_fee = fee_table.query.filter_by(course_id = course.course_id).first()
#             schema = fee_tableschema()
#             fee_data = schema.dump(check_fee)

#             check_course = course_table.query.filter_by(course_id = course.course_id).first()
#             schema = course_tableschema()
#             course_data = schema.dump(check_course)


#             temp3 [course.course_id] = {
#                 "course" : course_data,
#                 "fee" : fee_data
#             }

        
#         temp1 = {}
#         temp1 ={
#             "college" : college_data,
#             "course" : temp3,
#             "placement" : placement_data
#         }

#         # <--------- college2 -------->
#         check_college = college_table.query.filter_by(college_id=id2).all()
#         schema = college_tableschema(many=True)
#         college_data = schema.dump(check_college)

#         check_placement = placement_table.query.filter_by(college_id = id2).all()
#         schema = placement_tableschema(many=True)
#         placement_data = schema.dump(check_placement)

#         check_course = course_table.query.filter_by(college_id=id2).all()
#         temp4 = {}
#         for course in check_course:
#             check_fee = fee_table.query.filter_by(course_id = course.course_id).first()
#             schema = fee_tableschema()
#             fee_data = schema.dump(check_fee)

#             check_course = course_table.query.filter_by(course_id = course.course_id).first()
#             schema = course_tableschema()
#             course_data = schema.dump(check_course)

#             temp4 [course.course_id] = {
#                 "course" : course_data,
#                 "fee" : fee_data,
#             }

#         temp2 = {}
#         temp2= { 
#             "college" : college_data,
#             "course" : temp4,
#             "placement" : placement_data
#         }

#         # <-----------college3---------->
#         check_college = college_table.query.filter_by(college_id=id3).all()
#         schema = college_tableschema(many=True)
#         college_data = schema.dump(check_college)

#         check_placement = placement_table.query.filter_by(college_id = id3).all()
#         schema = placement_tableschema(many=True)
#         placement_data = schema.dump(check_placement)

#         check_course = course_table.query.filter_by(college_id=id3).all()
#         temp6 = {}
#         for course in check_course:
#             check_fee = fee_table.query.filter_by(course_id = course.course_id).first()
#             schema = fee_tableschema()
#             fee_data = schema.dump(check_fee)

#             check_course = course_table.query.filter_by(course_id = course.course_id).first()
#             schema = course_tableschema()
#             course_data = schema.dump(check_course)

#             temp6 [course.course_id] = {
#                 "course" : course_data,
#                 "fee" : fee_data,
#             }

#         temp5 = {}
#         temp5= { 
#             "college" : college_data,
#             "course" : temp6,
#             "placement" : placement_data
#         }

#         # <----------college4---------->
#         check_college = college_table.query.filter_by(college_id=id4).all()
#         schema = college_tableschema(many=True)
#         college_data = schema.dump(check_college)

#         check_placement = placement_table.query.filter_by(college_id = id4).all()
#         schema = placement_tableschema(many=True)
#         placement_data = schema.dump(check_placement)

#         check_course = course_table.query.filter_by(college_id=id4).all()
#         temp8= {}
#         for course in check_course:
#             check_fee = fee_table.query.filter_by(course_id = course.course_id).first()
#             schema = fee_tableschema()
#             fee_data = schema.dump(check_fee)

#             check_course = course_table.query.filter_by(course_id = course.course_id).first()
#             schema = course_tableschema()
#             course_data = schema.dump(check_course)

#             temp8 [course.course_id] = {
#                 "course" : course_data,
#                 "fee" : fee_data,
#             }

#         temp7 = {}
#         temp7= { 
#             "college" : college_data,
#             "course" : temp8,
#             "placement" : placement_data
#         }

#         return jsonify({"college1":temp1,"college2":temp2,"college3":temp5,"college4":temp7})  
#         # return jsonify({"id1":id1,"id2":id2,"id3":id3,"id4":id4})



