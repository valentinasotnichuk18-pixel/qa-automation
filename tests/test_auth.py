import requests
import pytest

BASE_URL = 'https://reqres.in/api'


@pytest.fixture(scope='module')
def auth_token():
    payload = {
        'email': 'eve.holt@reqres.in',
        'password': 'cityslicka'
    }
    response = requests.post(f'{BASE_URL}/login', json=payload)
    data = response.json()
    return data['token']


def test_login_status():
    payload = {
        'email': 'eve.holt@reqres.in',
        'password': 'cityslicka'
    }
    response = requests.post(f'{BASE_URL}/login', json=payload)
    assert response.status_code == 200


def test_login_returns_token():
    payload = {
        'email': 'eve.holt@reqres.in',
        'password': 'cityslicka'
    }
    response = requests.post(f'{BASE_URL}/login', json=payload)
    data = response.json()
    assert 'token' in data
    assert len(data['token']) > 0


def test_get_users_with_token(auth_token):
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = requests.get(f'{BASE_URL}/users', headers=headers)
    assert response.status_code == 200


def test_get_single_user(auth_token):
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = requests.get(f'{BASE_URL}/users/2', headers=headers)
    data = response.json()
    assert response.status_code == 200
    assert data['data']['id'] == 2
    assert 'email' in data['data']


def test_login_wrong_password():
    payload = {
        'email': 'eve.holt@reqres.in',
        'password': 'wrongpassword'
    }
    response = requests.post(f'{BASE_URL}/login', json=payload)
    assert response.status_code == 400
