import pytest

from app import create_app

@pytest.fixture
def test_app_csrf():
    app = create_app({
        'SECRET_KEY': 'barrel-spinster-barrel-smile',
        'TESTING': True
    })
    return app

@pytest.fixture
def client_csrf(test_app_csrf):
    return test_app_csrf.test_client()

# create a client with CSRF protection enabled
def test_with_csrf(client_csrf):
    # get returns input template
    response = client_csrf.get('/')
    assert b'<h1>Test Page with form</h1>' in response.data
    # but so does post
    response = client_csrf.post('/', data = {}, follow_redirects=True)
    assert b'<h1>Test Page with form</h1>' in response.data
