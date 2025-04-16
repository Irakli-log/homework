
def jami(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print("1-დან 5-მდე ჯამი:", jami(5))
print("1-დან 10-მდე ჯამი:", jami(10))
print("1-დან 100-მდე ჯამი:", jami(100))
