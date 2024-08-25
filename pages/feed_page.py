from selenium.webdriver.common.by import By

from .const import PagePath as PP, PageTitle as PT
from .tools import PageMethods as PM

from .base_page import BasePage


class Locators:
    # fmt: off
    L_PAGE_TITLE    = (By.XPATH        , f"//main//h2[text()='{PT.FEED}']")
    L_LATEST_ORDER  = (By.CSS_SELECTOR , "main li:first-of-type>a")
    L_TOTAL_COUNTER = (By.XPATH        , "//p[contains(text(),'за все время')]/../p[starts-with(@class,'OrderFeed_number')]")
    L_DAILY_COUNTER = (By.XPATH        , "//p[contains(text(),'за сегодня')]/../p[starts-with(@class,'OrderFeed_number')]")
    L_ORDER_ID      = (By.CSS_SELECTOR , f"p[class*='text text_type_digits'")
    # fmt: on


class FeedPage(BasePage, Locators):
    PAGE_PATH = PP.FEED

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self._is_loaded_locator = self.L_PAGE_TITLE

    def get_order_id(self):
        order_element = PM.find_present_element(self.driver, self.L_LATEST_ORDER)
        id_element = PM.find_present_element(
            self.driver, order_element.find_element(*self.L_ORDER_ID)
        )

        return id_element.text
