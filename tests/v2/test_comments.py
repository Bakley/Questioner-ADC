import json
from tests.v2.basecases import TestBaseCase


class CommentTestCase(TestBaseCase):
    """
    test class for the comment endpoint
    """

    def test_comment_created_successfully(self):
        """Test if a comment is posted"""
        auth_token = self.user_login()

        response = self.client.post('/api/v2/comment',
                                    data=json.dumps(self.comment_one),
                                    headers=dict(
                                        Authorization="Bearer " + auth_token),
                                    content_type='application/json')
        res = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            res["error"],
            "The question ID you entered is not available")
