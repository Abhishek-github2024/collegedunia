from app import app
from dotenv import load_dotenv
import os
from datetime import datetime,timedelta
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token,get_jwt,jwt_manager,JWTManager,jwt_required,create_refresh_token
from flask_marshmallow import Marshmallow
import random
from flask_mail import Message,Mail
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
# import flask_whooshalchemy as wa

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@localhost/{os.getenv('USER_DB')}'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@localhost/collegedunia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = os.getenv('secret_key')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=15)
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('USER_MAIL')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'None'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SECRET_KEY'] = os.getenv('secret_key')
app.config['WHOOSH_BASE'] = 'whoosh'
UPLOAD_FOLDER = '/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSTIONS = set(['png','jpg','jpeg','gif'])



db = SQLAlchemy(app)
jwt = JWTManager(app)
ma = Marshmallow(app)
mail = Mail(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app,db)