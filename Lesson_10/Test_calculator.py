import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage
# Импортируем класс


@pytest.fixture
def driver() -> webdriver.Chrome:
    """ Инициализация WebDriver (например, Chrome)
    :return: Экземпляр WebDriver (Chrome) """
    driver = webdriver.Chrome()
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    yield driver
    driver.quit()


@allure.title("Тест на сложение")
@allure.description("Проверка функции сложения в калькуляторе с ожиданием")
@allure.feature("Сложение")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    calculator = CalculatorPage(driver)

    # Установка задержки в 46 секунд
    calculator.set_delay(46)

    # Выполнение сложения 7 + 8
    calculator.click_button('1')
    calculator.click_button('+')
    calculator.click_button('2')
    calculator.click_button('=')

    # Ожидание, пока результат не будет отображен
    calculator.wait_for_result(3)

    # Получение результата и проверка
    result = calculator.get_result()
    assert result == '3', "Ожидалось, что результат будет '3', но получено '{result}'"