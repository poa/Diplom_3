from .const import Constants as C

from .account_nav_comp import AccountNavComp
from .base_page import BasePage


class Locators:
    pass


class OrederHistoryPage(BasePage, Locators):
    PAGE_PATH = C.ACCOUNT_PATH

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.nav = AccountNavComp(driver)

    def open_page(self):
        BasePage.open_page(self)
        self.nav.click_order_history_link()


