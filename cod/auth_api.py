import requests

class AuthAPI:
    BASE_URL = 'https://restful-booker.herokuapp.com'

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

    def get_token(self, username="admin", password="password123"):
        payload = {
            "username": username,
            "password": password
        }
        return self.session.post(f'{self.BASE_URL}/auth', json=payload)
    