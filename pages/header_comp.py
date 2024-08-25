from selenium.webdriver.common.by import By

from .const import PagePath as PP, PageTitle as PT
from .tools import PageMethods as PM


class Locators:
    """Locators class
    Contains locators for header component
    """

    # fmt: off
    L_ACCOUNT_LINK = (By.CSS_SELECTOR , f"header a:is([class][href='{PP.ACCOUNT}'])")
    L_FEED_LINK    = (By.CSS_SELECTOR , f"header a:is([class][href='{PP.FEED}'])")
    L_MAIN_LINK    = (By.CSS_SELECTOR , f"header a:is([class][href='{PP.MAIN}'])")
    L_BURGER_LOGO  = (By.CSS_SELECTOR , f"header a:not([class])[href='{PP.MAIN}']")
    # fmt: on


class HeaderComponent(Locators):
    def __init__(self, driver):
        self.driver = driver

    def click_account_link(self):
        PM.click_element(self.driver, self.L_ACCOUNT_LINK)

    def click_feed_link(self):
        PM.click_element(self.driver, self.L_FEED_LINK)

    def click_main_link(self):
        PM.click_element(self.driver, self.L_MAIN_LINK)

    def click_burger_logo(self):
        PM.click_element(self.driver, self.L_BURGER_LOGO)

