from abc import ABC, abstractmethod
class smartdevice(ABC):
    def showdevice(self,name):
        print("The device name is:",name)

    @abstractmethod
    def turn_on(self):
        pass

class smartlight(smartdevice):
    def turn_on(self):
        print("The smart light is turn on")

class smartfan(smartdevice):
    def turn_on(self):
        print("The smart fan is turn on")

class smartspeaker(smartdevice):
    def turn_on(self):
        print("The smart speaker is turn on")

obj1 = smartlight()
obj2 = smartfan()
obj3 = smartspeaker()

obj1.showdevice("smart light")
obj1.turn_on()

obj2.showdevice("smart fan")
obj2.turn_on()

obj3.showdevice("smart speaker")
obj3.turn_on()

class securitycamera:
    def checkstatus(self,name):
        print("This is a security camera:",name)

class doorlock:
    def checkstatus(self,name):
        print("This is a door lock:",name)

obj4 = securitycamera()
obj5 = doorlock()

for device in (obj4,obj5):
    device.checkstatus("security camera")
    device.checkstatus("door lock")
