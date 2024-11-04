from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def checkout(self):
        self.page.click("button[data-test='checkout']")
