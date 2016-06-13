f=open("C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\\arithmetic_progression.txt")
sums=[]
for line in f:
    A,B,target=line.split()
    total=int(A)
    counter=1
    while counter<int(target):
        total+=(int(A)+counter*int(B))
        counter+=1
    sums.append(total)
print " ".join(str(x) for x in sums)
