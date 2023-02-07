
# 1 Test - expected result -> Button "Guest login" should be work

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


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

time.sleep(2) #sleep for 2 sec
assert "Add car" in driver.page_source
driver.close()