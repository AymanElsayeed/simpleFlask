from pytest import mark


class TestCasesApi:
    """Basics test for the API"""
    even_numbers = [(i, {'message': 'the number is even', 'number': i}) for i in range(0, 10, 2)]
    odd_numbers = [(i, f"http://localhost/is_odd/{i}") for i in range(1, 10, 2)]

    def test_get_api(self, client):
        """test availability of the api"""
        print("client: ", client.get("/"))
        assert client.get("/").status_code == 200

    def test_even(self, client):
        response = client.get("/2")
        assert response.status_code == 200
        assert response.get_json() == {'message': 'the number is even', 'number': 2}

    @mark.parametrize(["number", "output"], even_numbers)
    def test_even_list(self, client, number, output):
        response = client.get(f"/{number}")
        assert response.status_code == 200
        assert response.get_json() == output

    def test_odd(self, client):
        n = 3
        response = client.get(f"/{n}")
        assert response.status_code == 302
        # print(dir(response))
        # print(response.location)
        assert response.location == f"http://localhost/is_odd/{n}"

    @mark.parametrize(["number", "output"], odd_numbers)
    def test_odd_list(self, client, number, output):
        response = client.get(f"/{number}")
        assert response.status_code == 302
        assert response.location == output
