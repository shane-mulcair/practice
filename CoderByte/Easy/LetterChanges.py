def LetterChanges(str):
    output = []
    output2 = []
    for x in str:
        if ord(x) >= 65 and ord(x) < 122:
            output.append(chr(ord(x)+1))
    for y in output:
        if y == "a":
            output2.append("A")
        elif y == "e":
            output2.append("E")
        elif y == "i":
            output2.append("I")
        elif y == "o":
            output2.append("O")
        elif y == "u":
            output2.append("U")
        else:
            output2.append(y)
    # code goes here
    return output2


# keep this function call here
print LetterChanges(raw_input())
















