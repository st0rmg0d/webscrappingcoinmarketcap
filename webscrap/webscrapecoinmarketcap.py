from bs4 import BeautifulSoup
from selenium import webdriver
import requests


def getdata(url):
    r = requests.get(url)
    return r.text   

url = ("https://coinmarketcap.com/currencies/bitcoin/news/")

driver = webdriver.Chrome()
driver.get(url)

source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')
data = ''

for data in soup.find_all("p"):
    print(data.get_text())

