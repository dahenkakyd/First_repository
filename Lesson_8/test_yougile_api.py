import pytest  # noqa: F401
from yougile import YougileAPI

api_key = (""
           )
base_url = "https://ru.yougile.com/api-v2"
yougile_api = YougileAPI(base_url, api_key)

# Тестовые данные
test_project_title = "One_Project"
test_project_users = {"dcff2390-cfc9-4e75-b89c-dea91b09d5fc": "admin"}


def test_create_project_positive():
    response = yougile_api.create_project(
        test_project_title, test_project_users
    )
    assert response.status_code == 201
    project_id = response.json().get("id")
    assert project_id is not None
    yougile_api.update_project(project_id, deleted=True)


def test_create_project_negative():
    response = yougile_api.create_project("", test_project_users)
    assert response.status_code != 200
    assert response.status_code == 400


def test_update_project_positive():
    # Создаем проект
    create_response = yougile_api.create_project(
        test_project_title, test_project_users
    )
    assert create_response.status_code == 201
    project_id = create_response.json().get("id")
    assert project_id is not None
    new_title = "Updated One_Project"
    response = yougile_api.update_project(
        project_id, title=new_title
    )
    assert response.status_code == 200
    project_id = response.json().get("id")
    assert project_id is not None
    yougile_api.update_project(project_id, deleted=True)


def test_update_project_negative():
    response = yougile_api.update_project(
        "invalid_id", title="Updated One_Project"
    )
    assert response.status_code != 200
    assert response.status_code == 404


def test_get_project_positive():
    create_response = yougile_api.create_project(
        test_project_title, test_project_users
    )
    assert create_response.status_code == 201
    project_id = create_response.json().get("id")
    assert project_id is not None

    response = yougile_api.get_project(project_id)
    assert response.status_code == 200
    assert response.json().get("id") == project_id
    assert response.json().get("title") == test_project_title
    yougile_api.update_project(project_id, deleted=True)


def test_get_project_negative():
    response = yougile_api.get_project("invalid_id")
    assert response.status_code != 405
    assert response.status_code == 404