from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestCart:

    def test_add_one_item(self, page):
        LoginPage(page).open()
        LoginPage(page).login("standard_user", "secret_sauce")
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        assert inventory.get_cart_count() == "1"

    def test_add_multiple_items(self, page):
        LoginPage(page).open()
        LoginPage(page).login("standard_user", "secret_sauce")
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.add_item_to_cart("Sauce Labs Bike Light")
        assert inventory.get_cart_count() == "2"

    def test_remove_item_from_cart(self, page):
        LoginPage(page).open()
        LoginPage(page).login("standard_user", "secret_sauce")
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        inventory.go_to_cart()
        cart = CartPage(page)
        cart.remove_first_item()
        assert cart.get_items_count() == 0

    def test_cart_persists_after_navigation(self, page):
        LoginPage(page).open()
        LoginPage(page).login("standard_user", "secret_sauce")
        inventory = InventoryPage(page)
        inventory.add_item_to_cart("Sauce Labs Backpack")
        page.goto("https://www.saucedemo.com/inventory.html")
        assert inventory.get_cart_count() == "1"