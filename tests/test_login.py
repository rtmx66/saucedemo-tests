from pages.login_page import LoginPage

class TestLogin:

    def test_valid_login(self, page):
        login = LoginPage(page)
        login.open()
        login.login("standard_user", "secret_sauce")
        assert page.url == "https://www.saucedemo.com/inventory.html"

    def test_invalid_password(self, page):
        login = LoginPage(page)
        login.open()
        login.login("standard_user", "wrong_password")
        assert "Epic sadface" in login.get_error_message()

    def test_empty_fields(self, page):
        login = LoginPage(page)
        login.open()
        login.login("", "")
        assert "Username is required" in login.get_error_message()

    def test_locked_user(self, page):
        login = LoginPage(page)
        login.open()
        login.login("locked_out_user", "secret_sauce")
        assert "locked out" in login.get_error_message()