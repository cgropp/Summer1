import requests 
from bs4 import BeautifulSoup

# access the website 
result = requests.get("http://www.math.ucsd.edu/~alpelayo/Math103A_SummerSession12019.html")

# print the accesibility 
print(result.status_code)

#print(result.headers)
# print the status 
#print(result.staus_code)

# get source code
src = result.content

soup = BeautifulSoup(src, 'lxml')

#find all the a tags
links = soup.find_all("a")
#print(links)
#print("\n")

# print the links that contain "Homework"
for link in links:
    if "Homework" in link.text:
        print(link)
        print(link.attrs['href'])


