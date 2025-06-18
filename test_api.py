import requests
import pytest
import json

@pytest.fixture
def base_url():
    return "https://restful-booker.herokuapp.com"

def test_ping(base_url):
    response = requests.get(base_url + "/ping")

    # Verify status code
    assert response.status_code == 201
    # Verify content-type
    assert response.headers["Content-Type"] == "text/plain; charset=utf-8"

def test_create_booking(base_url):

    payload = json.dumps({
    "firstname": "User32920",
    "lastname": "Test38388",
    "totalprice": 123,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-06-17",
        "checkout": "2025-06-20"
    },
    "additionalneeds": "Breakfast"
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }

    response = requests.request("POST", base_url + "/booking", headers=headers, data=payload)

    assert response.status_code == 200
    assert response.json().bookingid == "application/json; charset=utf-8"
