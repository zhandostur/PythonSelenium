import time
from selenium import webdriver

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
driver = webdriver.Firefox()

driver.get('https://duckduckgo.com')