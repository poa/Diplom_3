import pytest
from selenium import webdriver

from const import Constants as C
from api.auth import AuthAPI


@pytest.fixture(scope="session")
def test_user():
    with AuthAPI(C.APP_URL,**C.TEST_USER) as test_user:
        test_user.register()
        yield test_user


# @pytest.fixture(params=["Firefox", "Chrome"])
@pytest.fixture(params=["Chrome"], scope="function")
def driver(test_user, request):
    _Driver = getattr(webdriver, request.param)
    _Options = getattr(webdriver, f"{request.param}Options")
    options = _Options()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1280,1280")
    options.add_argument("--window-position=2560,32")
    driver = _Driver(options=options)
    driver.get(C.APP_URL)
    yield driver
    driver.quit()
