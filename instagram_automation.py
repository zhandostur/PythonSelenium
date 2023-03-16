import random

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pickle


service = Service(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=service)
# title = driver.titl

username = '87071819477'
password = 'zhandos2003'

try:
#     driver.implicitly_wait(0.5)
#     username_input = driver.find_element(by=By.NAME, value="username")
#     username_input.clear()
#     time.sleep(5)
#
#     username_input.send_keys(username)
#
#     password_input = driver.find_element(by=By.NAME, value="password")
#     password_input.clear()
#     time.sleep(4)
#     password_input.send_keys(password)
#     time.sleep(3)
#     password_input.send_keys(Keys.ENTER)
#

#     pickle.dump(driver.get_cookies(), open('cookies', 'wb'))

    driver.get("https://www.instagram.com/")
    time.sleep(5)

    for cookie in pickle.load(open('cookies', 'rb')):
        driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()

    time.sleep(10)
    driver.execute_script("document.getElementsByClassName('_a9-- _a9_1')[0].click()")
    # driver.execute_script("document.getElementsByClassName('_a9-- _a9_1')[0].click()")

    time.sleep(12)
    go_message = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div')
    go_message.click()
    time.sleep(13)
    in_message = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div[1]')
    in_message.click()
    time.sleep(3)
    count = 1
    for i in range(100):
        input_message = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        time.sleep(random.randint(2, 3))
        input_message.send_keys(f'Я люблю тебя {count}')
        input_message.send_keys(Keys.ENTER)
        count += 1
    time.sleep(500)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()



