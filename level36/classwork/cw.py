def multiply_check(num1, num2):
    result = num1 * num2 
    print("ნამრავლი:", int(result))
    
    if result % 2 == 0:
        print("ნამრავლი ლუწია")
    else:
        print("ნამრავლი კენტია")


multiply_check(4, 4) 
multiply_check(6, 5)  
multiply_check(2, 2)
multiply_check(8, 3)  