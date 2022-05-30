import pytest

from goals.models import Goal


@pytest.mark.django_db
def test_create_comment(client, logged_in_user, category):
    goal = Goal.objects.create(title="test", category=category, due_date="2022-05-30", user = logged_in_user)
    response = client.post(
        "/goals/goal_comment/create",
        {
            "text": "test",
            "goal": goal.id,
            "user": logged_in_user.id
        },
        content_type="application/json"
    )

    assert response.status_code == 201