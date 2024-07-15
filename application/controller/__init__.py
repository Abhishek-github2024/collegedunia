from flask import request,jsonify
import re
from application.database import *
# import flask_whooshalchemy as wa

import bcrypt
from marshmallow import schema,fields, ValidationError
from application.model.admin_model import *
from application.model.university_model import *
from application.model.college_model import *
from application.model.course_model import *
from application.model.placement_model import *
from application.model.user_model import *
from application.model.admission_model import *
from application.model.review_model import *
from application.model.cutoff_model import *
from application.model.gallery_model import *
from application.model.info_model import *
from application.model.faculty_model import *
from application.model.hostel_model import *
from application.model.answer_model import *
from application.model.question_model import *
from application.model.fee_model import *
from application.model.news_model import *
from application.model.rank_model import *
from application.model.news_model import *

from pytz import timezone 