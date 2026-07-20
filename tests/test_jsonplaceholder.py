import requests
import pytest   

def test_get_all_posts_status(posts_response):
    assert posts_response.status_code == 200
def test_get_single_post_id(single_post_response):
    data = single_post_response.json()
    assert data["id"] == 1

def test_get_single_post_fields(single_post_response):
    data = single_post_response.json()
    assert 'userId' in data
    assert 'title' in data
    assert 'body' in data

def test_create_post(base_url):
    payload = {
        "title": "Test Post",
        "body": "This is a test",
        "userId": 1
    }
    response = requests.post(f"{base_url}/posts", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data['title'] == 'Test Post'

def test_get_nonexistent_post(base_url):
    response = requests.get(f"{base_url}/posts/9999")
    assert response.status_code == 404