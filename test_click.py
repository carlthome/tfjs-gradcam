from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select

# TODO Also test with Firefox.

driver = Chrome('chromedriver')
driver.get('index.html')

# Try loading a new image.
driver.find_element_by_id('imageButton').click()

# Try loading another model.
select = Select(driver.find_element_by_id('classSelect'))
select.select_by_visible_text('DenseNet121')

driver.quit()