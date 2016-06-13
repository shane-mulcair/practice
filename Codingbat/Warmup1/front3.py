def front3(instr):
    if len(instr)<3:
        return instr+instr+instr
    else:
        return instr[0:3]+instr[0:3]+instr[0:3]

print front3("shane")
