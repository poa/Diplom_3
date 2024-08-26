import allure

from pages.login_page import LoginPage
from pages.account_page import AccountPage


class TestAccount:
    @allure.title("Test for unauthorized login page opens with header profile link")
    def test_account_link_unauthorized_opens_login_page(self, driver):
        login_page = LoginPage(driver)

        login_page.click_header_account_link()

        assert login_page.is_loaded()

    @allure.title("Test for authorized user profile page opens with header profile link")
    def test_authorized_user_account_link_opens_profile(self, authorized):
        account_page = AccountPage(authorized)
        account_page.click_header_account_link()

        assert account_page.is_profile_page_loaded()

    @allure.title("Test order history page opens for authorized user")
    def test_authorized_user_opens_order_history_successful(self, user_with_orders):
        account_page = AccountPage(user_with_orders)

        account_page.click_header_account_link()
        account_page.click_order_history_link()

        assert account_page.is_order_history_page_loaded()

    @allure.title("Test logout for authorized user")
    def test_logout_successful(self, authorized):
        login_page = LoginPage(authorized)
        account_page = AccountPage(authorized)

        account_page.click_header_account_link()
        account_page.click_logout_button()

        assert login_page.is_loaded()
