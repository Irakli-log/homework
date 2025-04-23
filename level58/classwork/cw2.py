text1 = "HELLO WORLD"
print(text1.lower())  

text2 = "PyThOn Is AwEsOmE"
print(text2.lower()) 

text3 = "123 ABC"
print(text3.lower())  


#lower() ყველა სიმბოლოს გარდაქმნის პატარა მცირე ასოებად არაბგეროვნებს არ ეხება მაგ რიცხვებს



text1 = "hello"
print(text1.upper())  

text2 = "Python3 is Fun"
print(text2.upper()) 

text3 = "Already UPPER?"
print(text3.upper())  


#upper() ყველა ასოს გარდაქმნის დიდ ასოებად რიცხვებსა და სხვა სიმბოლოებს არ ეხება



text1 = "hello world"
print(text1.capitalize())

text2 = "pYTHON IS FUN"
print(text2.capitalize())

text3 = "123abc"
print(text3.capitalize())


# capitalize() მხოლოდ პირველი ასოს აქცევს დიდად და ყველა სხვა სიმბოლოს მცირედ პატარა ასოებად


text1 = "hello world"
print(text1.find("o"))

text2 = "Find the word 'the'"
print(text2.find("the"))  

text3 = "no match here"
print(text3.find("z"))  


# find() აბრუნებს ინდექსს ადგილ მდებარეობას სადაც პირველად აღმოჩნდა მოძებნილი
# სიმბოლო ან სიტყვა თუ ვერ იპოვა  აბრუნებს -1


