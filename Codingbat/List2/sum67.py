def sum67(nums):
    sixflag = False
    total = 0
    for n in range(len(nums)):
        if nums[n] == 6:
            sixflag = True
        elif sixflag and nums[n] == 7:
            sixflag = False
        elif not sixflag and nums[n] != 6:
            total += nums[n]
    return total


print sum67([1, 2, 2])
print sum67([1, 2, 2, 6, 99, 99, 7])
print sum67([1, 1, 6, 7, 2])
