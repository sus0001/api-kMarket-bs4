from time import sleep
from bs4 import BeautifulSoup
import requests
import random


def get_ua():
    uastrings = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 "
        "Safari/600.1.25",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 "
        "Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 "
        "Safari/537.85.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
    ]
 
    return random.choice(uastrings)


headers = {'User-Agent': get_ua()}

url = "https://kalimatimarket.gov.np/#commodityPricesDailyTable"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')


def date_header_np():    
    table = soup.find('table', id='commodityDailyPrice').find('tbody').find_all('tr')    
    date = soup.find_all('div', id='commodityPricesDailyTable')
     
    for dat in date:
        return dat.find('h5').text


table = soup.find('table', id='commodityDailyPrice').find('tbody').find_all('tr')


def kalimati_market_np(value):
    # This technique is list comprehension:
    # It stores pulled data and store in lists: Less code and runs fast: It's quite powerful in Python
    lists = [(tab.find_all('td'))[value].text for tab in table]
    return lists

