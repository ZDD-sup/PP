import pytest
from cod.auth_api import AuthAPI
from cod.helpers import match_schema

class TestGetToken:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.auth_api = AuthAPI()

    def test_get_token_success(self):
        response = self.auth_api.get_token()

        assert response.status_code == 200

        response_json = response.json()
        assert match_schema(response_json, 'schemas/auth_schema.json')