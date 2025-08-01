import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator = CalculatorPage(driver)

    calculator.set_delay(45)

    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')


    calculator.wait_for_result(15)

    result = calculator.get_result()
    assert result == '15', f"Результат не = '15', but got '{result}'"