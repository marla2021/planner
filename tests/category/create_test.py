from typing import List

import pytest
from freezegun import freeze_time

from goals.models import GoalCategory

@freeze_time('2022-05-01T13:06:12.461236Z')
@pytest.mark.django_db
def test_create(client):
    assert not GoalCategory.objects.all()
    response = client.post(
        "/goals/goal/create/",
        {
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
        },
        content_type="application/json",
    )


    # assert response.status_code == 201
    assert response.json() == {
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
