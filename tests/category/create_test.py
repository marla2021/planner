from typing import List

import pytest
from freezegun import freeze_time

from goals.models import GoalCategory

@freeze_time('2022-05-01T13:06:12.461236Z')
@pytest.mark.django_db
def test_create(client, user, category):
    assert not GoalCategory.objects.all()
    response = client.post(
        "/goals/goal/create/",
        {
             "id": category.id,
             "user": {
                    "id": user.id,
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
    ads: List[GoalCategory] = GoalCategory.objects.all()
    assert len(ads) == 1

    assert response.status_code == 201
    assert response.json() == {
        "id": category[0].pk,
        "user": {
            "id": user[0].pk,
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
