def lone_sum(a, b, c):
    if a == b:
        if a == c:
            return 0
        else:
            return c
    elif b == c:
        if a == c:
            return 0
        else:
            return a
    elif a == c:
        if a == b:
            return 0
        else:
            return b
    else:
        return a + b + c
