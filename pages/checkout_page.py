from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = "input[data-test='firstName']"
        self.last_name_input = "input[data-test='lastName']"
        self.postal_code_input = "input[data-test='postalCode']"
        self.continue_button = "input[data-test='continue']"
        self.finish_button = "button[data-test='finish']"

    def enter_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)
        self.page.click(self.continue_button)

    def finish_order(self):
        self.page.click(self.finish_button)
