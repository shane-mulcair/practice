def monkey_trouble(a_smile, b_smile):
    if a_smile:
        if b_smile:
            return True
        else:
            return False
    else:
        if b_smile:
            return False
        else:
            return True

print monkey_trouble(True,True)
print monkey_trouble(False,False)
print monkey_trouble(True,False)
