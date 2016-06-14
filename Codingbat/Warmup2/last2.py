def last2(instr):
    if len(instr) > 2:
        counter = 0
        substr = instr[-2:]
        for x in range(len(instr[:-1])-1):
            if instr[x:x+2] == substr:
                counter += 1
        return counter
    else:
        return 0

print last2("xaxxaxaxx")

