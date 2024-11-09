import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
def test_login(page, username, password):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    assert page.url == "https://www.saucedemo.com/inventory.html"
