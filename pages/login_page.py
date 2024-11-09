from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "input#user-name"
        self.password_input = "input#password"
        self.login_button = "input#login-button"
        self.url = "https://www.saucedemo.com/"

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
