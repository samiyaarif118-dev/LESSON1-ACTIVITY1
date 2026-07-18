try:
    number = int(input("Enter the number:"))
    print("number" ,number)
    raise ValueError
except ValueError as x:
    print("the number is not integer,enter integer" ,x)


try:
    number1 ,number2 = eval(input("Enter the two number seperated by a ,"))
    result = number1 / number2 
    print(result)
except ZeroDivisionError:
    print("zero by division is an error")
except SyntaxError:
    print("comma is missing")
except:
    print("invalid input")
else:
    print("no exception")
finally:
    print("this block will be printed no matter what")




