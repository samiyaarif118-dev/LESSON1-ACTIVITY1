x = []
print(x)
numbers = [1 ,2, 3 ,4, 5]
print(numbers)
triples = [4 ,7 , 8] *3
print(triples)

p = [100,200,300,400,500]
p = p[::-1]
print(p)

y = [8,4,9,2,7,5,0,1]
print("original list",y)
sum = 0
for i in y:
    sum = sum + i
print("sum is",sum)
average = sum / (len(y))
print(average)

y.sort()
print(y)

print("smallest value",y[0])
print("largest value",y[7])



