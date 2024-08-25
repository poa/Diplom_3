from selenium.webdriver.common.by import By

from .const import PagePath as PP
from .tools import PageMethods as PM


class Locators:
    # fmt: off
    L_OPEN_MODAL_CONTAINER = (By.CSS_SELECTOR , f"section[class^='Modal_modal_opened']>div[class*='container']")
    L_CLOSE_BUTTON         = (By.CSS_SELECTOR,  " button[class*='close_modified']")
    L_ORDER_ID             = (By.CSS_SELECTOR , "[class*='text text_type_digits'")
    # fmt: on


class ModalComponent(Locators):
    def __init__(self, driver):
        self.driver = driver

    def close_open_modal_container(self):
        open_container = PM.find_visible_element(self.driver, self.L_OPEN_MODAL_CONTAINER)
        open_container.find_element(*self.L_CLOSE_BUTTON).click()

    @property
    def is_open(self):
        # modal = PM.find_visible_element(self.driver, self.L_OPEN_MODAL_CONTAINER)
        # result = modal.is_displayed()
        result = PM.is_visible(self.driver, self.L_OPEN_MODAL_CONTAINER)
        return result

    def get_order_id(self):
        result = None
        if self.is_open:
            modal = PM.find_visible_element(self.driver, self.L_OPEN_MODAL_CONTAINER)
            id = modal.find_element(*self.L_ORDER_ID)
            result = id.text

        return result
