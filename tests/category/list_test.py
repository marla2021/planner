import pytest
from freezegun import freeze_time


@pytest.mark.django_db
@freeze_time('2022-05-01T13:06:12.461236Z')
def test_list(client):
    response = client.get(
        "/goals/goal_category/list/",
    )
    expected_response = {
        "id": 1,
        "user": {
            "id": 1,
            "username": "mar.la",
            "first_name": None,
            "last_name": None,
            "email": None
        },
        "created": '2022-05-01T13:06:12.461236Z',
        "updated": '2022-05-01T13:06:12.461236Z',
        "title": "test",
        "is_deleted": False,
        "board": 1
    }

    assert response.status_code == 200
    assert response.data == expected_response
