def max_end3(nums):
    if len(nums) == 3:
        if nums[0] >= nums[2]:
            return [nums[0], nums[0], nums[0]]
        elif nums[2] >= nums[0]:
            return [nums[2], nums[2], nums[2]]
