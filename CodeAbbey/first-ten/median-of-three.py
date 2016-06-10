f = open('C:\Users\mulcas4\PycharmProjects\CodeAbbey\inputs\median_of_three.txt')
mins = []
for line in f:
    a, b, c = line.split(" ")
    if (int(c) > int(a) > int(b)) or ((int(c) < int(a) < int(b))):
        mins.append(int(a))
    elif (int(a) < int(b) < int(c)) or (int(a) > int(b) > int(c)):
        mins.append(int(b))
    else:
        mins.append(int(c))
print " ".join(str(x) for x in mins)
