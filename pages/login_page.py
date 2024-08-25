from selenium.webdriver.common.by import By

from .const import PagePath as PP, PageTitle as PT
from .tools import PageMethods as PM

from .base_page import BasePage


class Locators:
    # fmt: off
    L_PAGE_TITLE         = (By.XPATH        , f"//main//h2[text()='{PT.LOGIN}']")
    L_EMAIL_INPUT        = (By.CSS_SELECTOR , "main input[name='name']")
    L_PASSWORD_INPUT     = (By.CSS_SELECTOR , "main input[name='Пароль']")
    L_PASSWORD_REVEALED  = (By.CSS_SELECTOR , "main input[name='Пароль'][type='text']")
    L_SHOW_PASSWORD_ICON = (By.CSS_SELECTOR , "main div[class^='input__icon']>svg")
    L_LOGIN_BUTTON       = (By.CSS_SELECTOR , "main button")
    L_REGISTER_LINK      = (By.CSS_SELECTOR , f"main a[href='{PP.REGISTER}'")
    L_RECOVER_LINK       = (By.CSS_SELECTOR , f"main a[href='{PP.FORGOT_PASSWORD}'")
    # fmt: on


class LoginPage(BasePage, Locators):
    PAGE_PATH = PP.LOGIN

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self._is_loaded_locator = self.L_PAGE_TITLE

    def login(self, email, password):
        self.fill_text_input(self.L_EMAIL_INPUT, email)
        self.fill_text_input(self.L_PASSWORD_INPUT, password)
        self.click_login_button()

    def is_password_revealed(self):
        result = PM.is_visible(self.driver, self.L_PASSWORD_REVEALED)
        return result

    def click_show_password_button(self):
        self.click_element(self.L_SHOW_PASSWORD_ICON)

    def click_login_button(self):
        self.click_element(self.L_LOGIN_BUTTON)

    def click_register_link(self):
        self.click_element(self.L_REGISTER_LINK)

    def click_recover_link(self):
        self.click_element(self.L_RECOVER_LINK)