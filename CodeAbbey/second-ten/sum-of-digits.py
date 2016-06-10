f = open("C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\sum_of_digits.txt")
output = []
for line in f:
    a, b, c = line.split()
    total = (int(a)*int(b))+int(c)
    sum = 0
    for x in str(total):
        sum += int(x)
    output.append(sum)
print " ".join(str(y) for y in output)