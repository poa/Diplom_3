from data import Data
from pages.const import IngredientType as IT
from pages.main_page import MainPage


def make_order(main_page: MainPage, data: Data):
    bun = data.get_ingredient(IT.BUNS)
    filling = data.get_ingredient(IT.FILLINGS)
    sauce = data.get_ingredient(IT.SAUCES)

    main_page.add_ingredient_to_order(bun)
    main_page.add_ingredient_to_order(filling)
    main_page.add_ingredient_to_order(sauce)
    main_page.click_make_order_button()
    main_page.wait_loading()
    order_id = main_page.get_modal_order_id()
    main_page.close_open_modal_container()
    return order_id
