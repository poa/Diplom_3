import enum


class Constants:
    TIMEOUT = 7


class IngredientType(enum.StrEnum):
    # fmt: off
    BUNS     = "Булки"
    FILLINGS = "Начинки"
    SAUCES   = "Соусы"
    # fmt: on


class PagePath(enum.StrEnum):
    # fmt: off
    ACCOUNT          = "/account"
    FEED             = "/feed"
    RECOVER_PASSWORD = "/forgot-password"
    INGREDIENT       = "/ingredient"
    LOGIN            = "/login"
    MAIN             = "/"
    ORDER_HISTORY    = "/account/order-history"
    PROFILE          = "/account/profile"
    REGISTER         = "/register"
    RESET_PASSWORD   = "/reset-password"
    # fmt: on


class PageTitle(enum.StrEnum):
    # fmt: off
    FEED             = "Лента заказов"
    LOGIN            = "Вход"
    MAIN             = "Соберите бургер"
    RECOVER_PASSWORD = "Восстановление пароля"
    REGISTER         = "Регистрация"
    RESET_PASSWORD   = "Восстановление пароля"
    # fmt: on

