import allure

from .const import PagePath as PP
from .header_comp import HeaderComponent
from .tools import PageMethods as PM


class BasePage:
    PAGE_PATH = PP.MAIN

    def __init__(self, driver):
        self.driver = driver
        self.header = HeaderComponent(self.driver)
        self.app_url = driver.current_url.strip("/")
        self.page_url = self.app_url + self.PAGE_PATH
        self._is_loaded_locator = ()

    @allure.step("Open page")
    def open_page(self):
        PM.open_page(self.driver, self.page_url)

    @property
    def is_loaded(self):
        result = (
            PM.is_displayed(self.driver, self._is_loaded_locator)
            and self.current_path == self.PAGE_PATH
        )
        return result

    @allure.step("Get current url")
    @property
    def current_url(self):
        return PM.get_current_url(self.driver)

    @property
    def current_path(self):
        return PM.get_current_path(self.driver)