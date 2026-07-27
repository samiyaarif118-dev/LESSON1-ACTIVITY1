import random
import math
lucky_number = random.randint(1, 10)
print("Your lucky number is:", lucky_number)
print()


fun_choices = ["Play a game", "solve a puzzle", "Read a book", "Go for a walk"]
activity = random.choice(fun_choices)
print("Your random activity is:", activity)
print()


secret_number = random.randint(1, 5)
while True:
    guess = int(input("Guess the secret number (1-5): "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number!")
        break
    else:
        print("Wrong guess! Try again.")
print()


decimal_number = float(input("Enter a decimal number: "))
print("Ceiling:", math.ceil(decimal_number))
print("Floor:", math.floor(decimal_number))
print()


number = float(input("Enter a number: "))

print("Absolute value:", math.fabs(number))
print("Copy sign:", math.copysign(number, -1))

print()


num1 = int(input("Enter first number for GCD: "))
num2 = int(input("Enter second number for GCD: "))

print("GCD:", math.gcd(num1, num2))