"""
This module provides responses to url requests.
"""
from flask import jsonify, request
from flask.views import MethodView
from models.questions import GetAllquestion
from auth.user import User


class QuestionViews(MethodView):
    """
    This class contains methods that respond to various url end points.
    """

    question_get = GetAllquestion()

    def get(self, question_id):
        """
       
        :param question_id: question id
        :return:
        """
        token = request.headers.get('auth_token')
        if not token:
            return jsonify({"message": "Token is missing"}), 401

        decoded = User.decode_token(request.headers.get('auth_token'))
        if decoded["state"] == "Failure":
            return User.decode_failure(decoded["error_message"])

        if User.check_login_status(decoded["user_id"]):
            if not question_id:
                request_sql = """SELECT "user".user_name, questions.* FROM "questions" LEFT JOIN "user"\
                ON(questions.user_id = "users".user_id) WHERE "question".user_id != %s"""
                sql_data = (decoded["user_id"], )
                return self.question_get.get_all_questions(request_sql, sql_data)
            return self.question_get.one_question(question_id)
        return jsonify({"message": "Please login"}), 401