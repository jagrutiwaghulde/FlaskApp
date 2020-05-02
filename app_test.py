from myApp import app
import pytest

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client

def test_dummy(client):
    response = client.get('/')
    print(response.data)
    assert b'Hello, World!' in response.data
   