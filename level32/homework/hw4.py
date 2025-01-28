numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


list  = []

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:  
       list.append(numbers[i])

print(list)
