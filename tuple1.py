tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

tuplex = (4, 6, 2, 8, 1, 9)
print(tuplex)

tuplex = tuplex + (7,)
print(tuplex)

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

tuplex = (2, 4, 5, 6, 8, 8, 9, 3)
_slice = tuplex[3:5]
print(_slice)
_slice = tuplex[:6]
print(_slice)



def palind(r):
    e = len(r) -1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r = (1, 2, 3, , 3, 2, 1)
if(palind(r)):
    print("The tuple is Flip-flop")
else:
    print("The tuple is not Flip-flop")



