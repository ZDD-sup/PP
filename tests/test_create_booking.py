import pytest
from cod.booking_api import BookingAPI
from cod.auth_api import AuthAPI
from cod.helpers import match_schema
from cod.test_data import test_data

class TestCreateBooking:
    @classmethod
    def setup_class(cls):
        cls.auth_api = AuthAPI()
        cls.booking_api = BookingAPI()
        cls.booking_id = None

        auth_response = cls.auth_api.get_token(username=test_data["auth"]["username"], password=test_data["auth"]["password"])
        assert auth_response.status_code == 200, "Не удалось получить токен"
        auth_json = auth_response.json()
        assert match_schema(auth_json, 'schemas/auth_schema.json'), "Схема ответа токена не соответствует ожиданиям"
        cls.token = auth_json.get('token')

    def test_create_booking_success(self):
        payload = test_data["booking"]["valid"]
        response = self.booking_api.create_booking(payload)

        assert response.status_code == 200, f"Ожидался статус код 200, получен {response.status_code}"

        response_json = response.json()
        assert match_schema(response_json, 'schemas/booking_schema.json'), "Схема ответа бронирования не соответствует ожиданиям"

        self.booking_id = response_json.get('bookingid')

    @classmethod
    def teardown_class(cls):
        if cls.booking_id:
            delete_response = cls.booking_api.delete_booking(cls.booking_id, cls.token)
            assert delete_response.status_code == 201, f"Ожидался статус код 201 при удалении, получен {delete_response.status_code}"
