import pytest
from cod.booking_api import BookingAPI
from cod.auth_api import AuthAPI
from cod.helpers import match_schema
from cod.test_data import test_data

class TestDeleteBooking:

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

        payload = test_data["booking"]["delete"]
        create_response = cls.booking_api.create_booking(payload)
        assert create_response.status_code == 200, "Не удалось создать бронирование для удаления"
        create_json = create_response.json()
        cls.booking_id = create_json.get('bookingid')

    def test_delete_booking_success(self):
        response = self.__class__.booking_api.delete_booking(self.__class__.booking_id, self.__class__.token)

        assert response.status_code == 201, f"Ожидался статус код 201 при удалении, получен {response.status_code}"

        get_response = self.__class__.booking_api.get_booking(self.__class__.booking_id)
        assert get_response.status_code == 404, f"Ожидался статус код 404 при получении удаленного бронирования, получен {get_response.status_code}"

    @classmethod
    def teardown_class(cls):
        pass
