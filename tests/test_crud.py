import requests
import pytest

BASE_URL = 'https://jsonplaceholder.typicode.com'


def test_create_post():
    payload = {'title': 'My Post', 'body': 'My Body', 'userId': 1}
    response = requests.post(f'{BASE_URL}/posts', json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data['title'] == 'My Post'
    assert data['body'] == 'My Body'
    assert data['userId'] == 1


def test_get_post():
    response = requests.get(f'{BASE_URL}/posts/1')
    data = response.json()
    assert response.status_code == 200
    assert data['id'] == 1
    assert 'title' in data


def test_update_post():
    payload = {'id': 1, 'title': 'Updated Title', 'body': 'Updated Body', 'userId': 1}
    response = requests.put(f'{BASE_URL}/posts/1', json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data['title'] == 'Updated Title'
    assert data['body'] == 'Updated Body'


def test_delete_post():
    response = requests.delete(f'{BASE_URL}/posts/1')
    assert response.status_code == 200


def test_get_deleted_post():
    response = requests.get(f'{BASE_URL}/posts/9999')
    assert response.status_code == 404
