from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.ordery_history_page import OrederHistoryPage


class TestAccount:
    def test_account_link_unauthorized_open_login_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.open_page()
        main_page.header.click_account_link()

        assert login_page.is_loaded()

    def test_account_link_authorized_open_profile_page(self, authorized):
        main_page = MainPage(authorized)
        profile_page = ProfilePage(authorized)

        main_page.open_page()
        main_page.header.click_account_link()

        assert profile_page.is_loaded()

    def test_open_order_history_successful(self, authorized):
        main_page = MainPage(authorized)
        profile_page = ProfilePage(authorized)
        order_history_page = OrederHistoryPage(authorized)

        main_page.open_page()
        main_page.header.click_account_link()
        profile_page.nav.click_order_history_link()

        assert order_history_page.is_loaded

    def test_logout_successful(self, authorized):
        main_page = MainPage(authorized)
        login_page = LoginPage(authorized)
        profile_page = ProfilePage(authorized)


        main_page.header.click_account_link()
        profile_page.nav.click_logout_button()

        assert login_page.is_loaded()
