import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

URL = "https://www.footlocker.ca/en/category/new-arrivals.html"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
sales = soup.find('div', attrs={'class': 'SearchResults'})
itemLinks = []
counter = 0
for row in sales.find_all('li', attrs={"class": "product-container col"}):
    reading = {}
    # reading['descr'] = row.img['alt']
    reading['link' + str(counter)] = row.a['href']
    itemLinks.append(reading)
    counter += 1


# print(ShowData)
# fileName = 'new_data.csv'
# counter = 1
# with open(fileName,'w') as f:
#     w = csv.DictWriter(f,['descr','link'])
#     counter += 1
#     w.writeheader()
#     for data in ShowData:
#         w.writerow(data)

def urlProcessing(URL1, URL2):
    URL1 = list(URL.split("/"))
    URL1 = URL1[:3]
    URL1 = "/".join(URL1)
    newURL = URL1 + URL2
    return newURL


def linkMaker(itemLinks):
    counter = 0
    itemURLS = []
    for links in itemLinks:
        itemURLS.append(urlProcessing(URL, links['link' + str(counter)]))
        counter += 1

    return itemURLS


def OpenLinks(itemURLS):
    driver = webdriver.Chrome()
    for urls in itemURLS:
        driver.get(urls)

    driver.close()


OpenLinks(linkMaker(itemLinks))
