import allure

from selenium.webdriver.common.by import By

from .const import PagePath as PP, PageTitle as PT
from .tools import PageMethods as PM

from .base_page import BasePage


class Locators:
    # fmt: off
    L_PAGE_TITLE           = (By.XPATH        , f"//main//h1[text()='{PT.MAIN}']")
    L_INGREDIENT_LINK      = (By.CSS_SELECTOR , f"main section a[href='{PP.INGREDIENT}/%s']")
    L_INGREDIENT_COUNTER   = (By.CSS_SELECTOR , f"p[class^='counter']")
    L_INGREDIENT_TYPE_TAB  = (By.XPATH        , "//main//span[text()='%s']")
    L_DROP_ZONE            = (By.CSS_SELECTOR , "main div[class*='__totalContainer']")
    L_LOGIN_BUTTON         = (By.XPATH        , "//main//button[text()='Войти в аккаунт']")
    L_MAKE_ORDER_BUTTON    = (By.XPATH        , "//main//button[text()='Оформить заказ']")
    # fmt: on


class MainPage(BasePage, Locators):
    PAGE_PATH = PP.MAIN

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self._is_loaded_locator = self.L_PAGE_TITLE

    @allure.step("Shoe ingredient details")
    def click_ingredient(self, ingredient):
        locator = (self.L_INGREDIENT_LINK[0], self.L_INGREDIENT_LINK[1] % ingredient)
        self.click_element(locator)

    @allure.step("Click make order button")
    def click_make_order_button(self):
        self.click_element(self.L_MAKE_ORDER_BUTTON)

    @allure.step("Get ingredient counter")
    def get_ingredient_counter(self, ingredient):
        self.wait_loading()
        locator = (self.L_INGREDIENT_LINK[0], self.L_INGREDIENT_LINK[1] % ingredient)
        ingredient_element = PM.find_present_element(self.driver, locator)
        counter_element = ingredient_element.find_element(*self.L_INGREDIENT_COUNTER)

        return counter_element.text

    @allure.step("Drag and drop ingredient to basket")
    def add_ingredient_to_order(self, ingredient):
        src = (self.L_INGREDIENT_LINK[0], self.L_INGREDIENT_LINK[1] % ingredient)
        dst = self.L_DROP_ZONE

        PM.drag_element(self.driver, src, dst)
