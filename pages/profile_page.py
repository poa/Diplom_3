from selenium.webdriver.common.by import By

from .const import Constants as C
from .tools import PageMethods as PM

from .account_nav_comp import AccountNavComp
from .base_page import BasePage


class Locators:
    # fmt: off
    L_CANCEL_BUTTON     = (By.CSS_SELECTOR, "main button[class*='type_secondary'")
    L_SAVE_BUTTON       = (By.CSS_SELECTOR, "main button[class*='type_primary'")
    # fmt: on


class ProfilePage(BasePage, Locators):
    PAGE_PATH = C.ACCOUNT_PATH

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.nav = AccountNavComp(driver)

    def click_cancel_button(self):
        PM.click_element(self.driver, self.L_CANCEL_BUTTON)

    def click_save_button(self):
        PM.click_element(self.driver, self.L_SAVE_BUTTON)

