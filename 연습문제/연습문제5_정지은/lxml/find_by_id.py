from bs4 import BeautifulSoup
with open("index.html","r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    # print(soup.find("ul", attrs={"id":"mylist"}))
    print(soup.find("ul",id= "mylist"))
'''
<ul id="mylist" style="width:150px">
<li>Solaris</li>
<li>FreeBSD</li>
<li>Debian</li>
<li>NetBSD</li>
<li>Windows</li>
</ul>
'''

'''
<ul id="mylist" style="width:150px">
<li>Solaris</li>
<li>FreeBSD</li>
<li>Debian</li>
<li>NetBSD</li>
<li>Windows</li>
</ul>
'''
