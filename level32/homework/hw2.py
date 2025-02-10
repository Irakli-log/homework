nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new= []

for i in  range(len(nums)):
        if nums[i] % 2 == 0:
                new.append(nums[i])
print(new)