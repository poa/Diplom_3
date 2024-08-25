from selenium.webdriver.common.by import By

from .const import PagePath as PP, PageTitle as PT
from .tools import PageMethods as PM

from .base_page import BasePage


class Locators:
    # fmt: off
    L_RECOVER_PAGE_TITLE = (By.XPATH        , f"//main//h2[text()='{PT.RECOVER_PASSWORD}']")
    L_EMAIL_INPUT        = (By.CSS_SELECTOR , "main input[type='text']")
    L_PASSWORD_INPUT     = (By.CSS_SELECTOR , "main input[name='Введите новый пароль']")
    L_CODE_INPUT         = (By.CSS_SELECTOR , "main input[name='name']")
    L_PASSWORD_REVEALED  = (By.CSS_SELECTOR , "main input[name='Введите новый пароль'][type='text']")
    L_SHOW_PASSWORD_ICON = (By.CSS_SELECTOR , "main div[class^='input__icon']>svg")
    L_RECOVER_BUTTON     = (By.CSS_SELECTOR , "main button")
    L_SAVE_BUTTON        = (By.CSS_SELECTOR , "main button")
    L_LOGIN_LINK         = (By.CSS_SELECTOR , f"main a[href='{PP.LOGIN}'")
    # fmt: on


class RecoverPasswordPage(BasePage, Locators):
    PAGE_PATH = PP.FORGOT_PASSWORD

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self._is_loaded_locator = self.L_RECOVER_PAGE_TITLE

    def is_forgot_page_loaded(self):
        result = (
            self.is_loaded(path=PP.FORGOT_PASSWORD) is True
            and PM.is_visible(self.driver, self.L_RECOVER_BUTTON) is True
        )
        return result

    def is_reset_page_loaded(self):
        result = (
            self.is_loaded(path=PP.RESET_PASSWORD) is True
            and PM.is_visible(self.driver, self.L_SAVE_BUTTON) is True
        )
        return result

    def is_password_revealed(self):
        result = PM.is_visible(self.driver, self.L_PASSWORD_REVEALED)
        return result

    def fill_password(self, password):
        self.fill_text_input(self.L_PASSWORD_INPUT, password)

    def click_recover_button(self):
        self.click_element(self.L_RECOVER_BUTTON)

    def click_show_password_button(self):
        self.click_element(self.L_SHOW_PASSWORD_ICON)

    def click_login_link(self):
        self.click_element(self.L_LOGIN_LINK)

    def click_save_button(self):
        self.click_element(self.L_SAVE_BUTTON)

    def recover(self, email):
        self.fill_text_input(self.L_EMAIL_INPUT, email)
        self.click_recover_button()
        self.wait_loading()
