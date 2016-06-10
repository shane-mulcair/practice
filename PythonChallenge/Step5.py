import urllib
import re
y="12345"
for x in range(1,400):
    f=urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+y)
    output= f.read()
    print output
    y=re.sub(r'\D',"",output)
    print y
