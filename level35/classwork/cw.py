num = [ 34, 43, 56, 77, 87, 23, 18, 99, 70, 66 ]

sum_number = []

for i in range(len(num)):
    if num[i] % 2 ==0:
        sum_number += [num[i]]

    print(sum_number)