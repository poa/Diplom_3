import allure
import tools

from pages.const import IngredientType as IT
from pages.feed_page import FeedPage
from pages.account_page import AccountPage
from pages.main_page import MainPage


class TestCostructor:
    @allure.title("Test open constructor page from profile")
    def test_open_constructor_from_account_successful(self, authorized):
        account_page = AccountPage(authorized)
        main_page = MainPage(authorized)

        account_page.open_page()
        account_page.click_header_constructor_link()

        assert main_page.is_loaded()

    @allure.title("Test open order feed from constructor page")
    def test_open_feed_page_from_constructor_successful(self, authorized):
        feed_page = FeedPage(authorized)

        feed_page.click_header_feed_link()

        assert feed_page.is_loaded()

    @allure.title("Test ingredient details opens successfully")
    def test_click_ingredient_opens_details_successful(self, authorized, data):
        main_page = MainPage(authorized)

        main_page.click_ingredient(ingredient=data.get_ingredient(IT.BUNS))

        assert main_page.is_modal_container_open()

    @allure.title("Test ingredient details closes successfully")
    def test_close_ingredient_details_successful(self, authorized, data):
        main_page = MainPage(authorized)

        main_page.click_ingredient(ingredient=data.get_ingredient(IT.BUNS))
        main_page.close_open_modal_container()

        assert main_page.is_modal_container_open() is False

    @allure.title("Test adding ingredient to burger increases it's counter")
    def test_add_ingredient_increased_counter(self, authorized, data):
        main_page = MainPage(authorized)
        bun = data.get_ingredient(IT.BUNS)

        init_counter = main_page.get_ingredient_counter(bun)
        main_page.add_ingredient_to_order(bun)
        new_counter = main_page.get_ingredient_counter(bun)

        assert new_counter > init_counter

    @allure.title("Test authorized user can crate order")
    def test_authorised_user_can_create_order_successful(self, authorized, data):
        main_page = MainPage(authorized)

        tools.make_order(main_page, data)
        main_page.click_make_order_button()

        assert main_page.is_modal_container_open()
