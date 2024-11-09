import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
def test_checkout(page, username, password):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.navigate()
    login_page.login(username, password)

    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    cart_page.checkout()

    checkout_page.enter_checkout_info("Dima", "Zayc", "12345")
    checkout_page.finish_order()

    assert page.locator(".complete-header").inner_text() == "Thank you for your order!"
