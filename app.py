from application import app
from application.route import *

FLASK_ENV = 'app.py'

if __name__ == '__main__':
    app.run(port=555,debug=True)