from selenium.webdriver.common.by import By

from .const import Constants as C
from .tools import PageMethods as PM


class Locators:
    # fmt: off
    L_LOGOUT_BUTTON      = (By.CSS_SELECTOR, "main nav button[class^='Account_button'")
    L_PROFILE_LINK       = (By.CSS_SELECTOR, f"main nav a[href='{C.PROFILE_PATH}'")
    L_ORDER_HISTORY_LINK = (By.CSS_SELECTOR, f"main nav a[href='{C.ORDER_HISTORY_PATH}'")
    # fmt: on


class AccountNavComp(Locators):
    def __init__(self, driver):
        self.driver = driver

    def click_profile_link(self):
        PM.click_element(self.driver, self.L_PROFILE_LINK)

    def click_order_history_link(self):
        PM.click_element(self.driver, self.L_ORDER_HISTORY_LINK)

    def click_logout_button(self):
        PM.click_element(self.driver, self.L_LOGOUT_BUTTON)
