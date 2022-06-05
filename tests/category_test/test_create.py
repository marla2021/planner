import pytest

from goals.models import GoalCategory, Board, BoardParticipant


@pytest.mark.django_db
def test_create_category(client, logged_in_user):
    board = Board.objects.create(title="TEST")
    BoardParticipant.objects.create(board=board, user=logged_in_user)
    response = client.post(
        "/goals/goal_category/create",
        {
            "title": "TEST",
            "board": board.id,
        },
        content_type="application/json"
    )

    assert response.status_code == 201

@pytest.mark.django_db
def test_create_category_unauthorized(client, user2):
    board = Board.objects.create(title="TEST")
    response = client.post(
        "/goals/goal_category/create",
        {
            "title": "TEST2",
            "board": board.id,
        },
        content_type="application/json"
    )

    assert response.status_code == 403