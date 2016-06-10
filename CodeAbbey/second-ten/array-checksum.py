f=open("C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\\array_checksum.txt")
inputs=f.readline().split()
outputs=[]
result=0
for x in inputs:
    result+=int(x)
    result*=113
    result=result%10000007
print result
