class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.cart_items = page.locator(".cart_item")
        self.remove_buttons = page.locator(".cart_item button")

    def get_items_count(self):
        return self.cart_items.count()

    def click_checkout(self):
        self.checkout_button.click()

    def remove_first_item(self):
        self.remove_buttons.first.click()