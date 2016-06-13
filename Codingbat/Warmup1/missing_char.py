def missing_char(instr, n):
    output=""
    counter=0
    for x in instr:
        if counter !=n:
            output+=x
        counter+=1
    return output

print missing_char("shane", 1)
