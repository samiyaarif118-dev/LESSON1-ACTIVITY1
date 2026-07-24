import random
num = str(random.randint(1,9))
print("I will generate a number from 1 to 9 and you have to guess the number 1 digit at a time")
playing = True
while playing:
    number = (input("Enter the number:"))
    if number == num:
        print("you won")
        print("The number is",num)
        break
    else:
     print("Try again") 



