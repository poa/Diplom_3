from selenium.webdriver.common.by import By

from .const import Constants as C
from .tools import PageMethods as PM

from .base_page import BasePage


class Locators:
    # fmt: off
    L_NAME_INPUT        = (By.XPATH, "//main//label[text()='Имя']/../input[@type='text']")
    L_EMAIL_INPUT       = (By.XPATH, "//main//label[text()='Email']/../input[@type='text']")
    L_PASSWORD_INPUT    = (By.CSS_SELECTOR, "main input[type='password']")
    L_REGISTER_BUTTON   = (By.CSS_SELECTOR, "main button")
    L_LOGIN_LINK        = (By.CSS_SELECTOR, f"main a[href='{C.LOGIN_PATH}'")
    # fmt: on


class RegisterPage(BasePage, Locators):
    PAGE_PATH = C.REGISTER_PATH

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def register(self, name, email, password):
        PM.fill_text_input(self.driver, self.L_NAME_INPUT, name)
        PM.fill_text_input(self.driver, self.L_EMAIL_INPUT, email)
        PM.fill_text_input(self.driver, self.L_PASSWORD_INPUT, password)
        PM.click_element(self.driver, self.L_REGISTER_BUTTON)

    def click_login_link(self):
        PM.click_element(self.driver, self.L_LOGIN_LINK)
