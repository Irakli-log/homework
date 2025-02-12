def check(number):
    if number > 0:
        print("რიცხვი დადებითია.")
    elif number < 0:
        print("რიცხვი უარყოფითია.")
    else:
        print("რიცხვი ნულია.")

num = float(input("შეიყვანეთ რიცხვი: "))

check(num)
