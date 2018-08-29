"""
This module handels requests to urls.
"""

from views import RegisterUser, LoginUser ,Logout
from models.questions import GetAllquestion
from config.db_link import linkdb

class Urls(object):
    """
    Class to generate urls
    """
    @staticmethod
    def generate_url(app):
        """
         Generates urls on the app context
        :param: app: takes in the app variable
        :return: urls
        """
        app.add_url_rule('/api/v1/auth/signup/', view_func=RegisterUser.as_view('register_user'),
                         methods=["POST",])
        app.add_url_rule('/api/v1/auth/login/', view_func=LoginUser.as_view('login_user'),
                          methods=["POST",])
        app.add_url_rule('/api/v1/users/logout',view_func=Logout.as_view('logout_user'),
                         methods=["POST",])
        app.add_url_rule('/api/v1/questions/', defaults={'question_id': None},
                         view_func=GetAllquestion.as_view('get_all_questions'), methods=['GET',])
        app.add_url_rule('/api/v1/questions/<int:question_id>/',
                         view_func=GetAllquestion.as_view('get_one_question'), methods=['GET',])
        app.add_url_rule('/api/v1/questions/', defaults={'question_id': None},
                         view_func=GetAllquestion.as_view('post_a_question') , methods=['POST',])