def make_chocolate(small, big, goal):
    if goal > (small + big * 5):
        return -1
    elif (goal % 5 > small):
        return -1
    else:
        if (goal % (big * 5)) == 0:
            return 0
        elif big * 5 > goal:
            return (goal - ((big * 5) - 5))
        else:
            return goal - big * 5


print make_chocolate(6, 2, 7)
