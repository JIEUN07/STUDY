from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    contents =f.read()
    soup = BeautifulSoup(contents, 'lxml')
    print(soup.select_one("#mylist"))
    # soup안 mylist 출력

'''
<ul id="mylist" style="width:150px">
<li>Solaris</li>
<li>FreeBSD</li>
<li>Debian</li>
<li>NetBSD</li>
<li>Windows</li>
</ul>
'''