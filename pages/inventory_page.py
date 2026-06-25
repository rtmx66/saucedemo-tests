class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_item_to_cart(self, item_name):
        self.page.locator(f"text={item_name}").first.wait_for()
        item = self.page.locator(f".inventory_item:has-text('{item_name}')")
        item.locator("button").click()

    def go_to_cart(self):
        self.cart_icon.click()

    def get_cart_count(self):
        return self.cart_badge.text_content()