import pytest

from core.models import User
from goals.serializers import BoardListSerializer


@pytest.mark.django_db
def test_list_board(client, logged_in_user,board, board2,board_participants,board2_participants):
    expected_response = [
        BoardListSerializer(board).data,
        BoardListSerializer(board2).data,
    ]
    response = client.get("/goals/board/list")

    assert response.status_code == 200
    assert response.json() == expected_response

