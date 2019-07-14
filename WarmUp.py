from bs4 import BeautifulSoup

import urllib.request
from urllib.request import urlopen
import requests

# setup request 
url = "https://www.coinbase.com/price"

#Make request
req2 = requests.get(url)

#Obtain html string for requested url
htmlstring2 = req2.text

#Use BeautifulSoup to parse html string
soup = BeautifulSoup(htmlstring2, 'html.parser')

#print(soup.prettify())

print(soup.title)
