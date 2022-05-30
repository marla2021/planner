# import pytest
#
# from goals.models import GoalComment
#
#
# @pytest.mark.django_db
# def test_delete_comment(client,logged_in_user, goal):
#     comment = GoalComment.objects.create(text="test", goal=goal, user=logged_in_user)
#     response = client.delete(f"/goals/goal_comment/{comment.id}")
#     assert response.status_code == 204
#
#     response = client.get(f"/goals/goal_comment/{comment.id}")
#     assert response.status_code == 404
