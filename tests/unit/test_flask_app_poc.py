from flask_app import create_app
import json

def test_poc():
    tester = create_app().test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"

def test_poc_jsonResponse():
    tester = create_app().test_client()
    response = tester.get("/poc/json-response")
    assert response.status_code == 200
    assert json.loads(response.data) == {"test": "sucessful"}

def test_poc_jsonResponse2_200():
    tester = create_app().test_client()
    response = tester.post("/poc/json-response", json={
        "ma": "exista ma"
    })
    assert response.status_code == 200
    assert "exista ma" in json.loads(response.data)["eu"]

def test_poc_jsonResponse2_400():
    tester = create_app().test_client()
    response = tester.post("/poc/json-response", json={
        "no": "nu exista ma"
    })
    assert response.status_code == 400
    assert "probleme" in json.loads(response.data)