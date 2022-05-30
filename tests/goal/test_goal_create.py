import pytest


@pytest.mark.django_db
def test_create_goal(client, user1, category):

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