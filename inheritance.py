class familymember:
    def __init__(self,eyecolor,height):
        self.eyecolor = eyecolor
        self.height = height


    def showtraits(self):
        print("eyecolor :",self.eyecolor)
        print("height:",self.height)


class kid(familymember):
    def __init__(self,name,age,eyecolor,height):
        self.name = name
        self.age = age
        super().__init__(eyecolor,height)


    def showtraits(self):
        print("name:",self.name)
        print("age:",self.age)


    def favouritehobby(self,hobby):
        print("favourite hobby:",hobby)


obj = kid("samiya",14,"brown","162cm")

obj.showtraits()
obj.favouritehobby("playing football")


class animals:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def pet (self):
        print("name:",self.name)
        print("color:",self.color)


class child(animals):
    def __init__(self,haircolor,eyecolor,name,color):
        self.haircolor = haircolor
        self.eyecolor = eyecolor
        super().__init__(name,color)

    def pet (self):
            print("haircolor:",self.haircolor)
            print("eyecolor:",self.eyecolor)

    def favouritehobby (self,hobby):
            print("favouritehobby:",hobby)


obj = child("black","black","puppy","black")

obj.pet()
obj.favouritehobby("walking")









        
        