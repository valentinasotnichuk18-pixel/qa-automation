import pytest
from pages.login_page import LoginPage


class TestLogin:

    def test_successful_login(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.login("tomsmith", "SuperSecretPassword!")
        assert page.is_success_message_visible()
        assert "secure area" in page.get_success_message().lower()

    def test_invalid_username(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.login("wronguser", "SuperSecretPassword!")
        assert page.is_error_message_visible()
        assert "invalid" in page.get_error_message().lower()

    def test_invalid_password(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.login("tomsmith", "wrongpassword")
        assert page.is_error_message_visible()
        assert "invalid" in page.get_error_message().lower()

    def test_empty_credentials(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.login("", "")
        assert page.is_error_message_visible()

    @pytest.mark.parametrize("username, password", [
        ("wronguser", "SuperSecretPassword!"),
        ("tomsmith", "wrongpassword"),
        ("", ""),
    ])
    def test_invalid_login_parametrized(self, driver, username, password):
        page = LoginPage(driver)
        page.open_login_page()
        page.login(username, password)
        assert page.is_error_message_visible()