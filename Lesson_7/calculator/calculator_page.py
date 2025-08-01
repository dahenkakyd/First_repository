from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver, 45)

    def set_delay(self, delay):
        delay_stop = self.waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_stop.clear()
        delay_stop.send_keys(delay)

    def click_button(self, button):
        button = self.waiter.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))
        )
        button.click()

    def get_result(self):
        result = (By.CSS_SELECTOR, ".screen")
        return self.waiter.until(EC.presence_of_element_located(result)).text

    def wait_for_result(self, expected_result):
        self.waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(expected_result)))