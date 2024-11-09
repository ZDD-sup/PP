from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = "button[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_link = ".shopping_cart_link"

    def add_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def go_to_cart(self):
        self.page.click(self.cart_link)
