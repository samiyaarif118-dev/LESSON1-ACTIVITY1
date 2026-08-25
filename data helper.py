class dailymessage:
    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter your message")
    def print_message(self):
        print("your message:",self.message.upper())

obj = dailymessage()
obj.get_message()
obj.print_message()


class helpersession:
    def __init__(self):
        print("session is created")
    def __del__(self):
        print("session is end")

obj1 = helpersession()
del obj1


def create_session():
    print("making helper session")
    session = helpersession()
    print("session is ready")
    return session 

obj1 = create_session()


class PairFinder:
    def find_pair(self,numbers,target):
        lookup = {}
        for index, number in enumerate(numbers):
            diff = target - number
            if diff in lookup:
                return(lookup[diff],index)
            lookup[number] = index
        return None
        
numbers = (10, 20, 30, 40, 50, 60, 70)
 
target_value = int(input("Enter target sum to search: "))
 
result = PairFinder().find_pair(numbers, target_value)
 
if result is not None:
    print("index1=%d, index2=%d" % result)
else:
    print("No matching pair found.")
print("Program End")


          

        

                  


