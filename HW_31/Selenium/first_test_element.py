
# 2 Test - expected result -> Button "Guest login" should be on the page

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os

absolute_path = os.path.dirname(__file__)
relative_path = "/"
full_path = os.path.join(absolute_path, relative_path)
# print(f'Path: {full_path}')
# print('Path:'+ full_path)

options = Options()
options.add_argument("start-maximized")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(full_path+'chromedriver'), options=options)

user = "guest"
password = "welcome2qauto"
driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")
# driver.get("https://qauto2.forstudy.space/")

time.sleep(3)


def is_element_present(self, how, what):
    try:
        self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e:
        return False
    return True


element = driver.find_element(By.XPATH, '//button[@class="header-link -guest"]')
if element.is_displayed():
    print("Element found")
    not_found = True
else:
    print("Element not found")
    not_found = False

assert not_found

driver.close()
