tree1 = 37
tree2 = 59
tree3 = 30
tree4 = 69
total = tree1 + tree2 + tree3 + tree4
print("total height: ",total)
average = total / 4
print("average height: ",average)

amount = int(input("Enter the amount: "))
n100 = amount // 100
amount = amount % 100
n50 = amount // 50
amount = amount % 50
n20 = amount // 20
print("Numberof 100s: ", n100)
print("Number of 50s: ", n50)
print("Number of 20s: ", n20)

maths = int(input("Enter the marks of maths: "))
science = int(input("Enter the marks of science: "))
english = int(input("Enter the marks of english: "))
physics = int(input("Enter the marks of physics: "))
chemistry = int(input("Enter the marks of chemistry: "))
total_marks = maths + science + english + physics + chemistry
print("Total marks: ", total_marks)
percentage = (total_marks / 500) * 100
print("Percentage: ", percentage)