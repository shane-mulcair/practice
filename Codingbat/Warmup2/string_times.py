def string_times(instr, n):
    output=""
    counter=0
    while counter<n:
        output+=instr
        counter+=1
    return output

print string_times("Hi",5)