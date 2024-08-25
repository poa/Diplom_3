import time

from pages.const import IngredientType as IT
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestMain:
    def test_open_constructor_from_account_successful(self, authorized):
        login_page = LoginPage(authorized)
        main_page = MainPage(authorized)

        login_page.open_page()
        login_page.click_header_constructor_link()

        assert main_page.is_loaded()

    def test_open_feed_page_from_constructor_successful(self, authorized):
        feed_page = FeedPage(authorized)

        feed_page.click_header_feed_link()

        assert feed_page.is_loaded()

    def test_click_ingredient_opens_details_successful(self, authorized, data):
        main_page = MainPage(authorized)

        main_page.click_ingredient(ingredient=data.get_ingredient(IT.BUNS))

        assert main_page.is_modal_container_open()

    def test_close_ingredient_details_successful(self, authorized, data):
        main_page = MainPage(authorized)

        main_page.click_ingredient(ingredient=data.get_ingredient(IT.BUNS))
        main_page.close_open_modal_container()

        # result = main_page.is_modal_container_open()
        assert main_page.is_modal_container_open() is False

    def test_add_ingredient_increased_counter(self, authorized, data):
        main_page = MainPage(authorized)
        bun = data.get_ingredient(IT.BUNS)

        init_counter = main_page.get_ingredient_counter(bun)
        main_page.add_ingredient_to_order(bun)
        time.sleep(3)
        new_counter = main_page.get_ingredient_counter(bun)

        assert init_counter < new_counter

    def test_authorised_user_can_create_order_successful(self, authorized, data):
        main_page = MainPage(authorized)
        bun = data.get_ingredient(IT.BUNS)
        filling = data.get_ingredient(IT.FILLINGS)
        sauce = data.get_ingredient(IT.SAUCES)

        main_page.add_ingredient_to_order(bun)
        main_page.add_ingredient_to_order(filling)
        main_page.add_ingredient_to_order(sauce)
        main_page.click_make_order()

        assert main_page.is_modal_container_open()

