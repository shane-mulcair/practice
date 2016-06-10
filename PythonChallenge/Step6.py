import pickle
import urllib
f=urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data=pickle.load(f)
for elt in data:
    print "".join([e[1] * e[0] for e in elt])