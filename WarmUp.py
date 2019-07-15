from bs4 import BeautifulSoup

import urllib.request
from urllib.request import urlopen
import requests
import json
import time

# setup request 
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

while True:

    #Make request
    priceReq = urlopen(url)

    #Read JSON from API request
    priceJSON = json.load(priceReq)

    rate = priceJSON["bpi"]["USD"]["rate"]

    print("$" + rate)
    time.sleep(10)



#Soup stuff
#req2 = requests.get(url)

#Obtain html string for requested url
#htmlstring2 = req2.text

#Use BeautifulSoup to parse html string
#soup = BeautifulSoup(htmlstring2, 'html.parser')

#print(soup.prettify())

#print(soup.title)
