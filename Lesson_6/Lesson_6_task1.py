from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def main(driver):
    driver.maximize_window()

    driver.get()
driver.implicitly_wait(16)

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = driver.find_element(By.CSS_SELECTOR, "#content")
text_plashki= content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(text_plashki)

driver.quit()