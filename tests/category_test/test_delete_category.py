# import pytest
#
#
# @pytest.mark.django_db
# def test_delete_category(client,logged_in_user,goal_category, board, board_participants):
#     category = goal_category
#
#     response = client.delete(f"/goals/goal_category/{category.id}")
#     assert response.status_code == 204
#
#     response = client.get(f"/goals/goal_category/{category.id}")
#     assert response.status_code == 404