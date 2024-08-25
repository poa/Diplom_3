from selenium.webdriver.common.by import By

from .const import PagePath as PP

from .account_nav_comp import AccountNavComp
from .base_page import BasePage


class Locators:
    L_ORDER_HISTORY_BOX = (By.CSS_SELECTOR, "main div[class^='OrderHistory']")
    pass


class OrederHistoryPage(BasePage, Locators):
    PAGE_PATH = PP.ORDER_HISTORY

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.nav = AccountNavComp(driver)
        self._is_loaded_locator = self.L_ORDER_HISTORY_BOX

    def open_page(self):
        BasePage.open_page(self)
        self.nav.click_order_history_link()


