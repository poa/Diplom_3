from selenium.webdriver.common.by import By

from .base_page import BasePage
from .const import Constants as C
from .tools import PageMethods as PM


class Locators:
    # fmt: off
    L_EMAIL_INPUT       = (By.CSS_SELECTOR, "main input[type='text']")
    L_RESTORE_BUTTON    = (By.CSS_SELECTOR, "main button")
    L_LOGIN_LINK        = (By.CSS_SELECTOR, f"main a[href='{C.LOGIN_PATH}'")
    # fmt: on


class ForgotPasswordPage(BasePage, Locators):
    PAGE_PATH = C.FORGOT_PASSWORD_PATH

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def restore(self, email):
        PM.fill_text_input(self.driver, self.L_EMAIL_INPUT, email)
        PM.click_element(self.driver, self.L_RESTORE_BUTTON)

    def click_login_link(self):
        PM.click_element(self.driver, self.L_LOGIN_LINK)
