import enum


class Constants:
    TIMEOUT = 5

    # PATH constants
    ACCOUNT_PATH = "/account"
    PROFILE_PATH = "/account/profile"
    ORDER_HISTORY_PATH = "/account/order-history"
    FEED_PATH = "/feed"
    LOGIN_PATH = "/login"
    MAIN_PATH = "/"
    REGISTER_PATH = "/register"
    FORGOT_PASSWORD_PATH = "/forgot-password"
    RESET_PASSWORD_PATH = "/reset-password"
    INGREDIENT_PATH = "/ingredient"


class IngredientType(enum.StrEnum):
    BUNS = "Булки"
    FILLINGS = "Начинки"
    SAUCES = "Соусы"
