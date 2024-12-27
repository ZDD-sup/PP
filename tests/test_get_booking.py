import pytest
from cod.booking_api import BookingAPI
from cod.auth_api import AuthAPI
from cod.helpers import match_schema
from cod.test_data import test_data

class TestGetBooking:

    @classmethod
    def setup_class(cls):
        cls.auth_api = AuthAPI()
        cls.booking_api = BookingAPI()
        cls.booking_id = None
        cls.token = None

        payload = test_data["booking"]["get"]
        create_response = cls.booking_api.create_booking(payload)
        assert create_response.status_code == 200, "Не удалось создать бронирование для получения по ID"
        create_json = create_response.json()
        cls.booking_id = create_json.get('bookingid')

    def test_get_booking_success(self):
        response = self.__class__.booking_api.get_booking(self.__class__.booking_id)

        assert response.status_code == 200, f"Ожидался статус код 200 при получении бронирования, получен {response.status_code}"

        response_json = response.json()
        assert match_schema(response_json, 'schemas/booking_detail_schema.json'), "Схема ответа при получении бронирования не соответствует ожиданиям"

        assert response_json['firstname'] == test_data["booking"]["get"]["firstname"], "Имя не соответствует ожиданиям"
        assert response_json['lastname'] == test_data["booking"]["get"]["lastname"], "Фамилия не соответствует ожиданиям"
        assert response_json['totalprice'] == test_data["booking"]["get"]["totalprice"], "Цена не соответствует ожиданиям"
        assert response_json['depositpaid'] is test_data["booking"]["get"]["depositpaid"], "Депозит не соответствует ожиданиям"
        assert response_json['bookingdates']['checkin'] == test_data["booking"]["get"]["bookingdates"]["checkin"], "Дата заезда не соответствует ожиданиям"
        assert response_json['bookingdates']['checkout'] == test_data["booking"]["get"]["bookingdates"]["checkout"], "Дата выезда не соответствует ожиданиям"
        assert response_json['additionalneeds'] == test_data["booking"]["get"]["additionalneeds"], "Дополнительные услуги не соответствуют ожиданиям"

    @classmethod
    def teardown_class(cls):
        if cls.booking_id:

            auth_response = cls.auth_api.get_token(username=test_data["auth"]["username"], password=test_data["auth"]["password"])
            assert auth_response.status_code == 200, "Не удалось получить токен для удаления"
            auth_json = auth_response.json