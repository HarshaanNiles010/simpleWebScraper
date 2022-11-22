from selenium import webdriver
from selenium.webdriver.common.by import By
import time
cardNumber = 4556534512255231
expMonth = 12
expYearLong = 2027
expYearShort = 27
CCV = 384
URL = "https://www.footlocker.ca/en/product/nike-air-max-270-mens/4205587.html"
driver = webdriver.Chrome()
try:
    driver.get(URL)
    time.sleep(3)
    driver.find_element(By.LINK_TEXT("10.0")).click()
    driver.close()
except:
    print("failed to find the element")


