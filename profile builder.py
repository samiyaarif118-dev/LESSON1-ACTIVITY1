class pet:
    print("this is pet profile")

obj = pet()

class petprofile:
    category = "pet"

    def __init__(self,name,animal_type,age,favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food

pet1 = petprofile("buddy","dog",3,"meat")
pet2 = petprofile("milo","cat",2,"fish")

print("pet1 profile picture:",pet1.name)
print("pet1 profile picture:",pet1.animal_type)
print("pet1 profile picture:",pet1.age)
print("pet1 profile picture:",pet1.favourite_food)

print("pet2 profile picture:",pet2.name)
print("pet2 profile picture:",pet2.animal_type)
print("pet2 profile picture:",pet2.age)
print("pet2 profile picture:",pet2.favourite_food)