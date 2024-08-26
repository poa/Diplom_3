import allure
from selenium.webdriver.common.by import By

from .const import PagePath as PP, PageTitle as PT
from .tools import PageMethods as PM

from .base_page import BasePage


class Locators:
    # fmt: off
    L_PAGE_TITLE         = (By.XPATH        , f"//main//h1[text()='{PT.FEED}']")
    L_ORDER_LIST         = (By.CSS_SELECTOR , "main ul[class^='OrderFeed_list']")
    L_ORDERS_IN_WORK     = (By.CSS_SELECTOR , "main ul[class^='OrderFeed_orderListReady'] li[class*='text_type_digits']")
    L_LAST_ORDER         = (By.CSS_SELECTOR , "main li[class^='OrderHistory_listItem']:first-of-type")
    L_ORDER_LIST_ITEM_ID = (By.CSS_SELECTOR , " div[class^='OrderHistory_textBox']>p[class*='text_type_digits']")
    L_TOTAL_COUNTER      = (By.XPATH        , "//p[contains(text(),'за все время')]/../p[starts-with(@class,'OrderFeed_number')]")
    L_DAILY_COUNTER      = (By.XPATH        , "//p[contains(text(),'за сегодня')]/../p[starts-with(@class,'OrderFeed_number')]")
    L_ORDER_ID           = (By.CSS_SELECTOR , f"p[class*='text text_type_digits'")
    # fmt: on


class FeedPage(BasePage, Locators):
    PAGE_PATH = PP.FEED

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self._is_loaded_locator = self.L_PAGE_TITLE

    @allure.step("Show latest order details")
    def click_last_order(self):
        self.click_element(self.L_LAST_ORDER)

    # complex methods
    @allure.step("Get ID of latest order showed in order feed")
    def get_last_order_id(self):
        self.wait_loading()
        order = PM.find_present_element(self.driver, self.L_LAST_ORDER)
        order_id_elem = order.find_element(*self.L_ORDER_LIST_ITEM_ID)
        return order_id_elem.text.strip("#")

    @allure.step("Get list of orders showed in order feed")
    def get_all_order_ids(self):
        self.wait_loading()
        order_ids = []
        items = PM.find_present_elements(self.driver, self.L_ORDER_LIST_ITEM_ID)
        for i in items:
            order_ids.append(i.text.strip("#"))

        return order_ids

    @allure.step("Get list of orders in work")
    def get_in_work_orders(self):
        self.wait_loading()
        order_ids = []
        items = PM.find_present_elements(self.driver, self.L_ORDERS_IN_WORK)
        for i in items:
            order_ids.append(i.text)

        return order_ids

    @allure.step("Get total orders counter")
    def get_total_counter(self):
        counter_elem = PM.find_present_element(self.driver, self.L_TOTAL_COUNTER)
        return counter_elem.text

    @allure.step("Get daily orders counter")
    def get_daily_counter(self):
        counter_elem = PM.find_present_element(self.driver, self.L_DAILY_COUNTER)
        return counter_elem.text
