f=open('C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\min_of_two.txt')
mins=[]
for line in f:
    a,b=line.split(" ")
    mins.append(min(int(a),int(b)))
print " ".join(str(x) for x in mins)