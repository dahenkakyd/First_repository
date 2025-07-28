from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


for i in range(4):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, f"//img[{i+1}]"))
    )

img = driver.find_elements(By.TAG_NAME, 'img')

if len(img) >= 3:
    third_image_src = img[2].get_attribute('src')
    print("Атрибут src третьего изображения:", third_image_src)
else:
    print("На странице меньше трех изображений.")


driver.quit()