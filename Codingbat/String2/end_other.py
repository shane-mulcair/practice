def end_other(a, b):
    aL = a.lower()
    bL = b.lower()
    if aL == bL:
        return True
    alength = len(aL)
    blength = len(bL)
    if aL[-blength:] == bL or bL[-alength:] == aL:
        return True
    else:
        return False


print "shane"[0:2]  # first two letters
print "shane"[:2]  # first two letters
print "shane"[2:]  # from second to end
print "shane"[-1:]  # only last letter
print "shane"[:-1]  # except last letter
