import requests

def test_github_status():
    response = requests.get('https://api.github.com/users/octocat')
    assert response.status_code == 200

def test_github_login():
    response = requests.get('https://api.github.com/users/octocat')
    data = response.json()
    assert data['login'] == 'octocat'
