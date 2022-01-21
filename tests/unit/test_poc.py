from flask_app import create_app
import unittest
import json


class TestPoc(unittest.TestCase):
    def test_index(self):
        tester = create_app().test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")

    def test_jsonResponse(self):
        tester = create_app().test_client(self)
        response = tester.get("/poc/json-response")
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data), {"test": "sucessful"})

    def test_jsonResponse2_200(self):
        tester = create_app().test_client(self)
        response = tester.post("/poc/json-response", json={
            "ma": "exista ma"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("exista ma", json.loads(response.data)["eu"])

    def test_jsonResponse2_400(self):
        tester = create_app().test_client(self)
        response = tester.post("/poc/json-response", json={
            "no": "nu exista ma"
        })
        self.assertEqual(response.status_code, 400)
        self.assertTrue("probleme" in json.loads(response.data))




if __name__ == "__main__":
    unittest.main()
