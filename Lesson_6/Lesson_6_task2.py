from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

name= driver.find_element(By.ID, "newButtonName")
name.send_keys("SkyPro")

Button=driver.find_element(By.ID, "updatingButton")
Button.click()
updated_button_text = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))

button_text = driver.find_element(By.ID, "updatingButton").text
print(button_text)

driver.quit()
