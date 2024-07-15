from app import app
from application.controller.admin_controller import *
from application.controller.user_controller import *
from application.controller.university_controller import *
from application.controller.college_controller import *
from application.controller.course_controller import *
from application.controller.faculty_controller import *
from application.controller.cutoff_controller import *
from application.controller.fee_controller import *
from application.controller.hostel_controller import *
from application.controller.rank_controller import *
from application.controller.admission_controller import *
from application.controller.placement_controller import *
from application.controller.question_controller import *
from application.controller.answer_controller import *
from application.controller.review_controller import *
from application.controller.news_controller import *
# import flask_whooshalchemy as wa


@app.route('/admin_login',methods=["POST","GET"])
def admin_login_route():
    return admin_login()

@app.route('/user_registration',methods=["POST"])
def user_registration_route():
    return user_registration()

@app.route('/varify_account',methods=["PUT"])
def varify_account_route():
    return varify_account()

@app.route('/user_login',methods=["GET"])
def user_login_route():
    return user_login()

@app.route('/user_logout',methods=["DELETE"])
def user_logout_route():
    return user_logout()

@app.route('/admin_logout',methods=["DELETE"])
def admin_logout_route():
    return admin_logout()



@app.route('/university_data',methods=["POST"])
def add_university_route():
    return add_university()

@app.route('/university_data/update/<int:university_id>',methods=["PUT"])
def update_university_route(university_id):
    return update_university(university_id)

@app.route('/university_data/delete/<int:university_id>',methods=["DELETE"])
def delete_university_route(university_id):
    return delete_university(university_id)

@app.route('/university_data/show/<int:university_id>',methods=["GET"])
def show_university_data_route(university_id):
    return show_university_data(university_id)



@app.route('/college_data',methods=["POST"])
def add_college_route():
    return add_college()

@app.route('/college_data/update/<int:college_id>',methods=["PUT"])
def update_college_route(college_id):
    return update_college(college_id)

@app.route('/college_data/delete/<int:college_id>',methods=["DELETE"])
def delete_college_route(college_id):
    return delete_college(college_id)

@app.route('/college_data/show/<int:college_id>',methods=["GET"])
def show_college_data_route(college_id):
    return show_college_data(college_id)




@app.route('/course_data',methods=["POST"])
def add_course_route():
    return add_course()

@app.route('/course_data/update/<int:course_id>',methods=["PUT"])
def update_course_route(course_id):
    return update_course(course_id)

@app.route('/course_data/delete/<int:course_id>',methods=["DELETE"])
def delete_course_route(course_id):
    return delete_course(course_id)

@app.route('/course_data/show/<int:course_id>',methods=["GET"])
def show_course_data_route(course_id):
    return show_course_data(course_id)



@app.route('/faculty_data',methods=["POST"])
def add_faculty_route():
    return add_faculty()

@app.route('/faculty_data/update/<int:faculty_id>',methods=["PUT"])
def update_faculty_route(faculty_id):
    return update_faculty(faculty_id)

@app.route('/faculty_data/delete/<int:faculty_id>',methods=["DELETE"])
def delete_faculty_route(faculty_id):
    return delete_faculty(faculty_id)

@app.route('/faculty_data/show/<int:faculty_id>',methods=["GET"])
def show_faculty_data_route(faculty_id):
    return show_faculty_data(faculty_id)



@app.route('/cutoff_data',methods=["POST"])
def add_cutoff_route():
    return add_cutoff()

@app.route('/cutoff_data/update/<int:cutoff_id>',methods=["PUT"])
def update_cutoff_route(cutoff_id):
    return update_cutoff(cutoff_id)

@app.route('/cutoff_data/delete/<int:cutoff_id>',methods=["DELETE"])
def delete_cutoff_route(cutoff_id):
    return delete_cutoff(cutoff_id)

@app.route('/cutoff_data/show/<int:cutoff_id>',methods=["GET"])
def show_cutoff_data_route(cutoff_id):
    return show_cutoff_data(cutoff_id)




@app.route('/fee_data',methods=["POST"])
def add_fee_route():
    return add_fee()

@app.route('/fee_data/update/<int:fee_id>',methods=["PUT"])
def update_fee_route(fee_id):
    return update_fee(fee_id)

@app.route('/fee_data/delete/<int:fee_id>',methods=["DELETE"])
def delete_fee_route(fee_id):
    return delete_fee(fee_id)

