f = open("C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\\dice_rolling.txt")
output = []
for line in f:
    i=float(line)*6
    j=int(i)+1
    output.append(j)
print " ".join(str(y) for y in output)