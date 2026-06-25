class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.success_message = page.locator(".complete-header")
        self.error_message = page.locator(".error-message-container")

    def fill_form(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    def click_continue(self):
        self.continue_button.click()

    def click_finish(self):
        self.finish_button.click()

    def get_success_message(self):
        return self.success_message.text_content()

    def get_error_message(self):
        return self.error_message.text_content()    