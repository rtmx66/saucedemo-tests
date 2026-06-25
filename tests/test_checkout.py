from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCheckout:

    def setup_cart(self, page):
        LoginPage(page).open()
        LoginPage(page).login("standard_user", "secret_sauce")
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()
        CartPage(page).click_checkout()

    def test_successful_checkout(self, page):
        self.setup_cart(page)
        checkout = CheckoutPage(page)
        checkout.fill_form("John", "Doe", "12345")
        checkout.click_continue()
        checkout.click_finish()
        assert "Thank you" in checkout.get_success_message()

    def test_checkout_empty_firstname(self, page):
        self.setup_cart(page)
        checkout = CheckoutPage(page)
        checkout.fill_form("", "Doe", "12345")
        checkout.click_continue()
        assert "First Name is required" in checkout.get_error_message()

    def test_checkout_empty_lastname(self, page):
        self.setup_cart(page)
        checkout = CheckoutPage(page)
        checkout.fill_form("John", "", "12345")
        checkout.click_continue()
        assert "Last Name is required" in checkout.get_error_message()

    def test_checkout_empty_postal(self, page):
        self.setup_cart(page)
        checkout = CheckoutPage(page)
        checkout.fill_form("John", "Doe", "")
        checkout.click_continue()
        assert "Postal Code is required" in checkout.get_error_message()