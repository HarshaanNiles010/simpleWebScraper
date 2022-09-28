from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait


def siteScraper():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    try:
        driver.get("https://www.footlocker.ca/en/category/new-arrivals.html")
        driver.find_element(By.CLASS_NAME,"ProductCard").click()
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"Buttons--stackOnMobile"))
        )
        #products = driver.find_element(By.CLASS_NAME,"ProductDetails-form__info")
        driver.find_element(By.CSS_SELECTOR,"[aria-label='Size: 09.0']").click()
        #products.click()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "//button[@class='Button ProductDetails-form__action'][.='Add To Cart']"))
        )
        driver.find_element(By.XPATH,"//button[@class='Button ProductDetails-form__action'][.='Add To Cart']").click()
        #print(products.text)
        #print(products.text)


        #productPage = driver.find_element(By.CLASS_NAME, "SearchResults")
        #product = productPage.find_element(By.CLASS_NAME,"ProductCard")
        #product.click()
        #wait = WebDriverWait(driver, 10)
        #element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Buttons--stackOnMobile')))
        #ids = product.find_elements(By.ID,"main")
        #print(ids)
        #cart = driver.find_element(By.CLASS_NAME,"Button Button--alt")


    except Exception as e:
        print(f'error detail {e}')

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


# cardVerify(cardPath)
siteScraper()
