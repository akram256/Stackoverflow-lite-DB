"""
This module runs the application
"""

"""
This is the main module
"""
from flask import Flask
from urls import Urls

APP = Flask(__name__)
APP.env = 'development'
APP.testing = True
Urls.generate_url(APP)

if __name__ == '__main__':
    APP.run(debug = True)
