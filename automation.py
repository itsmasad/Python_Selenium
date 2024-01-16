import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Path to the ChromeDriver executable
# chrome_driver_path = 'C:\\Users\\Asad\\Desktop\\Python Selenium\\chromedriver.exe'


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to a website
driver.get("http://www.google.com")

# wait untill the element arrives
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_field = driver.find_element(By.CLASS_NAME, "gLFyf")
# Clear the input field
input_field.clear()

input_field.send_keys("Muhammad Asad" + Keys.ENTER)

# wait untill the element arrives
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Muhammad Asad"))
)

# Its gonna search if the text "Muhammad Asad" is presence in any kind of link
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Muhammad Asad")
link.click

time.sleep(5)

# Close the browser window
driver.quit()
