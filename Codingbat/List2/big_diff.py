def big_diff(nums):
    largest = 0
    smallest = 10000000
    for n in range(len(nums)):
        if largest < nums[n]:
            largest = nums[n]
        if smallest > nums[n]:
            smallest = nums[n]
    return largest - smallest


print big_diff([10, 3, 5, 6])
print big_diff([7, 2, 10, 9])
print big_diff([2, 10, 7, 2])
