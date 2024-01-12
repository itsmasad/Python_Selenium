from selenium import webdriver

# Path to the ChromeDriver executable
# chrome_driver_path = 'C:\\Users\\Asad\\Desktop\\Python Selenium\\chromedriver.exe'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to a website
driver.get('https://www.google.com')

# Close the browser window
driver.quit()
