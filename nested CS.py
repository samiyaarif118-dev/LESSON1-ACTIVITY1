#exam eligility
computer_sci = input("Did you take the computer sacience course? y/n: ")
if computer_sci == "y":
    fee_balance = int(input("Enter fee bal: "))
    if fee_balance == 0:
        attendance = int(input("Enter attendance %: "))
        if attendance >= 75:
            print("you are allowed")
        else:
            print("Not allowed")
    else:
        print("Not allowed. Must clear fee")
else:
    print("Not allowed. Must take computer science course")


print("What do you prefer")
print("1. Car")
print("2. Bike")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("1. Mercedes")
    print("2. BMW")
    choice2 =(input("Enter your choice: "))
    if choice2 == "1":
        print("You chose Mercedes")
    else:
        print("You chose BMW")
else:
    print("1. Heavy bike")
    print("2. Racing bike")
    choice3 = input("Enter your choice: ")
    if choice3 == "1":
        print("You chose Heavy bike")
    else:
        print("You chose Racing bike")

    



