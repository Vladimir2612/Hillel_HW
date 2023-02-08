# All tests one by one for Home-work №33 in this file "test_base.py"
# 1 Test - expected result -> Button "Guest login" should be work
# 2 Test - expected result -> Button "Guest login" should be on the page
# 3 Test - expected result -> Button are presents on page
# 4 Test - expected result -> Word "Hillel" should be on the Title
# 5 Test - expected result -> When you click on the "Contacts" button, go to contacts below

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def test_button_gest_login_work():
    options = Options()
    options.add_argument("start-maximized"); # open Browser in maximized mode
# options.add_argument("disable-infobars"); # disabling infobars
# options.add_argument("--disable-extensions"); # disabling extensions
# options.add_argument("--disable-gpu"); # applicable to windows os only
# options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
    options.add_argument("--no-sandbox")
# options.add_argument("headless")

# START DRIVER
# driver = webdriver.Chrome('/home/dima/Завантаження/Hillel/chromedriver', options=options)
    driver = webdriver.Chrome(service=Service('C:\Selenium\QA\chromedriver.exe'), options=options)

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver.get("https://www.python.org/")
    driver.get("https://qauto2.forstudy.space/")

#time.sleep(2) #sleep for 2 sec

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")
    elem = driver.find_element(By.XPATH, "//button[@class='header-link -guest']")
# elem = driver.find_element(By.NAME, "q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
    goButton = driver.find_element(By.XPATH, "//button[@class='header-link -guest']")
#goButton = driver.find_element(By.XPATH, "Xpath=//button[@class='header-link -guest']")
    goButton.click()
    assert "Add car" in driver.page_source
    time.sleep(2) #sleep for 2 sec
#assert "Add car" in driver.page_source
    driver.close()

#next test

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

def test_button_gest_login_present():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(full_path + 'chromedriver'), options=options)

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


from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def test_buttons_are_presents():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")

    # START DRIVER

    driver = webdriver.Chrome(service=Service('/home/dima/Завантаження/Hillel/chromedriver'), options=options)

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")

    # GET ATTRIBUTE
    # signIn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).get_attribute("value")

    # CLICK by clickable
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()

    # CLICK be presense
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()

    elements = driver.find_elements(By.XPATH, '//button')
    print(len(elements))
    assert len(elements) > 0
    # elem = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")
    # elem.click()

    # goButton = driver.find_element(By.ID, "submit")
    # goButton.click()

    # assert "No results found." not in driver.page_source
    driver.close()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def test_d():
    options = Options()
    options.add_argument("start-maximized");  # open Browser in maximized mode
    # options.add_argument("disable-infobars"); # disabling infobars
    # options.add_argument("--disable-extensions"); # disabling extensions
    # options.add_argument("--disable-gpu"); # applicable to windows os only
    # options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service('C:\Selenium\QA\chromedriver.exe'), options=options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")
    # driver.get("https://qauto2.forstudy.space/")

    assert "Hillel" in driver.title
    time.sleep(2)  # sleep for 2 sec

    driver.close()


from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def test_go_to_contacts():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")

    # START DRIVER

    driver = webdriver.Chrome(service=Service('C:\Selenium\QA\chromedriver.exe'), options=options)

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto2.forstudy.space/")

    # CLICK by clickable
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//nav/button[2]"))).click()

    time.sleep(3)
    # GET ATTRIBUTE
    # signIn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).get_attribute("formcontrolname")
    # signIn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "signinEmail"))).get_attribute("formcontrolname")
    # print(signIn)

    # CLICK be presense
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()

    # elem = driver.find_element(By.XPATH, "//div[2]/button[2]")
    # elem.click()

    # goButton = driver.find_element(By.ID, "submit")
    # goButton.click()

    assert "Contacts" in driver.page_source
    driver.close()
