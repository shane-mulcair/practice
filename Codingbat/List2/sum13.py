def sum13(nums):
    s = 0
    for n in range(len(nums)):
        if nums[n] != 13:
            if n > 0:
                if nums[n - 1] != 13:
                    s += nums[n]
            else:
                s += nums[n]
    return s


# print sum13([1,2,2,1,13])
# print sum13([1,2,2,1,13])
print sum13([1, 2, 13, 2, 1, 13])
