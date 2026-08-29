class myclass:
    __private = 30
    def __privatemethod(self):
        print("This is my class")


    def hello(self):
        print("the private attribute is:",myclass.__private)


obj = myclass()
obj.hello()



class computer:
    def __init__(self):
        self.__maximumprize = 1000

    def sell(self):
        print("the selling prize is:",self.__maximumprize)

    def setprize(self,prize):
        self.__maximumprize = prize 


obj1 = computer()
obj1.sell()
obj1.__maximumprize = 3000
obj1.sell()
obj1.setprize(3000)
obj1.sell()





    