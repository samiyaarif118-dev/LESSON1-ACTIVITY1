class animal:
    animals = "cow"
    print("the animal is:", animals)
obj1 = animal()

class vehicel:
    def __init__(self,maximumspeed,mileage):
        self.maximumspeed = maximumspeed
        self.mileage = mileage
obj2 = vehicel(280,12000)
print("maximum:", obj2.maximumspeed )
print("mileage:", obj2.mileage)

class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj3 = parrot("king",7)
obj4 = parrot("queen",6)
print("name:",obj3.name)
print("age:",obj3.age)
print("name:",obj4.name)
print("age:",obj4.age)
        



        



