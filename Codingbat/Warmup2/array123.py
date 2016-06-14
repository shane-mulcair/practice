def array123(nums):
    return "123" in "".join(str(x) for x in nums)

print array123([1,1,2,3,4,5])