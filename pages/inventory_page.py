from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self):
        self.page.click("button[data-test='add-to-cart-sauce-labs-backpack']")

    def go_to_cart(self):
        self.page.click(".shopping_cart_link")
