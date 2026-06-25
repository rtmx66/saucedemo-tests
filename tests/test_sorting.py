from pages.login_page import LoginPage

class TestSorting:

    def login(self, page):
        LoginPage(page).open()
        LoginPage(page).login("standard_user", "secret_sauce")

    def get_prices(self, page):
        items = page.locator(".inventory_item_price").all()
        return [float(i.text_content().replace("$", "")) for i in items]

    def get_names(self, page):
        items = page.locator(".inventory_item_name").all()
        return [i.text_content() for i in items]

    def sort_by(self, page, value):
        page.locator(".product_sort_container").select_option(value)

    def test_sort_price_low_to_high(self, page):
        self.login(page)
        self.sort_by(page, "lohi")
        prices = self.get_prices(page)
        assert prices == sorted(prices)

    def test_sort_price_high_to_low(self, page):
        self.login(page)
        self.sort_by(page, "hilo")
        prices = self.get_prices(page)
        assert prices == sorted(prices, reverse=True)

    def test_sort_name_a_to_z(self, page):
        self.login(page)
        self.sort_by(page, "az")
        names = self.get_names(page)
        assert names == sorted(names)

    def test_sort_name_z_to_a(self, page):
        self.login(page)
        self.sort_by(page, "za")
        names = self.get_names(page)
        assert names == sorted(names, reverse=True)