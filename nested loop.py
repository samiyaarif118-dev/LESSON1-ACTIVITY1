word = input("Enter a word: ")
char = input("Enter a letter: ")
count = 0
i = 0

while i < (len(word)):
    if word[i] == char:
        count += 1 
    i += 1

print("The letter", char, "appeared", count, "times")

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
for i in range(lower, upper+1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)

