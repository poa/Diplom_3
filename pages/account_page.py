from selenium.webdriver.common.by import By

from .const import PagePath as PP
from .base_page import BasePage


class Locators:
    # fmt: off
    L_ORDER_HISTORY_BOX  = (By.CSS_SELECTOR , "main div[class^='OrderHistory']")
    L_ORDER_HISTORY_LINK = (By.CSS_SELECTOR , f"main nav a[href='{PP.ORDER_HISTORY}'")
    L_PROFILE_BOX        = (By.CSS_SELECTOR , "main div[class^='Profile_profile']")
    L_PROFILE_LINK       = (By.CSS_SELECTOR , f"main nav a[href='{PP.PROFILE}'")
    L_CANCEL_BUTTON      = (By.CSS_SELECTOR , "main button[class*='type_secondary'")
    L_LOGOUT_BUTTON      = (By.CSS_SELECTOR , "main nav button[class^='Account_button'")
    L_SAVE_BUTTON        = (By.CSS_SELECTOR , "main button[class*='type_primary'")
    # fmt: on


class AccountPage(BasePage, Locators):
    PAGE_PATH = PP.ACCOUNT

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self._is_loaded_locator = self.L_PROFILE_BOX

    def is_profile_page_loaded(self):
        return self.is_loaded(self.L_PROFILE_BOX, PP.PROFILE)

    def is_order_history_page_loaded(self):
        return self.is_loaded(self.L_ORDER_HISTORY_BOX, PP.ORDER_HISTORY)

    def click_cancel_button(self):
        self.click_element(self.L_CANCEL_BUTTON)

    def click_save_button(self):
        self.click_element(self.L_SAVE_BUTTON)

    def click_profile_link(self):
        self.click_element(self.L_PROFILE_LINK)

    def click_order_history_link(self):
        self.click_element(self.L_ORDER_HISTORY_LINK)

    def click_logout_button(self):
        self.click_element(self.L_LOGOUT_BUTTON)
