from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.get("https://www.footlocker.ca/en/release-dates")
# #col
# products = driver.find_element(By.CLASS_NAME,"c-release-calender-details")
# print(products.text)
# driver.quit()
try:
    driver.get("https://www.footlocker.ca/en/release-dates")
    productPage = driver.find_element(By.CLASS_NAME, "c-release-calender-details")
    products = productPage.find_elements(By.CLASS_NAME, "ReleaseCalendar-Products")
    for product in products:
        info = product.find_elements(By.CLASS_NAME,"col")
        print(info)
except:
    driver.quit()
