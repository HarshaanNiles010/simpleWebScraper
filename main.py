from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


def siteScraper():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    try:
        driver.get("https://www.footlocker.ca/en/release-dates")
        productPage = driver.find_element(By.CLASS_NAME, "c-release-calender-details")
        products = productPage.find_elements(By.CLASS_NAME, "ReleaseCalendar-Products")
        results = []
        for product in products:
            info = product.find_elements(By.CLASS_NAME, "col")
            results.append([i.text for i in info])
        print(results)
    except:
        print("Encountered some problem closing the web page")
        driver.quit()
    finally:
        time.sleep(5)
        driver.quit()


cardPath = r"C:\Users\harshaan\PycharmProjects\pythonProject1\cards.txt"


# making sure the card entered will actually work
def cardVerify(cardPath):
    card = []
    try:
        f = open(cardPath, "r", encoding='utf-8')
        card.append(f.readline())
        print(card)
        f.close()
    except:
        print("Process failed")
    finally:
        return


cardVerify(cardPath)
