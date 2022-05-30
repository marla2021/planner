import pytest

from goals.models import GoalComment


@pytest.mark.django_db
def test_delete_comment(client, comment):

    response = client.delete(f"/goals/goal_comment/{comment.id}")
    assert response.status_code == 404
