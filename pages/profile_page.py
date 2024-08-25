from selenium.webdriver.common.by import By

from .const import Constants as C
from .const import PagePath as PP, PageTitle as PT

from .tools import PageMethods as PM

from .account_nav_comp import AccountNavComp
from .base_page import BasePage


class Locators:
    # fmt: off
    L_PROFILE_BOX   = (By.CSS_SELECTOR , "main div[class^='Profile_profile']")
    L_CANCEL_BUTTON = (By.CSS_SELECTOR , "main button[class*='type_secondary'")
    L_SAVE_BUTTON   = (By.CSS_SELECTOR , "main button[class*='type_primary'")
    # fmt: on


class ProfilePage(BasePage, Locators):
    PAGE_PATH = PP.PROFILE

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.nav = AccountNavComp(driver)
        self._is_loaded_locator = self.L_PROFILE_BOX

    def click_cancel_button(self):
        PM.click_element(self.driver, self.L_CANCEL_BUTTON)

    def click_save_button(self):
        PM.click_element(self.driver, self.L_SAVE_BUTTON)

