f = open("C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\weighted_sum_of_digits.txt")
output = []
for x in f.readline().split():
    total=0
    counter=1
    for i in x:
        total+=(int(i)*counter)
        counter+=1
    output.append(total)
print " ".join(str(y) for y in output)