def string_splosion(instr):
    result=""
    for x in range(len(instr)):
        result+=instr[:x+1]
    return result
