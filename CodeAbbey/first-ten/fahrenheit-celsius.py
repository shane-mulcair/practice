f=open("C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\\fahrenheit_celsius.txt")
temps=[]
for x in f.readline().split():
    temps.append(round(((float(x)-32)*5.0)/9.0))
print " ".join(str(int(t)) for t in temps)