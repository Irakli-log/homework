def divide_numbers(a, b):
    if b == 0:
        print("ნულზე გაყოფა შეუძლებელია!")
    else:
        print("რიცხვების განაყოფი არის:", a / b)

num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

divide_numbers(num1, num2)
