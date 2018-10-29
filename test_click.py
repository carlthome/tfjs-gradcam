import os

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

# TODO Also test with Firefox.

driver = Chrome('chromedriver')
driver.get('https://carlthome.github.io/tfjs-gradcam')

# Try loading a new image.
element = WebDriverWait(driver, 10).until(element_to_be_clickable((By.ID, 'imageButton')))
element.click()

# Try loading another model.
element = WebDriverWait(driver, 10).until(element_to_be_clickable((By.ID, 'modelSelect')))
select = Select(element)
select.select_by_visible_text('DenseNet121')

driver.quit()