@app.route('/fee_data/show/<int:fee_id>',methods=["GET"])
def show_fee_data_route(fee_id):
    return show_fee_data(fee_id)



@app.route('/hostel_data',methods=["POST"])
def add_hostel_route():
    return add_hostel()

@app.route('/hostel_data/update/<int:hostel_id>',methods=["PUT"])
def update_hostel_route(hostel_id):
    return update_hostel(hostel_id)

@app.route('/hostel_data/delete/<int:hostel_id>',methods=["DELETE"])
def delete_hostel_route(hostel_id):
    return delete_hostel(hostel_id)

@app.route('/hostel_data/show/<int:hostel_id>',methods=["GET"])
def show_hostel_data_route(hostel_id):
    return show_hostel_data(hostel_id)




@app.route('/rank_data',methods=["POST"])
def add_rank_route():
    return add_rank()

@app.route('/rank_data/update/<int:rank_id>',methods=["PUT"])
def update_rank_route(rank_id):
    return update_rank(rank_id)

@app.route('/rank_data/delete/<int:rank_id>',methods=["DELETE"])
def delete_rank_route(rank_id):
    return delete_rank(rank_id)

@app.route('/rank_data/show/<int:rank_id>',methods=["GET"])
def show_rank_data_route(rank_id):
    return show_rank_data(rank_id)



@app.route('/admission_data',methods=["POST"])
def add_admission_route():
    return add_admission()

@app.route('/admission_data/update/<int:admission_id>',methods=["PUT"])
def update_admission_route(admission_id):
    return update_admission(admission_id)

@app.route('/admission_data/delete/<int:admission_id>',methods=["DELETE"])
def delete_admission_route(admission_id):
    return delete_admission(admission_id)

@app.route('/admission_data/show/<int:admission_id>',methods=["GET"])
def show_admission_data_route(admission_id):
    return show_admission_data(admission_id)



@app.route('/placement_data',methods=["POST"])
def add_placementdata_route():
    return add_placementdata()

@app.route('/placement_data/update/<int:placement_id>',methods=["PUT"])
def update_placement_route(placement_id):
    return update_placement(placement_id)

@app.route('/placement_data/delete/<int:placement_id>',methods=["DELETE"])
def delete_placement_route(placement_id):
    return delete_placement(placement_id)

@app.route('/placement_data/show/<int:placement_id>',methods=["GET"])
def show_placement_data_route(placement_id):
    return show_placement_data(placement_id)



@app.route('/add_question',methods=["POST"])
def add_question_route():
    return add_question()

# @app.route('/update_question',methods=["PUT"])
# def update_question_route():
#     return update_question()

# @app.route('/delete_question',methods=["PUT"])
# def delete_question_route():
#     return delete_question()



@app.route('/answer_data',methods=["POST"])
def add_answer_route():
    return add_answer()

@app.route('/answer_data/update/<int:answer_id>',methods=["PUT"])
def update_answer_route(answer_id):
    return update_answer(answer_id)

# @app.route('/delete_answer',methods=["PUT"])
# def delete_answer_route():
#     return delete_answer()



@app.route('/add_review',methods=["POST"])
def add_review_route():
    return add_review()

@app.route('/update_review',methods=["PUT"])
def update_review_route():
    return update_review()



@app.route('/affiliated_colleges_data/show/<int:university_id>',methods=["GET"])
def affiliated_colleges_route(university_id):
    return affiliated_colleges(university_id)



@app.route('/searching_colleges_by_name/show/<name>',methods=["GET"])
def searching_colleges_by_name_route(name):
    return searching_colleges_by_name(name)




@app.route('/news_data',methods=["POST"])
def add_news_route():
    return add_news()

@app.route('/news_data/update/<int:news_id>',methods=["PUT"])
def update_news_route(news_id):
    return update_news(news_id)

@app.route('/news_data/delete/<int:news_id>',methods=["DELETE"])
def delete_news_route(news_id):
    return delete_news(news_id)

@app.route('/news_data/show/<int:news_id>',methods=["GET"])
def show_news_data_route(news_id):
    return show_news_data(news_id)



@app.route('/college_compressionsecondmethod',methods=["GET"])
def college_compression_route():
    return college_compression()



@app.route('/search_college_by_state_city_course',methods=["GET"])
def search_college_by_state_city_course_route():
    return search_college_by_state_city_course()


@app.route('/all_data_of_college/show/<int:college_id>',methods=["GET"])
def all_data_of_college_route(college_id):
    return all_data_of_college(college_id)