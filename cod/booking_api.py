import requests

class BookingAPI:
    BASE_URL = 'https://restful-booker.herokuapp.com'

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

    def create_booking(self, payload):
        return self.session.post(f'{self.BASE_URL}/booking', json=payload)

    def get_booking(self, booking_id):
        return self.session.get(f'{self.BASE_URL}/booking/{booking_id}')

    def update_booking(self, booking_id, token, payload):
        headers = {'Cookie': f'token={token}'}
        return self.session.put(f'{self.BASE_URL}/booking/{booking_id}', json=payload, headers=headers)

    def delete_booking(self, booking_id, token):
        headers = {'Cookie': f'token={token}'}
        return self.session.delete(f'{self.BASE_URL}/booking/{booking_id}', headers=headers)
    