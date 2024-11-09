from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = "button[data-test='checkout']"

    def checkout(self):
        self.page.click(self.checkout_button)
