import os
import tempfile
import pytest
import json
from flask_app import create_app

@pytest.fixture()
def tester():
    # creez un fisier nou temporar .sqlite unde va fi stocata baza de date
    db_fd, dbfile = tempfile.mkstemp(suffix=".sqlite")
    app = create_app("config.TestingConfig", db_file=dbfile)

    # returnez clientul tester cu setarea de mai sus
    with app.test_client() as tester:
        with app.app_context():
            yield tester

    # inchid file descriptorul
    os.close(db_fd)
    # sterg fisierul de pe disk
    os.unlink(app.config['DATABASE'])


def addToDb(tester):
    postData = {
        "some_text": "test - some text",
        "another_text": "test - another text",
        "a_date": "2022-01-01T00:00:00.000Z",
    }
    response = tester.post("/poc/add-to-db", json=postData)
    return response, postData


def test_poc_addToDb(tester):
    response, _ = addToDb(tester)
    assert response.status_code == 200
    assert "no_problem" in json.loads(response.data)


def test_poc_get_from_db(tester):
    _, postData = addToDb(tester)
    response = tester.get("/poc/get-from-db?id=2")
    assert response.status_code == 404
    response = tester.get("/poc/get-from-db?id=1")
    data = json.loads(response.data)
    assert data["no_problem"] == "test - some text"

def test_poc_get_all_from_db(tester):
    _, postData = addToDb(tester)
    response = tester.get("/poc/get-all-from-db")
    data = json.loads(response.data)
    assert [item for item in data if item["some_text"] == postData["some_text"]]
