import pytest

from goals.serializers import CommentSerializer


@pytest.mark.django_db
def test_update_comment(client, logged_in_user1, comment):
    expected_response = CommentSerializer(comment).data
    expected_response["text"] = "test10"

    response = client.patch(
        f"/goals/goal_comment/{comment.id}",
        {"text": "test10"},
        content_type="application/json"
    )

    assert response.status_code == 200

