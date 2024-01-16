from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://orteil.dashnet.org/cookieclicker/")

# initializing the id
Cookie_id = "bigCookie"

# wait untill the language to arrives
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

# selecting english as a language and searching by text
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Wait for the cookie to arrive
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, Cookie_id))
)

# Clicking the cookie
Cookie = driver.find_element(By.ID, Cookie_id)
Cookie.click()


# Wait for 10 seconds
time.sleep(10)

# Closes the instance
driver.quit