import allure

from const import Constants as C
# from data import TestData as TD
from pages.header_comp import HeaderComponent
from tools import PageMethods as PM


class Locators:
    pass


class BasePage(Locators):
    PAGE_PATH = C.MAIN_PATH

    def __init__(self, driver):
        self.driver = driver
        self.Header = HeaderComponent(self.driver)
        self.page_url = C.APP_URL + self.PAGE_PATH

    @allure.step("Open page")
    def open_page(self):
        PM.open_page(self.driver, self.page_url)

    @allure.step("Get current url")
    def get_current_url(self):
        return PM.get_current_url(self.driver)
