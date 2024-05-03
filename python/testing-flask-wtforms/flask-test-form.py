import pytest

from app import create_app

# create a client with CSRF protection disabled
@pytest.fixture
def test_app():
    app = create_app({
        'TESTING': True,
        'WTF_CSRF_ENABLED': False
    })
    return app

@pytest.fixture
def client(test_app):
    return test_app.test_client()

# now when can test the form submission
def test_without_csrf(client):
    # get returns input template
    response = client.get('/')
    assert b'<h1>Test Page with form</h1>' in response.data
    # but now post follows the redirect and returns the output template
    response = client.post('/', data = {}, follow_redirects=True)
    assert b'<h1>Test Output Page</h1>' in response.data
