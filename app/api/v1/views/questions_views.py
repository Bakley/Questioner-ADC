"""Questions views file"""

from flask import Flask
from flask_restful import Resource, reqparse
from app.api.v1.models import questions

question_view = questions.QuestionsModel()


class QuestionResource(Resource):
    """Question class"""
    parser = reqparse.RequestParser()
    parser.add_argument('body', required=True,
                        help='Location cannot be blank', type=str)
    parser.add_argument('title', required=True,
                        help='topic cannot be blank', type=str)
    parser.add_argument('createdBy', required=True,
                        help='created by cannot be blank', type=int)
    parser.add_argument('meetup', required=True,
                        help='meetup cannot be blank', type=int)

    def post(self):
        args = QuestionResource.parser.parse_args()
        location = args.get('body')
        topic = args.get('title')

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


class UpvoteResource(Resource):
    """Upvote view"""

    def patch(self, questions_id):
        """Upvote method"""

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

    def delete(self):
        pass
