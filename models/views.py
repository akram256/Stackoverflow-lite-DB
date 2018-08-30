"""
This module handles get all questions and one question
"""

from flask import request, jsonify
from flask.views import MethodView
from config.db_link import linkdb

class Questionhandler(MethodView):

    def one_question(question_id):
        for question in questions:
            if question.questionn_id == question_id:
                return question
       