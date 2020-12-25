from pytest import mark


class TestCasesApi:
    """Basics test for the API"""

    def test_get_api(self, get_api_client):
        """test availability of the api"""
        client = get_api_client
        print("client: ", client.get("/"))
        assert client.get("/").status_code == 200

    def test_even(self, get_api_client):
        response = get_api_client.get("/2")
        assert response.status_code == 200
        assert response.get_json() == {'message': 'the number is even', 'number': 2}

    def test_odd(self, get_api_client):
        n = 3
        response = get_api_client.get(f"/{n}")
        assert response.status_code == 302
        # print(dir(response))
        # print(response.location)
        assert response.location == f"http://localhost/is_odd/{n}"
