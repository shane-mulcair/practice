def front_times(instr, n):
    if len(instr) < 3:
        input2=instr
    else:
        input2=instr[0:3]
    output = ""
    counter = 0
    while counter < n:
        output += input2
        counter += 1
    return output
print front_times("hello",5)