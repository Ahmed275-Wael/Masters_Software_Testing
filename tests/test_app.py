import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Great Gatsby' in response.data or b'1984' in response.data

def test_cart_page(client):
    response = client.get('/cart')
    assert response.status_code == 200

def test_register_get(client):
    response = client.get('/register')
    assert response.status_code == 200

def test_login_get(client):
    response = client.get('/login')
    print("Response data:", response.data)
    assert response.status_code == 200