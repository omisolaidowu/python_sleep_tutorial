import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the browser (Chrome)
driver = webdriver.Chrome()

# Go to the target page
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")

# Mimic a human pause before interacting with the page
time.sleep(random.uniform(3, 6))

# Try to find the element after the simulated human delay
next_button = driver.find_element(By.CLASS_NAME, "carousel-control-next-icon")

# Scroll to the element's position
driver.execute_script(
    "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });",
    next_button,
)

# Mimic a random human pause after scrolling to the element's position
time.sleep(random.uniform(3, 7))

# Click the next button
next_button.click()

# Mimic another human pause before quitting
time.sleep(random.uniform(4, 8))

driver.quit()
