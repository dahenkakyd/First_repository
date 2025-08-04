import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from LoginPage import LoginPage
from MainPage import MainPage
from ByPage import ByPage
from Checkout_page import Checkout_page


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()

    yield driver
    driver.quit()


def test_shop(browser):
    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    cart_page = ByPage(browser)
    checkout_page = Checkout_page(browser)

    browser.get("https://www.saucedemo.com/")

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items:
        main_page.item_to_cart(item)

    main_page.in_cart()
    cart_page.Сheckout_in_cart(items)
    cart_page.click_checkout()

    checkout_page.fill_form("Имя", "Фамилия", "123456")
    checkout_page.click_continue()

    total = checkout_page.get_total()
    assert total == "Total: $58.29", \
        f"Expected total to be $58.29, but got {total}"