word = input("Enter the word")
for i in word:
    if i== "a":
        print("a found")
        break
    else:
        print(i)


word = input("Enter the word")
for i in word:
    if i =="c":
        continue
    else:
        print(i)


number = 10
for i in range(11):
    if i ==5:
        continue
    else:
        print(i)


number = 10
for x in range(number):
    if x %20 ==0:
        print("fist")
    elif x %7 ==0:
        pass
    elif x %5 ==0:
        print("five")
    elif x %3 ==0:
        print("three")
    else:
        print(x)

    




