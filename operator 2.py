x = 7
y = 6
if x > 0 and y > 0:
    print("the number are positive")

x = 4
y = -2
if x > 0 or y > 0:
        print("either of the number is positive")

weight = float(input("enter the weight in kgs:"))
height = float(input("enter the height in cm:"))
BMI = weight / (height/100)**2
if BMI < 18.5:
      print("you are underweight")
elif BMI < 24.5:
      print("you are healthy")
elif BMI <29.5:
      print("you are overweight")
else: 
      print("you are obese")
      


        
