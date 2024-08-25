import pytest
from selenium import webdriver

from const import Constants as C
from data import Data as D
from api.auth import AuthAPI

from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def data():
    data = D()
    yield data
    del data


@pytest.fixture(scope="session")
def test_user():
    with AuthAPI(C.APP_URL, **C.TEST_USER) as test_user:
        test_user.register()
        yield test_user


# @pytest.fixture(params=["Firefox", "Chrome"], scope="function")
# @pytest.fixture(params=["Firefox"], scope="function")
@pytest.fixture(params=["Chrome"], scope="function")
def driver(request, test_user):
    _Driver = getattr(webdriver, request.param)
    _Options = getattr(webdriver, f"{request.param}Options")
    options = _Options()
    # options.add_argument("--headless")
    # options.add_argument("--user-data-dir=R:/browsers/webdriver")
    # options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--window-size=1280,1280")
    # options.add_argument("--window-position=2560,32")
    driver = _Driver(options=options)
    driver.set_window_position(2560, 32)
    driver.set_window_size(1280, 1280)

    driver.get(C.APP_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def authorized(driver, test_user):
    login_page = LoginPage(driver)
    login_page.open_page()
    if login_page.is_loaded():
        login_page.login(email=test_user.email, password=test_user.password)
        yield driver
    else:
        raise RuntimeError("Login failed")

