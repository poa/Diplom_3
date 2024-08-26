import allure
import pytest
import tools

from pages.feed_page import FeedPage
from pages.account_page import AccountPage
from pages.main_page import MainPage


class TestOrderFeed:
    def test_open_order_details_successful(self, driver):
        feed_page = FeedPage(driver)

        feed_page.open_page()
        feed_page.click_last_order()
        feed_page = MainPage(driver)

        assert feed_page.is_modal_container_open()

    def test_user_orders_present_in_order_feed_successful(self, user_with_orders):
        feed_page = FeedPage(user_with_orders)
        account_page = AccountPage(user_with_orders)

        account_page.open_order_history_page()
        last_user_order_id = account_page.get_last_order_id()
        feed_page.open_page()
        last_feed_order_id = feed_page.get_all_order_ids()

        assert last_user_order_id in last_feed_order_id

    @pytest.mark.parametrize("period", ["total", "daily"])
    def test_new_order_increases_order_counter_successful(self, authorized, data, period):
        allure.dynamic.title(f"Test {period} counter is increased with new order")
        feed_page = FeedPage(authorized)
        main_page = MainPage(authorized)

        get_counter = getattr(feed_page, f"get_{period}_counter")

        feed_page.open_page()
        init_counter = get_counter()
        main_page.open_page()
        tools.make_order(main_page, data)
        feed_page.open_page()
        new_counter = get_counter()

        assert new_counter > init_counter

    def test_new_order_present_in_processing_successful(self, authorized, data):
        feed_page = FeedPage(authorized)
        main_page = MainPage(authorized)

        main_page.open_page()
        order_id = tools.make_order(main_page, data)
        feed_page.open_page()
        in_work_orders = feed_page.get_in_work_orders()

        assert order_id in in_work_orders
