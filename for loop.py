n = int(input("Enter the value of n: "))
sum = 0

for i in range(1, n+1):
    sum = sum + i
    print("The sum is: ", sum)

string = input("Enter a word")
string2 = ("")

for char in string:
    string2 = char + string2
    print("The original: ", string)
    print("The reversed: ", string2)

n = int(input("Enter the starting point: "))
for i in range(n, 0, -1):
    print(i)