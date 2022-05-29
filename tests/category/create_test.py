from typing import List

import pytest
from freezegun import freeze_time

from goals.models import GoalCategory

@freeze_time('2022-05-01T13:06:12.461236Z')
@pytest.mark.django_db
def test_create(client):
    assert not GoalCategory.objects.all()

    response = client.post(
        "/goals/goal_category/create/",
        {
            "title": "TEST1",
            "board": 1,
            "created": "2022-05-01T13:06:12.461236Z",
            "updated": "2022-05-01T13:06:12.461236Z",
            "is_deleted": False,
        },
        content_type="application/json",
    )
    category: List[GoalCategory] = GoalCategory.objects.all()

    assert response.status_code == 201
    assert response.json() == {
    "id": category[0].pk,
    "created": "2022-05-01T13:06:12.461236Z",
    "updated": "2022-05-01T13:06:12.461236Z",
    "title": "TEST1",
    "is_deleted": False,
    "board": 1
}
