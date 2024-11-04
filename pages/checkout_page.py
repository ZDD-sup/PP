from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def enter_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill("input[data-test='firstName']", first_name)
        self.page.fill("input[data-test='lastName']", last_name)
        self.page.fill("input[data-test='postalCode']", postal_code)
        self.page.click("input[data-test='continue']")

    def finish_order(self):
        self.page.click("button[data-test='finish']")
