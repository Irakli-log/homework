def add(a, b):
    result = a + b
    print(result)

def subtract(a, b):
    result = a - b
    print(result)

def multiply(a, b):
    result = a * b
    print(result)

def divide(a, b):
    if b != 0:
        result = a / b
        print(result)
    else:
        print("ნულზე გაყოფა შეუძლებელია ")

add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)
