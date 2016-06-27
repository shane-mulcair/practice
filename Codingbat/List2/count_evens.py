def count_evens(nums):
    s = 0
    for n in nums:
        if n % 2 == 0:
            s += 1
    return s
