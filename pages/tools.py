from typing import Tuple

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .const import Constants as C


class PageMethods:
    TIMEOUT = C.TIMEOUT

    @staticmethod
    def open_page(driver, url):
        driver.get(url)

    @staticmethod
    def get_current_url(driver):
        return driver.current_url

    @staticmethod
    def find_present_element(driver, locator, timeout=TIMEOUT):
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Not found: {locator}",
        )
        return element

    @staticmethod
    def find_present_elements(driver, locator, timeout=TIMEOUT):
        elements = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Not found: {locator}",
        )
        return elements

    @staticmethod
    def find_visible_element(driver, locator, timeout=TIMEOUT):
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Not found: {locator}",
        )
        return element

    @staticmethod
    def scroll_to_element(
        driver, target: WebElement | Tuple[str, str], timeout=TIMEOUT
    ):
        if isinstance(target, Tuple):
            element = PageMethods.find_present_element(driver, target, timeout)
        else:
            element = target
        driver.execute_script("arguments[0].scrollIntoView()", element)
        WebDriverWait(driver, timeout).until(EC.visibility_of(element))

    @staticmethod
    def scroll_to_clickable_element(
        driver, target: WebElement | Tuple[str, str], timeout=TIMEOUT
    ):
        if isinstance(target, Tuple):
            element = PageMethods.find_present_element(driver, target, timeout)
        else:
            element = target
        driver.execute_script("arguments[0].scrollIntoView(false);", element)
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(element))

    @staticmethod
    def click_element(driver, target: WebElement | Tuple[str, str], timeout=TIMEOUT):
        if isinstance(target, Tuple):
            element = PageMethods.find_present_element(driver, target, timeout)
        else:
            element = target
        PageMethods.scroll_to_clickable_element(driver, element, timeout)
        element.click()

    @staticmethod
    def fill_text_input(driver, locator, data):
        element = PageMethods.find_visible_element(driver, locator)
        PageMethods.click_element(driver, element)
        element.send_keys(data)

    @staticmethod
    def is_displayed(driver, locator):
        element = PageMethods.find_present_element(driver, locator)
        return element.is_displayed()

    @staticmethod
    def switch_to_next_window(driver):
        current_window = driver.current_window_handle
        windows = driver.window_handles
        for w in windows:
            if w != current_window:
                driver.switch_to.window(w)
                break