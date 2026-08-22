class string:
    def __init__(self):
        self.word =""

    def getstring(self):
        self.word = input("Enter any word")

    def printstring(self):
        print("the word is:",self.word.upper())

obj = string()
obj.getstring()
obj.printstring()


class employ:
    def __init__(self):
        print("employ created")

    def __del__(self):
        print("employ deleted")

obj1 = employ()
del obj1



