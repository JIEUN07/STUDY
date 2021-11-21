from bs4 import BeautifulSoup
import requests as req
resp = req.get("http://www.something.com")
soup = BeautifulSoup(resp.text, 'lxml')
print(soup.title)
print(soup.title.text)
print(soup.title.parent)


# <title>Something.</title>
# Something.
# <head><title>Something.</title></head>