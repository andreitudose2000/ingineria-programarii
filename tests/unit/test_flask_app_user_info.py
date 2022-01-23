import os
import tempfile
import pytest
import json
import utils
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


def addOneUserInfoRow(tester):
    postData = {
        "user_height": 180
    }
    response = tester.post("/userInfo/", json=postData)
    return response, postData


def test_user_info_post_201(tester):
    response, _ = addOneUserInfoRow(tester)
    assert response.status_code == 201


def test_user_info_post_400_no_body(tester):
    response = tester.post("/userInfo/", json={})
    assert response.status_code == 400


def test_user_info_post_400_no_user_height(tester):
    response = tester.post("/userInfo/", json={
        "other_data": 100
    })
    assert response.status_code == 400


def test_user_info_post_400_bad_user_height(tester):
    response = tester.post("/userInfo/", json={
        "user_height": 90
    })
    assert response.status_code == 400
    response = tester.post("/userInfo/", json={
        "user_height": 260
    })
    assert response.status_code == 400
    response = tester.post("/userInfo/", json={
        "user_height": "wrong"
    })
    assert response.status_code == 400


def test_user_info_get_404(tester):
    response = tester.get("/userInfo/")
    assert response.status_code == 404


def test_user_info_get_200(tester):
    _, postData = addOneUserInfoRow(tester)
    response = tester.get("/userInfo/")
    assert response.status_code == 200
    data = json.loads(response.data)
    print(data)
    assert data["id"] == 1 \
           and data["user_height"] == postData["user_height"] \
           and data["chair_height"] == utils.chair_height_formula(postData["user_height"]) \
           and data["desk_height"] == utils.desk_height_formula(postData["user_height"])
