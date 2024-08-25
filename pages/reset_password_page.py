from selenium.webdriver.common.by import By

from .const import PagePath as PP, PageTitle as PT
from .tools import PageMethods as PM

from .base_page import BasePage


class Locators:
    # fmt: off
    L_PAGE_TITLE         = (By.XPATH        , f"//main//h2[text()='{PT.RESET_PASSWORD}']")
    L_PASSWORD_INPUT     = (By.CSS_SELECTOR , "main input[name='Введите новый пароль']")
    L_PASSWORD_REVEALED  = (By.CSS_SELECTOR , "main input[name='Введите новый пароль'][type='text']")
    L_SHOW_PASSWORD_ICON = (By.CSS_SELECTOR , "main div[class^='input__icon']>svg")
    L_CODE_INPUT         = (By.CSS_SELECTOR , "main input[name='name']")
    L_SAVE_BUTTON        = (By.CSS_SELECTOR , "main button")
    L_LOGIN_LINK         = (By.CSS_SELECTOR , f"main a[href='{PP.LOGIN}'")
    # fmt: on


class ResetPasswordPage(BasePage, Locators):
    PAGE_PATH = PP.RESET_PASSWORD

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self._is_loaded_locator = self.L_PASSWORD_INPUT

    def fill_password(self, password):
        self.fill_text_input(self.L_PASSWORD_INPUT, password)

    def is_password_revealed(self):
        result = PM.is_visible(self.driver, self.L_PASSWORD_REVEALED)
        return result

    def click_show_password_button(self):
        self.click_element(self.L_SHOW_PASSWORD_ICON)

    def click_login_link(self):
        self.click_element(self.L_LOGIN_LINK)

    def click_save_button(self):
        self.click_element(self.L_SAVE_BUTTON)
