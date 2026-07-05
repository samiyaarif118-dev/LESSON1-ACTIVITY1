print("Mirrored right-angled triangle")
num = int(input("Enter numbers of rows: "))
for i in range(1, num + 1):

    print(" " * (num - i), end="")
    print("*" * i)
