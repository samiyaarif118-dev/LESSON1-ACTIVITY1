empty_list = []
marks = [85, 92, 78, 90, 85]
print(" Marks:", marks)

list1 = [85, 92, 78, 90, 85]
list2 = list1 * 3  
print(" Lists:", list2)

total_marks = len(marks)
print("Total marks count:", total_marks)

index1 = marks[0]   
index2 = marks[-1]  

print("First Mark:", index1)
print("Last Mark:", index2)

first_three_marks = marks[0:3]  
marks = marks[::-1]    

print("First 3 marks:", first_three_marks)
print("Reversed Marks:", marks)

for mark in marks:
    mark_text = str(mark) 
    
    if mark_text[0] == mark_text[-1]:
        print(mark, " First and last digit MATCH!")
    else:
        print(mark, " First and last digit DO NOT match.")

total_sum = 0
for mark in marks:
    total_sum = total_sum + mark

print("Total Sum of Marks:", total_sum)

average = total_sum / len(marks)
print("Average Mark:", average)

sorted_marks = sorted(marks)
print("Sorted Marks List:", sorted_marks)

smallest = sorted_marks[0]  
largest = sorted_marks[-1]  

print("Smallest Mark:", smallest)
print("Largest Mark:", largest)