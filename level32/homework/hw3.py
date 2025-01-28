nums = [1, 546, 456, 123]


max = nums[0]


for i in range(len(nums)):
    if nums[i] > max:
        max = nums[i]

print(max)
