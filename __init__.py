"""
This module sets up the flask emvironment
"""
from flask import Flask
from config import ENVIRONMENT, TESTING, SECRET_KEY, DEBUG
# from urls import Urls
from config.database_connection import Databaseconn

APP = Flask(__name__)
APP.secret_key = SECRET_KEY
APP.testing = TESTING
APP.debug = DEBUG
APP.env = ENVIRONMENT
APP.errorhandler(404)(ErrorHandler.url_not_found)

Urls.generate_url(APP)
DatabaseAccess.create_tables(APP)

CORS(APP)