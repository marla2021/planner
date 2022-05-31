import pytest

from core.models import User
from goals.models import GoalComment
from goals.serializers import CommentSerializer


@pytest.mark.django_db
def test_detail_comment(client, logged_in_user, comment):
    expected_response = CommentSerializer(comment).data

    response = client.get(f"/goals/goal_comment/{comment.id}")

    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db
def test_detail_comment_unauthor(client, goal):
    comment = GoalComment.objects.create(text="test",goal=goal)
    response = client.get(f"/goals/goal_comment/{comment.id}")

    assert response.status_code == 200

