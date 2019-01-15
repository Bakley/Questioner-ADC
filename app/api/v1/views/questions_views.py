"""Questions views file"""

from flask_restful import Resource, reqparse
from app.api.v1.models import questions
from app.utilities.validator_functions import (check_for_empty_string)

question_view = questions.QuestionsModel()


class QuestionResource(Resource):
    """Question views class"""
    parser = reqparse.RequestParser()
    parser.add_argument('body', required=True,
                        help='Location cannot be blank', type=str)
    parser.add_argument('title', required=True,
                        help='title cannot be blank', type=str)
    parser.add_argument('createdBy', required=True,
                        help='created by cannot be blank', type=int)
    parser.add_argument('meetup', required=True,
                        help='meetup cannot be blank', type=int)

    def post(self):
        """Creation of the question, and validating user inputs"""
        try:
            args = QuestionResource.parser.parse_args()
            body = args.get('body')
            title = args.get('title')
        except Exception:
            return {
                "status": 400,
                "error": "Invalid key error, please check on your spelling"
            }, 400

        # Check if user values inputted are empty

        if check_for_empty_string(body):
            return {
                "status": 400,
                "error":
                "Value cannot be empty, please provide a body for the question"
            }, 400

        if check_for_empty_string(title):
            return {
                "status": 400,
                "error":
                "Please provide a title for the question"
            }, 400

        question = question_view.create_question(body=args.get('body'),
                                                 title=args.get('title'),
                                                 meetup=args.get('meetup'),
                                                 createdBy=args.get(
                                                 'createdBy')
                                                 )

        return {
            "status": 201,
            "data": question,
            "Message": "question successfully created"
        }, 201

    def get(self):
        """Method to get all the available question"""
        question = question_view.get_all_questions()
        if not question:
            return {
                "status": 404,
                "error": "No upcoming question yet"
            }, 404
        return {
            "status": 200,
            "data": question
        }, 200


class UpvoteResource(Resource):
    """Upvote view class"""

    def patch(self, questions_id):
        """Upvote method, increments a vote by 1"""

        upvote = question_view.upvote_question(id=questions_id)

        if not upvote:
            return {
                "status": 404,
                "error": "No question found"
            }, 404
        return {
            "status": 200,
            "data": upvote
        }, 200


class DownvoteResource(Resource):
    """Downvote view class"""

    def patch(self, questions_id):
        """Downvote method, decrements a vote by 1"""

        downvote = question_view.downvote_question(id=questions_id)

        if not downvote:
            return {
                "status": 404,
                "error": "No question found"
            }, 404
        return {
            "status": 200,
            "data": downvote
        }, 200
