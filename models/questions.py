"""
This module handles get all questions and one question
"""

from flask import request, jsonify
from flask.views import MethodView
from config.db_link import linkdb
from models.question import Question


class GetAllquestion(MethodView):
    """
        This method returns all 
        questions in a JSON format
        :return
    """
    def get_all_questions(self ,sql_statement, data=None):
        sql = sql_statement
        tuple_list = []
        if  data is not None:
            tuple_list = linkdb.retrieve_all(sql, data)
        else:
            tuple_list = linkdb.retrieve_all(sql)

        question_list = []
        for question_tuple in tuple_list:
            question_dict = {
                "question_id": request_tuple[1],
                "user_id": request_tuple[2],
                "title": request_tuple[3],
                "question": request_tuple[4],
            }
            question_list.append(question_dict)
        return jsonify({"message": "all questions gotten successfully",
                        "questions": question_list})

    def one_question(self, question_id):
        """
        This remothod returns a question in
        a JSON format
        :param question_id: question_id
        :return
        """
        request_sql = """SELECT "users"user_name, question.* FROM "questions" LEFT JOIN "user"\
         ON(user.user_id = "user".user_id) WHERE "question_id" = %s """
        question_turple = linkdb.retrieve_one(request_sql, (question_id, ))

        if question_turple is not None:
            user_name = question_turple[0]
            question_id = question_turple[1]
            user_id = question_turple[2]
            title = question_turple[3]
            question = question_turple[4]
            return jsonify({"Status code": 200, "question": {
                "user_name": user_name,
                "question_id": question_id,
                "user_id": user_id,
                "title": title,
                "question": question
            },
                            "message": "question gotten successfully"})
        return self.error_message.no_questions_available(question_id)
        
    def post_question(self, user_id):
        """
        This method saves a question when a question_id is not set
        It takes control from the post() method
        :return
        """
        keys = ("title", "question")
        if not set(keys).issubset(set(request.json)):
            return self.error_message.request_missing_fields()

        request_condition = [
            request.json["title"].strip(),
            request.json["question"].strip(),
            ]

        if not all(request_condition):
            return self.error_message.fields_missing_information(request.json)

        user = linkdb.retrieve_one(
            """SELECT "user_id" FROM "users" WHERE "user_id" = %s""",
            (user_id, ))
        if user is None:
            return self.error_message.no_user_found_response("no question posted", request.json["question_id"])
        title = request.json['title']
        question= request.json['question']
        date= request.json['question']

        question = Question(user_name, title, question)

        question_existance = question.check_question_existance()
        if question_existance["status"] == "failure":
            return jsonify({"message": question_existance["message"]}), 400

        question.post_question()
        return jsonify({"status_code": 201, "message": "Question has been successfully"}), 201
