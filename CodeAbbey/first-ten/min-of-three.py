f=open('C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\min_of_three.txt')
mins=[]
for line in f:
    a,b,c=line.split(" ")
    mins.append(min(min(int(a),int(b)),int(c)))
print " ".join(str(x) for x in mins)