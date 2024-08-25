from selenium.webdriver.common.by import By

from .const import PagePath as PP, PageTitle as PT
from .tools import PageMethods as PM

from .base_page import BasePage


class Locators:
    # fmt: off
    L_PAGE_TITLE     = (By.XPATH        , f"//main//h2[text()='{PT.RECOVER_PASSWORD}']")
    L_EMAIL_INPUT    = (By.CSS_SELECTOR , "main input[type='text']")
    L_RECOVER_BUTTON = (By.CSS_SELECTOR , "main button")
    L_LOGIN_LINK     = (By.CSS_SELECTOR , f"main a[href='{PP.LOGIN}'")
    # fmt: on


class RecoverPasswordPage(BasePage, Locators):
    PAGE_PATH = PP.RECOVER_PASSWORD

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self._is_loaded_locator = self.L_PAGE_TITLE

    def recover(self, email):
        PM.fill_text_input(self.driver, self.L_EMAIL_INPUT, email)
        self.click_recover_button()

    def click_recover_button(self):
        PM.click_element(self.driver, self.L_RECOVER_BUTTON)

    def click_login_link(self):
        PM.click_element(self.driver, self.L_LOGIN_LINK)
