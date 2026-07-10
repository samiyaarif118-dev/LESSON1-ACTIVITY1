def wishes():
    print("Happy Birthday!")
wishes()

def weather():
    print("It's very hot during ", summer)
    print("It's is pleasant during:", winter)
summer = "summer"
winter = "winter"
weather()

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("Please pick an option to be performed")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Enter option (1/2/3/4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if option == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif option == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif option == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif option == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
