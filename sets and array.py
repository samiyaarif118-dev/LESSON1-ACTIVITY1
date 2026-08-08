basket1 = {"apple", "banana", "apple", "orange"}
basket2 = {"watermelon", "apple", "banana", "kiwi" , "watermelon"}
print("this is basket1: ",basket1)
print("this is basket2: ",basket2)

basket1.add("grapes")
print("grapes added to basket1: ",basket1)

common_fruits = basket1.intersection(basket2)
print("common fruits  :",common_fruits)

import array as arr 
fruits_count = arr.array("i",[3, 7, 9 ,4 ])
print("fruits count in array: ",fruits_count)

fruits_count.insert(0, 1)
fruits_count.append(6)
print("fruits count after adding numbers: ",fruits_count)

countofsix = fruits_count.count(6)
print("counting of number 6: ",countofsix)

fruits_count.reverse()
print("reversed array: ",fruits_count)

print("fruit basket organiser")
print("this is basket1 : ", basket1)
print("this is basket2 : ", basket2)
print("common fruits : ",common_fruits)
print("fruits count : ",fruits_count)
print("count of six number : ",countofsix)

