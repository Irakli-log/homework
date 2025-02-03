def positive_or_negative():

    number = float(input("შეიყვანეთ რიცხვი: "))
    
    
    if number > 0:
        print("რიცხვი დადებითია")
    elif number < 0:
        print("რიცხვი უარყოფითია")
    else:
        print("რიცხვი ნულოვანია")

positive_or_negative()