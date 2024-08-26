import allure

from const import Constants as C

from pages.login_page import LoginPage
from pages.recover_password_page import RecoverPasswordPage


class TestPasswordRecovery:
    @allure.title("Test password recovery page opens from login page")
    def test_open_recover_password_page_successful(self, driver):
        login_page = LoginPage(driver)
        recover_password_page = RecoverPasswordPage(driver)

        login_page.open_page()
        login_page.click_recover_link()

        assert recover_password_page.is_forgot_page_loaded()

    @allure.title("Test password reset page opens when request recovery by email")
    def test_recover_password_with_email_successful(self, driver):
        login_page = LoginPage(driver)
        recover_password_page = RecoverPasswordPage(driver)

        login_page.open_page()
        login_page.click_recover_link()
        recover_password_page.recover(C.TEST_USER.get("email"))

        assert recover_password_page.is_reset_page_loaded()

    @allure.title("Test password can be revealed with show password button")
    def test_show_password_button_password_revealed(self, driver):
        recover_password_page = RecoverPasswordPage(driver)

        recover_password_page.open_page()
        recover_password_page.recover(C.TEST_USER.get("email"))
        recover_password_page.fill_password(C.TEST_USER.get("password"))
        recover_password_page.click_show_password_button()

        assert recover_password_page.is_password_revealed() is True
