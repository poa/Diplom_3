from const import Constants as C

from pages.login_page import LoginPage
from pages.recover_password_page import RecoverPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:
    def test_open_recover_password_page_successful(self, driver):
        login_page = LoginPage(driver)
        recover_password_page = RecoverPasswordPage(driver)

        login_page.open_page()
        login_page.click_recover_link()

        assert recover_password_page.is_loaded

    def test_recover_password_with_email_successful(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        recover_password_page.open_page()
        recover_password_page.recover(C.TEST_USER.get("email"))

        assert reset_password_page.is_loaded

    def test_show_password_button_password_revealed(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        recover_password_page.open_page()
        recover_password_page.recover(C.TEST_USER.get("email"))
        reset_password_page.fill_password(C.TEST_USER.get("password"))
        reset_password_page.click_show_password_button()

        assert reset_password_page.is_password_revealed is True
