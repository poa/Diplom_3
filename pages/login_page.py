from selenium.webdriver.common.by import By

from const import Constants as C
from tools import PageMethods as PM

from pages.base_page import BasePage


class Locators:
    # fmt: off
    L_EMAIL_INPUT       = (By.CSS_SELECTOR, "main input:is([type='text'])")
    L_PASSWORD_INPUT    = (By.CSS_SELECTOR, "main input:is([type='password'])")
    L_LOGIN_BUTTON      = (By.CSS_SELECTOR, "main button")
    L_REGISTER_LINK     = (By.CSS_SELECTOR, f"main a[href={C.REGISTER_PATH}")
    L_FORGOT_LINK       = (By.CSS_SELECTOR, f"main a[href={C.FORGOT_PASSWORD_PATH}")
    # fmt: on


class LoginPage(BasePage, Locators):
    PAGE_PATH = C.LOGIN_PATH

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def login(self, email, password):
        PM.fill_text_input(self.driver, self.L_EMAIL_INPUT, email)
        PM.fill_text_input(self.driver, self.L_PASSWORD_INPUT, password)
        PM.click_element(self.driver, self.L_LOGIN_BUTTON)

    def click_register_link(self):
        PM.click_element(self.driver, self.L_REGISTER_LINK)

    def click_forgot_link(self):
        PM.click_element(self.driver, self.L_FORGOT_LINK)
