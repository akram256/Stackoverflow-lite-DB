"""
This module provides responses to url requests.
"""
from flask import jsonify, request
from flask.views import MethodView
from models.questions import GetAllquestion
from auth.user import User


class Question_now(MethodView):
    """
    This class contains methods that respond to various url end points.
    """

    Questions_fetch = GetAllquestion()

    def get(self, question_id):
        """
        Gets all questions and one question
        :return:
        """
        token = request.headers.get('auth_token')
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        decoded = User.decode_token(request.headers.get('auth_token'))
        if decoded["state"] == "Failure":
            return User.decode_failure(decoded["error_message"])

        if User.check_login_status(decoded["user_id"]):
            if not user_id:
                request_sql = """SELECT "users".user_name, question.* FROM "questions" LEFT JOIN "users"\ 
                ON(questions.user_id = "users".user_id) WHERE "question".user_id != %s"""
                sql_data = (decoded["user_id"], )
                return self.Questions_fetch.get_all_questions(request_sql, sql_data)
            return self.Questions_fetch.one_question(question_id)
        return jsonify({"message": "Please login"}), 401

    def post(self, question_id):
        """"
        Handles post question
        :return:
        """
        token = request.headers.get('auth_token')
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        decoded = User.decode_token(request.headers.get('auth_token'))
        if decoded["state"] == "Failure":
            return User.decode_failure(decoded["error_message"])
        if User.check_login_status(decoded["user_id"]):
            if question_id:
                return self.Questions_fetch.post_question(decoded["user_id"], question_id)
            if not request or not request.json:
                return jsonify({"status_code": 400, "data": str(request.data),
                                "error_message": "content not JSON"}), 400
            return self.Questions_fetch.post_question(decoded["user_id"])
        return jsonify({"message": "Please login"}), 401
     