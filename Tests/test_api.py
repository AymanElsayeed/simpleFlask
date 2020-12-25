from pytest import mark


class TestCasesApi:
    """Basics test for the API"""

    def test_get_api(self, client):
        """test availability of the api"""
        print("client: ", client.get("/"))
        assert client.get("/").status_code == 200

    def test_even(self, client):
        response = client.get("/2")
        assert response.status_code == 200
        assert response.get_json() == {'message': 'the number is even', 'number': 2}

    def test_odd(self, client):
        n = 3
        response = client.get(f"/{n}")
        assert response.status_code == 302
        # print(dir(response))
        # print(response.location)
        assert response.location == f"http://localhost/is_odd/{n}"
