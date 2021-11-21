from bs4 import BeautifulSoup

with open("index.html","r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    print(soup.select("li:nth-of-type(3)"))
    # soup안 li의 3번째를 출력

# [<li>Debian</li>]