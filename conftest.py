import pytest
from selenium import webdriver


# @pytest.fixture
# def firefox():
#     


@pytest.fixture(params=["Firefox", "Chrome"])
def driver(request):
    _Driver = getattr(webdriver, request.param)
    _Options = getattr(webdriver, f"{request.param}Options")
    options = _Options()
    options.add_argument("--headless")
    options.add_argument("--width=1280")
    options.add_argument("--height=1024")
    driver = _Driver(options=options)
    yield driver
    driver.quit()
