"""Comment views file"""
import json
from flask_restful import Resource, reqparse

from flask_jwt_extended import jwt_required
from app.api.v2.models import comment_models, question_model
from app.utilities.validator_file import (check_for_empty_string)

comment_views = comment_models.CommentModel()
question_views = question_model.QuestionModel()


class CommentViewsResource(Resource):
    """Create and Delete a comment"""

    parser = reqparse.RequestParser()
    parser.add_argument('comment', required=True,
                        help='Comment cannot be blank', type=str)
    parser.add_argument('question', required=True,
                        help='Question cannot be blank', type=int)

    @jwt_required
    def post(self):
        """User can create a comment"""
        try:
            args = CommentViewsResource.parser.parse_args()
            comment = args.get('comment')
            question = args.get('question')
        except Exception:
            return {
                "status": 400,
                "error": "Invalid comment or Question field."
            }, 400

        if check_for_empty_string(comment):
            return {
                "status": 400,
                "error":
                "Please provide a comment for the question"
            }, 400

        passed_question = question_views.get_a_specific_question(
            args['question'])
        if not passed_question:
            return {
                "status": 404,
                "error": "The question ID you entered is not available"
            }, 404

        comment = comment_views.create_comment(
            comment=args.get('comment'),
            question=args.get('question')

        )

        return {
            "status": 201,
            "data": comment,
            "Message": "meetup successfully created"
        }, 201
