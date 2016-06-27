def has22(nums):
    for n in range(len(nums)):
        if nums[n] == 2 and n + 1 < len(nums) and nums[n + 1] == 2:
            return True
    return False


print has22([])
print has22([1, 2, 2])
print has22([1, 2, 1, 2])
print has22([2, 1, 2])
