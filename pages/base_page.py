import allure
from selenium.webdriver.common.by import By

from .const import PagePath as PP
from .tools import PageMethods as PM


class Locators:
    # fmt: off
    L_HEADER_ACCOUNT_LINK = (By.CSS_SELECTOR , f"header a:is([class][href='{PP.ACCOUNT}'])")
    L_HEADER_FEED_LINK    = (By.CSS_SELECTOR , f"header a:is([class][href='{PP.FEED}'])")
    L_HEADER_MAIN_LINK    = (By.CSS_SELECTOR , f"header a:is([class][href='{PP.MAIN}'])")
    L_HEADER_BURGER_LOGO  = (By.CSS_SELECTOR , f"header a:not([class])[href='{PP.MAIN}']")

    L_MODAL_ANIMATION        = (By.CSS_SELECTOR , "div[class^='Modal_modal'] img[class*='loading']")
    L_MODAL_ANIMATION_OPEN   = (By.CSS_SELECTOR , "div[class^='Modal_modal_open'] img[class*='loading']")
    L_MODAL_CONTAINER        = (By.CSS_SELECTOR , "section[class^='Modal_modal']>div[class*='container']")
    L_MODAL_CONTAINER_OPEN   = (By.CSS_SELECTOR , "section[class^='Modal_modal_open']>div[class*='container']")
    L_MODAL_LOADING_OVERLAY  = (By.CSS_SELECTOR , "section div[class^='Modal_modal_overlay__']")
    L_MODAL_CLOSE_BUTTON     = (By.CSS_SELECTOR , " button[class*='close_modified']")
    L_ORDER_ID               = (By.CSS_SELECTOR , "[class*='text text_type_digits'")
    # fmt: on


class BasePage(Locators):
    PAGE_PATH = PP.MAIN

    def __init__(self, driver):
        self.driver = driver
        self.app_url = PM.get_app_url(self.driver)
        self.page_url = self.app_url + self.PAGE_PATH
        self._is_loaded_locator = ()

    # common methods
    @allure.step("Open page")
    def open_page(self):
        self.wait_loading()
        PM.open_page(self.driver, self.page_url)

    @allure.step("Check page is loaded")
    def is_loaded(self, locator=None, path=None) -> bool:
        self.wait_loading()
        _locator = locator if locator is not None else self._is_loaded_locator
        _path = path if path is not None else self.PAGE_PATH
        result = PM.is_visible(self.driver, _locator) and self.current_path == _path
        return result

    def click_element(self, locator):
        self.wait_loading()
        PM.click_element(self.driver, locator)

    def fill_text_input(self, locator, text):
        self.wait_loading()
        PM.fill_text_input(self.driver, locator, text)

    @property
    def current_url(self):
        return PM.get_current_url(self.driver)

    @property
    def current_path(self):
        return PM.get_current_path(self.driver)

    # header section
    @allure.step("Click header profile link")
    def click_header_account_link(self):
        self.click_element(self.L_HEADER_ACCOUNT_LINK)

    @allure.step("Click header orders feed link")
    def click_header_feed_link(self):
        self.click_element(self.L_HEADER_FEED_LINK)

    @allure.step("Click header constructor link")
    def click_header_constructor_link(self):
        self.click_element(self.L_HEADER_MAIN_LINK)

    @allure.step("Click header burger logo")
    def click_header_burger_logo(self):
        self.click_element(self.L_HEADER_BURGER_LOGO)

    # modal section
    @allure.step("Close modal container")
    def close_open_modal_container(self):
        self.wait_loading()
        open_container = PM.find_visible_element(self.driver, self.L_MODAL_CONTAINER)
        open_container.find_element(*self.L_MODAL_CLOSE_BUTTON).click()

    @allure.step("Check if modal container is open")
    def is_modal_container_open(self):
        result = PM.is_visible(self.driver, self.L_MODAL_CONTAINER_OPEN)
        return result

    @allure.step("Check if modal animation is open")
    def is_modal_animation_open(self):
        result = PM.is_displayed(self.driver, self.L_MODAL_ANIMATION_OPEN)
        return result

    @allure.step("Wait for loading animation")
    def wait_loading(self):
        result = (
            PM.is_invisible(self.driver, self.L_MODAL_ANIMATION)
            and self.is_modal_animation_open() is False
        )
        return result

    @allure.step("Get order id from modal container")
    def get_modal_order_id(self):
        self.wait_loading()
        result = None
        if self.is_modal_container_open:
            modal = PM.find_visible_element(self.driver, self.L_MODAL_CONTAINER)
            id = modal.find_element(*self.L_ORDER_ID)
            result = "{:07d}".format(int(id.text))

        return result
