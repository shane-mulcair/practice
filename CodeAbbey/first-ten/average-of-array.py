f = open("C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\\average_of_array.txt")
output = []
inputs = []
for line in f:
    total = 0
    counter = 0
    inputs = line.split()
    for num in inputs:
        counter += 1
        total += int(num)
    output.append(int(round(float(total)/float(counter-1))))
print " ".join(str(y) for y in output)