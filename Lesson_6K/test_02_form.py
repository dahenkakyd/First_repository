from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope="module")
def browser():

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()


def test_calculator(browser):

    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )


    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")


    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()


    result = WebDriverWait(browser, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    assert result, "Результат на экране не равен 15"