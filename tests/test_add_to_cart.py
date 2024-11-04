import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
def test_add_to_cart(page, username, password):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login(username, password)

    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    assert page.locator(".shopping_cart_badge").inner_text() == "1"
