
from random import choice

from const import Constants as C
from pages.const import IngredientType as IT


class Data:
    def __init__(self):
        self.ingredients = {IT.BUNS: C.BUNS, IT.FILLINGS: C.FILLINGS, IT.SAUCES: C.SAUCES}

    def get_ingredient(self, ingredient_type):
        return choice(self.ingredients[ingredient_type])
