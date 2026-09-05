from abc import ABC, abstractmethod
class abstractclass(ABC):
    def print(self, x):
        print("the value of x is:",x)

    @abstractmethod
    def task(self):
        print("we are in abstract class")
class childclass(abstractclass):
    def task(self):
        print("we are inside a childclass")
        

obj = childclass()
obj.task()
obj.print(100)


class Sweden:
    def capital(self):
        print("the capital of Sweden is Stockholm")

    def language(self):
        print("the language of Sweden is Swedish")

class USA:
    def capital(self):
        print("the capital of USA is washington D.C.")
    def language(self):
        print("the language of USA is English")

obj1 = Sweden()
obj2 = USA()
for country in (obj1,obj2):
    country.capital()
    country.language()









