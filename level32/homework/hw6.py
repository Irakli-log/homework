numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_sum = 0
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        even_sum += numbers[i]


print(even_sum)