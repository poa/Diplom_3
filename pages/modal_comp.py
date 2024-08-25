from selenium.webdriver.common.by import By

from .const import PagePath as PP
from .tools import PageMethods as PM


class Locators:
    # fmt: off
    L_MODAL_ANIMATION = (By.CSS_SELECTOR , "div[class^='Modal_modal'] img[class*='loading']")
    # L_MODAL_ANIMATION_OPEN = (By.CSS_SELECTOR , "div[class^='Modal_modal_open'] img[class*='loading']")
    L_MODAL_CONTAINER = (By.CSS_SELECTOR , "section[class^='Modal_modal']>div[class*='container']")
    L_MODAL_LOADING_OVERLAY        = (By.CSS_SELECTOR , "section div[class^='Modal_modal_overlay__']")
    L_CLOSE_BUTTON         = (By.CSS_SELECTOR , " button[class*='close_modified']")
    L_ORDER_ID             = (By.CSS_SELECTOR , "[class*='text text_type_digits'")
    # fmt: on


class ModalComponent(Locators):
    def __init__(self, driver):
        self.driver = driver

    def close_open_modal_container(self):
        open_container = PM.find_visible_element(self.driver, self.L_MODAL_CONTAINER)
        open_container.find_element(*self.L_CLOSE_BUTTON).click()

    def is_modal_container_open(self):
        result = PM.is_displayed(self.driver, self.L_MODAL_CONTAINER)
        return result

    def is_modal_animation_open(self):
        result = PM.is_displayed(self.driver, self.L_MODAL_CONTAINER)
        return result
    
    def wait_animation_closed(self):
        result = PM.is_invisible(self.driver, self.L_MODAL_ANIMATION)
        return result

    def get_order_id(self):
        result = None
        if self.is_modal_container_open:
            modal = PM.find_visible_element(self.driver, self.L_MODAL_CONTAINER)
            id = modal.find_element(*self.L_ORDER_ID)
            result = id.text

        return result
