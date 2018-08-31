"""
This module runs the application
"""

"""
This is the main module
"""
from flask import Flask
from urls import Urls
from config.database_connection import Databaseconn
from flask_jwt_extended import JWTManager


db = Databaseconn()
db.create_tables()

APP = Flask(__name__)

APP.config['JWT_SECRET_KEY'] = 'thhtthhth' 
jwt = JWTManager(APP)

APP.env = 'development'
APP.testing = True

Urls.generate_url(APP)
if __name__ == '__main__':
    
    APP.run(debug = True)
