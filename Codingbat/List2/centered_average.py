def centered_average(nums):
    total = 0
    count = 0
    largest = 0
    smallest = 1000000
    for n in range(len(nums)):
        if nums[n] < smallest:
            smallest = nums[n]
        if nums[n] > largest:
            largest = nums[n]
    for n in range(len(nums)):
        total += nums[n]
        count += 1
    print largest
    print smallest
    total -= smallest
    total -= largest
    return int(total / (count - 2))


# print centered_average([1, 2, 3, 4, 100])
# print centered_average([1, 1, 5, 5, 10, 8, 7])
# print centered_average([-10, -4, -2, -4, -2, 0])
# print centered_average([100,0,5,3,4])
print centered_average([1000, 0, 1, 99])
