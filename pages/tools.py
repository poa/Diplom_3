from typing import Tuple
from urllib.parse import urlparse

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
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
    def get_current_path(driver):
        return urlparse(driver.current_url).path

    @staticmethod
    def get_app_url(driver):
        scheme, netloc, path, params, query, fragment = urlparse(driver.current_url)
        app_url = f"{scheme}://{netloc}"
        return app_url

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
    def check_invisibility(driver, locator, timeout=TIMEOUT):
        result = WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element(locator),
            message=f"Not found: {locator}",
        )
        return result

    @staticmethod
    def scroll_to_element(driver, target: WebElement | Tuple[str, str], timeout=TIMEOUT):
        if isinstance(target, Tuple):
            element = PageMethods.find_present_element(driver, target, timeout)
        else:
            element = target
        driver.execute_script("arguments[0].scrollIntoView()", element)
        WebDriverWait(driver, timeout).until(EC.visibility_of(element))

    @staticmethod
    def scroll_to_clickable_element(driver, target: WebElement | Tuple[str, str], timeout=TIMEOUT):
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
    def drag_element(
        driver,
        src: WebElement | Tuple[str, str],
        dst: WebElement | Tuple[str, str],
        timeout=TIMEOUT,
    ):
        if isinstance(dst, Tuple):
            _src = PageMethods.find_present_element(driver, src, timeout)
            _dst = PageMethods.find_present_element(driver, dst, timeout)
        else:
            _src = src
            _dst = dst

        PageMethods.scroll_to_clickable_element(driver, _src, timeout)
        ActionChains(driver).drag_and_drop(_src, _dst).perform()

    @staticmethod
    def fill_text_input(driver, locator, data):
        element = PageMethods.find_visible_element(driver, locator)
        PageMethods.click_element(driver, element)
        element.send_keys(data)

    @staticmethod
    def is_displayed(driver, locator) -> bool:
        try:
            element = PageMethods.find_present_element(driver, locator)
            result = element.is_displayed()
        except (NoSuchElementException, TimeoutException):
            result = False

        return result

    @staticmethod
    def is_visible(driver, locator) -> bool:
        try:
            element = PageMethods.find_visible_element(driver, locator)
            result = element.is_displayed()
        except (NoSuchElementException, TimeoutException):
            result = False

        return result

    @staticmethod
    def is_invisible(driver, locator):
        check_result = PageMethods.check_invisibility(driver, locator)
        if isinstance(check_result, bool):
            result = check_result
        else:
            result = False

        return result

    @staticmethod
    def switch_to_next_window(driver):
        current_window = driver.current_window_handle
        windows = driver.window_handles
        for w in windows:
            if w != current_window:
                driver.switch_to.window(w)
                break
