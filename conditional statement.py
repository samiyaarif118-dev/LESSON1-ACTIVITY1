num = 2 
if num > 0:
    print(num, " is a positive number")

num = -6 
if num < 0:
        print(num, " is a negative number")

actual_cost = float(input("please enter the actual cost: "))
sale_amount = float(input("please enter the sale amount: "))

if (sale_amount > actual_cost):
      profit = sale_amount - actual_cost
      print("total profit = ", profit)
else:
      print("No profit")

number = int(input("enter a number to check: "))
print("number to be checked is: ", number)

if number%2 == 0:
            print(number, "is an even number")
else:
            print(number, "is an odd number")