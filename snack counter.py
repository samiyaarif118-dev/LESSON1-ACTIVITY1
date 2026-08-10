snack1 = {"pizza", "burger", "fries", "burger"}
snack2 = {"icecream", "cake", "burger", "fries", "cake"}
print("this is snack1: ",snack1)
print("this is snack2: ",snack2)

snack1.add("banana")
print("banana added to snack1: ",snack1)

common_snacks = snack1.intersection(snack2)
print("common snacks :",common_snacks)

import array as arr
snacks_count = arr.array("i",[6,7,1,8])
print("snacks count in array: ",snacks_count)

snacks_count.insert(0,2)
snacks_count.append(8)
print("snacks count after adding numbers: ",snacks_count)

snacks = snacks_count.count(8)
print("counting of number 8: ",snacks)

snacks_count.reverse()
print("reversed array: ",snacks_count)

print("snack counter organiser")
print("this is snack1 : ", snack1)
print("this is snack2 : ", snack2)
print("common snacks : ",common_snacks)
print("snacks count : ",snacks_count)
print("count of eight : ",snacks)
