"""
This module provides responses to url requests.
"""
from flask import jsonify, request
from flask.views import MethodView
from models.questions import GetAllquestion
from auth.user import User
from flask_jwt_extended import  jwt_required, create_access_token, get_jwt_identity



class Question_now(MethodView):
    """
    This class contains methods that respond to various url end points.
    """

    Questions_fetch = GetAllquestion()
    @jwt_required 
    def get(self, question_id):
        """
        Gets all questions and one question
        :return:
        """
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        user_id = get_jwt_identity()
        
        request_sql = """SELECT "users".user_name, question * FROM "questions" LEFT JOIN "users" \ 
        ON(questions.user_id = "users".user_id) WHERE "questions".user_id != %s"""
        sql_data = (user_id)
        question = self.Questions_fetch.get_all_questions(request_sql, sql_data)

        if question:
            return question
        return jsonify({"message": "question not found"}), 40
    
    @jwt_required 
    def post(self):
        """"
        Handles post question
        """

        user_id = get_jwt_identity()

        if not request or not request.json:
            return jsonify({"status_code": 400, "data": str(request.data),
                            "error_message": "content not JSON"}), 400
        return self.Questions_fetch.post_question(user_id)
        return jsonify({"message": "Please login"}), 401
     