n = int(input("Enter the value of n: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print("Total: " ,sum)

i = 0
while i >= 0:
    print(i)
    i=i+1

#Armstrong
num = int(input("Enter a number to check: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum+= digit ** 3
temp = temp // 10
if num == sum:
    print(num, " is an armstrong number")
else:
    print(num, " is not an armstrong number")
    

    