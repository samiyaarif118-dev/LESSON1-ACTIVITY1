try:
    age = int(input("Enter your age"))
    print("Your age is" ,age)
    if age %2 ==0:
         print("Your age is EVEN")
    else:
         print("your age is ODD")
except ValueError:
    print("The number you enter is not integer please enter integer")