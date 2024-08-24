from selenium.webdriver.common.by import By

from .const import Constants as C, IngredientType as IT
from .tools import PageMethods as PM

from .base_page import BasePage


class Locators:
    # fmt: off
    L_INGREDIENT_LINK       = (By.CSS_SELECTOR, f"main nav a[href='{C.INGREDIENT_PATH}/%s']")
    # L_INGREDIENT_COUNTER    = (By.CSS_SELECTOR, f"main nav a[href='{C.INGREDIENT_PATH}/%s'] p[class^='counter']")
    L_INGREDIENT_COUNTER    = (By.CSS_SELECTOR, f"p[class^='counter']")
    L_INGREDIENT_TYPE_TAB   = (By.XPATH, "//main//span[text()='%s']")
    L_DROP_ZONE             = (By.CSS_SELECTOR, "main section>ul")
    L_LOGIN_BUTTON          = (By.XPATH, "//main//button[text()='Войти в аккаунт']")
    L_MAKE_ORDER_BUTTON     = (By.XPATH, "//main//button[text()='Оформить заказ']")

    # fmt: on


class MainPage(BasePage, Locators):
    PAGE_PATH = C.MAIN_PATH

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_buns_tab(self):
        locator = (self.L_INGREDIENT_TYPE_TAB[0], self.L_INGREDIENT_TYPE_TAB[1] % IT.BUNS)
        PM.click_element(self.driver, locator)

    def click_fillings_tab(self):
        locator = (self.L_INGREDIENT_TYPE_TAB[0], self.L_INGREDIENT_TYPE_TAB[1] % IT.FILLINGS)
        PM.click_element(self.driver, locator)

    def click_sauces_tab(self):
        locator = (self.L_INGREDIENT_TYPE_TAB[0], self.L_INGREDIENT_TYPE_TAB[1] % IT.SAUCES)
        PM.click_element(self.driver, locator)

    def click_ingredient(self, ingredient):
        locator = (self.L_INGREDIENT_LINK[0], self.L_INGREDIENT_LINK[1] % ingredient)
        PM.click_element(self.driver, locator)

    def get_ingredient_counter(self, ingredient):
        # locator = (self.L_INGREDIENT_COUNTER[0], self.L_INGREDIENT_COUNTER[1] % ingredient)
        # counter_element = PM.find_present_element(self.driver, locator)

        locator = (self.L_INGREDIENT_LINK[0], self.L_INGREDIENT_LINK[1] % ingredient)
        ingredient_element = PM.find_present_element(self.driver, locator)
        counter_element = PM.find_present_element(self.driver, ingredient_element.find_element(*self.L_INGREDIENT_COUNTER))

        return counter_element.text

    def drag_ingredient(self, ingredient):
        src = (self.L_INGREDIENT_LINK[0], self.L_INGREDIENT_LINK[1] % ingredient)
        dst = self.L_DROP_ZONE

        PM.drag_element(self.driver, src, dst)
