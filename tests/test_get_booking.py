import pytest
from cod.booking_api import BookingAPI
from cod.auth_api import AuthAPI
from cod.helpers import match_schema

class TestGetBooking:

    @classmethod
    def setup_class(cls):
        cls.auth_api = AuthAPI()
        cls.booking_api = BookingAPI()
        cls.booking_id = None
        cls.token = None

        payload = {
            "firstname": "Alexander",
            "lastname": "Grigor",
            "totalprice": 180,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-10-10",
                "checkout": "2024-10-15"
            },
            "additionalneeds": "WiFi"
        }
        create_response = cls.booking_api.create_booking(payload)
        assert create_response.status_code == 200, "Не удалось создать бронирование для получения по ID"
        create_json = create_response.json()
        cls.booking_id = create_json.get('bookingid')

    def test_get_booking_success(self):
        response = self.__class__.booking_api.get_booking(self.__class__.booking_id)

        assert response.status_code == 200, f"Ожидался статус код 200 при получении бронирования, получен {response.status_code}"

        response_json = response.json()
        assert match_schema(response_json, 'schemas/booking_detail_schema.json'), "Схема ответа при получении бронирования не соответствует ожиданиям"

        assert response_json['firstname'] == "Alexander", "Имя не соответствует ожиданиям"
        assert response_json['lastname'] == "Grigor", "Фамилия не соответствует ожиданиям"
        assert response_json['totalprice'] == 180, "Цена не соответствует ожиданиям"
        assert response_json['depositpaid'] is True, "Депозит не соответствует ожиданиям"
        assert response_json['bookingdates']['checkin'] == "2024-10-10", "Дата заезда не соответствует ожиданиям"
        assert response_json['bookingdates']['checkout'] == "2024-10-15", "Дата выезда не соответствует ожиданиям"
        assert response_json['additionalneeds'] == "WiFi", "Дополнительные услуги не соответствуют ожиданиям"

    @classmethod
    def teardown_class(cls):
        if cls.booking_id:

            auth_response = cls.auth_api.get_token()
            assert auth_response.status_code == 200, "Не удалось получить токен для удаления"
            auth_json = auth_response.json()
            token = auth_json.get('token')
            assert match_schema(auth_json, 'schemas/auth_schema.json'), "Схема ответа токена не соответствует ожиданиям"

            delete_response = cls.booking_api.delete_booking(cls.booking_id, token)
            assert delete_response.status_code == 201, f"Ожидался статус код 201 при удалении, получен {delete_response.status_code}"
