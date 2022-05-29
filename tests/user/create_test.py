import pytest

from core.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("test", "test@test.ru", "test")
    assert User.objects.count() == 1

@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test_user")

@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True

