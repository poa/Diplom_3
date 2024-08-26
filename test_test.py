from const import Constants as C

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.recover_password_page import RecoverPasswordPage
from pages.register_page import RegisterPage
from pages.account_page import AccountPage


# from pages.home_page import HomePage


def test(driver):
    # fmt: off
    bp   = BasePage(driver)
    lp   = LoginPage(driver)
    recp = RecoverPasswordPage(driver)
    rp   = RegisterPage(driver)
    pp   = AccountPage(driver)
    # hp = HomePage(driver)
    # op = OrderPage(driver)
    # fmt: on

    print()
    print(f"BP:  {bp.PAGE_PATH}, {bp.page_url}")
    print(f"LP:  {lp.PAGE_PATH}, {lp.page_url}")
    print(f"FPP: {recp.PAGE_PATH}, {recp.page_url}")
    print(f"RP:  {rp.PAGE_PATH}, {rp.page_url}")
    print(f"PP:  {pp.PAGE_PATH}, {pp.page_url}")
    # print(f"\nOP:  {op.PAGE_PATH}, {op.page_url}")

    # bp.open_page()
    # bp.header.click_account_link()
    # bp.header.click_constructor_link()
    # bp.header.click_feed_link()
    # bp.header.click_burger_logo()

    # lp.open_page()
    # lp.login(C.TEST_USER.get("email"), C.TEST_USER.get("password"))
    # lp.click_register_link()
    # lp.open_page()
    # lp.click_forgot_link()

    # recp.open_page()
    # recp.recover(C.TEST_USER.get("email"))
    # recp.open_page()
    # recp.click_login_link()

    # rp.open_page()
    # rp.register(**C.TEST_USER)

    lp.open_page()
    lp.login(C.TEST_USER.get("email"), C.TEST_USER.get("password"))

    # pp.open_page()
    # pp.click_cancel_button()
    # pp.click_save_button()
    # pp.nav.click_order_history_link()
    # pp.nav.click_profile_link()
    # pp.nav.click_logout_button()

    # ohp.open_page()


    pass
