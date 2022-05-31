import pytest

from core.models import User
from goals.models import GoalCategory


@pytest.mark.django_db
def test_create_goal(client, logged_in_user, category):

    response = client.post(
        "/goals/goal/create",
        {
            "title": "TEST",
            "category": category.id,
            "due_date" : "2022-05-30"
        },
        content_type="application/json"
    )

    assert response.status_code == 201


# @pytest.mark.django_db
# def test_create_goal_unauthor(client, board):
#     user = User.objects.create_user("test")
#     category = GoalCategory.objects.create(title="test", user=user, board=board)
#     response = client.post(
#         "/goals/goal/create",
#         {
#             "title": "TEST",
#             "category": category.id,
#             "due_date" : "2022-05-30"
#         },
#         content_type="application/json"
#     )

    assert response.status_code == 404