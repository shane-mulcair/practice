f=open('C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\max_of_array.txt')
maxi=0
mini=0
for x in f.readline().split():
    if int(x)>maxi:
        maxi=int(x)
    elif int(x)<mini:
        mini=int(x)
print maxi,mini
