#   1) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ჯამი


num = int(input("ჩაწერეთ ცოფრი: "))

sum = 0

for i in range(1, num + 1):
    sum += i
print(sum)