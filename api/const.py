API_PATH = "/api"


class Endpoints:
    # fmt: off
    AUTH_LOGIN      = "/auth/login"
    AUTH_LOGOUT     = "/auth/logout"
    AUTH_REGISTER   = "/auth/register"
    AUTH_TOKEN      = "/auth/token"
    AUTH_USER       = "/auth/user"

    INGREDIENTS     = "/ingredients"

    ORDERS          = "/orders"
    ORDERS_ALL      = "/orders/all"

    PASSWORD_RESET  = "/password-reset"
    # fmt: on


class ErrorMessages:
    # auth related
    AUTH_DATA_INCOMPLETE = "Email, password and name are required fields"
    WRONG_AUTH_DATA = "email or password are incorrect"
    USER_EXISTS = "User already exists"
    NEED_AUTHORIZATION = "You should be authorised"

    # orders related
    NO_INGREDIENTS = "Ingredient ids must be provided"
    INCORRECT_INGREDIENTS = "One or more ids provided are incorrect"
