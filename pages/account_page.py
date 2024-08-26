import allure

from selenium.webdriver.common.by import By

from .const import PagePath as PP
from .tools import PageMethods as PM
from .base_page import BasePage


class Locators:
    # fmt: off
    L_ORDER_HISTORY_BOX  = (By.CSS_SELECTOR , "main div[class^='OrderHistory']")
    L_ORDER_HISTORY_LINK = (By.CSS_SELECTOR , f"main nav a[href='{PP.ORDER_HISTORY}'")
    L_LAST_ORDER         = (By.CSS_SELECTOR , "main li[class^='OrderHistory_listItem']:last-of-type")
    L_ORDER_LIST_ITEM_ID = (By.XPATH        , ".//div[starts-with(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]")
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

    @allure.step("Click cancel button")
    def click_cancel_button(self):
        self.click_element(self.L_CANCEL_BUTTON)

    @allure.step("Click save button")
    def click_save_button(self):
        self.click_element(self.L_SAVE_BUTTON)

    @allure.step("Click profile link")
    def click_profile_link(self):
        self.click_element(self.L_PROFILE_LINK)

    @allure.step("Click order history link")
    def click_order_history_link(self):
        self.click_element(self.L_ORDER_HISTORY_LINK)

    @allure.step("Click logout button")
    def click_logout_button(self):
        self.click_element(self.L_LOGOUT_BUTTON)

    # complex methods
    def open_order_history_page(self):
        self.open_page()
        self.click_order_history_link()

    @allure.step("Get last order ID")
    def get_last_order_id(self):
        self.wait_loading()
        order = PM.find_present_element(self.driver, self.L_LAST_ORDER)
        order_id_elem = order.find_element(*self.L_ORDER_LIST_ITEM_ID)
        return order_id_elem.text.strip("#")

    @allure.step("Get list of orders from order history")
    def get_all_order_ids(self):
        self.wait_loading()
        order_ids = []
        items = PM.find_present_elements(self.driver, self.L_ORDER_LIST_ITEM_ID)
        for i in items:
            order_ids.append(i.text.strip("#"))

        return order_ids
