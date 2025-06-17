import requests
import pytest

@pytest.fixture
def base_url():
    return "https://restful-booker.herokuapp.com/"

def test_ping(base_url):
    response = requests.get(base_url + "ping")

    # Verify status code
    assert response.status_code == 201
    # Verify content-type
    assert response.headers["Content-Type"] == "text/plain; charset=utf-8"
