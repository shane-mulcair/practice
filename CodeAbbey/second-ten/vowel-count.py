f=open("C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\\vowel_count.txt")
vowelcount=[]
for line in f:
    total=0
    for x in line:
        if x in 'aeiouy':
            total += 1
    vowelcount.append(total)
print " ".join(str(x) for x in vowelcount)