import re
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    strings = soup.find_all(string=re.compile('BSD'))
    for txt in strings:
        print("".join(txt.split()))

'''
FreeBSD
NetBSD
FreeBSDisanadvancedcomputeroperatingsystemusedtopowermodernservers,desktops,andembeddedplatforms.
'''