import pytest

from core.models import User
from goals.models import Board, BoardParticipant, GoalCategory

USER_NAME = "username"
USER_PASSWORD = "userpassword"
USER_NAME2 = "username2"
USER_PASSWORD2 = "userpassword2"


@pytest.fixture()
@pytest.mark.django_db
def user1(client, django_user_model):
    return django_user_model.objects.create_user(
        username=USER_NAME,
        password=USER_PASSWORD
    )

@pytest.fixture()
@pytest.mark.django_db
def user2(client, django_user_model):
    return django_user_model.objects.create_user(
        username=USER_NAME2,
        password=USER_PASSWORD2
    )


@pytest.fixture()
@pytest.mark.django_db
def logged_in_user(client, user1):
    client.login(username=USER_NAME, password=USER_PASSWORD)
    return user1


@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test_user")


@pytest.fixture()
@pytest.mark.django_db
def board(client):
    return Board.objects.create(title="test")


@pytest.fixture()
@pytest.mark.django_db
def board_participants(client, board, user1):
    return BoardParticipant.objects.create(board=board, user = user1)


@pytest.fixture()
@pytest.mark.django_db
def category(client, user1, board, board_participants):
    return GoalCategory.objects.create(title="test", user=user1, board=board)