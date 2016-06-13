def string_bits(instr):
    counter=0
    output=""
    while counter<len(instr):
        if counter%2==0 or counter==0:
            output+=instr[counter]
        counter+=1
    return output

print string_bits("Hello")