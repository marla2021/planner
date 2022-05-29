import pytest

USER_NAME = "username"
USER_PASSWORD = "userpassword"

@pytest.fixture()
@pytest.mark.django_db
def user1(client, django_user_model):
    return django_user_model.objects.create_user(
        username=USER_NAME,
        password=USER_PASSWORD
    )

@pytest.fixture()
@pytest.mark.django_db
def logged_in_user(client, user1):
    client.login(username=user1.username, password=USER_PASSWORD)
    return user1

@pytest.mark.django_db
def test_get_profile(client, logged_in_user):
    expected_response = {
        "id": logged_in_user.id,
        "username": "username",
        "first_name": "",
        "last_name": "",
        "email": ""
    }

    response = client.get(
        "/core/profile",
    )

    assert response.status_code == 200
    assert response.data == expected_response