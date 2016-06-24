def make_bricks(small, big, goal):
    if goal > (small + big * 5):
        return False
    elif (goal % 5 > small):
        return False
    else:
        return True


print make_bricks(3, 1, 8)
print make_bricks(3, 1, 9)
print make_bricks(3, 2, 10)
print make_bricks(3, 2, 9)
