import pytest

from goals.models import GoalComment


@pytest.mark.django_db
def test_delete_comment(client, goal):
    comment = GoalComment.objects.create(text="test",goal=goal)
    response = client.get(f"/goals/goal_comment/{comment.id}")

    assert response.status_code == 200
