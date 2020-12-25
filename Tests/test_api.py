from pytest import mark


@mark.smoke
class TestCasesApi:
    """Basics test for the API"""

    def test_get_api(self, get_api_client):
        """test availability of the api"""
        client = get_api_client
        print("client: ", client.get("/"))
        assert client.get("/").status_code == 200
