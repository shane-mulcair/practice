def make_bricks(small, big, goal):
    if ((goal - (goal % 5)) / 5 <= big + small and goal % 5 <= small) or goal <= small:
        return True
    else:
        return False


print make_bricks(3, 1, 8)
print make_bricks(3, 1, 9)
print make_bricks(3, 2, 10)
print make_bricks(3, 2, 9)
