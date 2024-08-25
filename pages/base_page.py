import allure

from .const import PagePath as PP
from .tools import PageMethods as PM

from .header_comp import HeaderComponent
from .modal_comp import ModalComponent


class BasePage:
    PAGE_PATH = PP.MAIN

    def __init__(self, driver):
        self.driver = driver
        self.header = HeaderComponent(self.driver)
        self.modal = ModalComponent(self.driver)
        self.app_url = PM.get_app_url(self.driver)
        self.page_url = self.app_url + self.PAGE_PATH
        self._is_loaded_locator = ()

    @allure.step("Open page")
    def open_page(self):
        PM.open_page(self.driver, self.page_url)

    def is_loaded(self) -> bool:
        result = (
            PM.is_visible(self.driver, self._is_loaded_locator)
            and self.current_path == self.PAGE_PATH
        )
        return result

    def wait_loading(self):
        self.modal.wait_animation_closed()

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
