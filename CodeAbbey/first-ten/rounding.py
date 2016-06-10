f=open("C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\\rounding.txt")
mins=[]
for line in f:
    a,b=line.split(" ")
    mins.append(round(float(a)/float(b)))
print " ".join(str(int(x)) for x in mins)