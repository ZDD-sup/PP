import pytest
from cod.booking_api import BookingAPI
from cod.auth_api import AuthAPI
from cod.helpers import match_schema

class TestUpdateBooking:

    @classmethod
    def setup_class(cls):
        cls.auth_api = AuthAPI()
        cls.booking_api = BookingAPI()
        cls.booking_id = None

        auth_response = cls.auth_api.get_token()
        assert auth_response.status_code == 200, "Не удалось получить токен"
        auth_json = auth_response.json()
        assert match_schema(auth_json, 'schemas/auth_schema.json'), "Схема ответа токена не соответствует ожиданиям"
        cls.token = auth_json.get('token')

        payload = {
            "firstname": "Alexander",
            "lastname": "Grigor",
            "totalprice": 150,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2024-11-15",
                "checkout": "2024-11-20"
            },
            "additionalneeds": "Breakfast"
        }
        create_response = cls.booking_api.create_booking(payload)
        assert create_response.status_code == 200, "Не удалось создать бронирование для обновления"
        create_json = create_response.json()
        cls.booking_id = create_json.get('bookingid')

    def test_update_booking_success(self):
        update_payload = {
            "firstname": "Valera",
            "lastname": "Petrov",
            "totalprice": 200,  
            "depositpaid": True,  
            "bookingdates": {
                "checkin": "2024-11-16",  
                "checkout": "2024-11-21"  
            },
            "additionalneeds": "Dinner"  
        }
        response = self.__class__.booking_api.update_booking(
            self.__class__.booking_id,
            self.__class__.token,
            update_payload
        )

        assert response.status_code == 200, f"Ожидался статус код 200 при обновлении, получен {response.status_code}"

        response_json = response.json()
        assert match_schema(response_json, 'schemas/booking_detail_schema.json'), "Схема ответа при обновлении не соответствует ожиданиям"

        assert response_json['firstname'] == "Valera", "Имя не соответствует ожиданиям"
        assert response_json['lastname'] == "Petrov", "Фамилия не соответствует ожиданиям"
        assert response_json['totalprice'] == 200, "Обновленная цена не соответствует ожиданиям"
        assert response_json['depositpaid'] is True, "Обновленный депозит не соответствует ожиданиям"
        assert response_json['bookingdates']['checkin'] == "2024-11-16", "Обновленная дата заезда не соответствует ожиданиям"
        assert response_json['bookingdates']['checkout'] == "2024-11-21", "Обновленная дата выезда не соответствует ожиданиям"
        assert response_json['additionalneeds'] == "Dinner", "Обновленные дополнительные услуги не соответствуют ожиданиям"

    @classmethod
    def teardown_class(cls):
        if cls.booking_id:
            delete_response = cls.booking_api.delete_booking(cls.booking_id, cls.token)
            assert delete_response.status_code == 201, f"Ожидался статус код 201 при удалении, получен {delete_response.status_code}"
