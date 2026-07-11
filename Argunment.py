def total_bill(bill_amount, tip_perc):
    total = bill_amount * (1+0.01*tip_perc)
    total = round(total,2)
    print("Please pay:" ,total)

total_bill(1000,20)


def cube(number):
    return number*number*number
def by_three(number):
    if number%3 == 0:
        return cube(number)
    else:
        return False
print(by_three(8))
print(by_three(27))
print(by_three(9))


def factorial(x):
    '''this is a recursive function to find factorial of an integer'''
    if x == 1 or x == 0:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("Factorial of 5 is", factorial(5))
print("Factorial of 6 is", factorial(6))
print("Factorial of 7 is", factorial(7))
print("Factorial of 8 is", factorial(8))
  
  