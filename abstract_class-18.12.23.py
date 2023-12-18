from abc import ABC, abstractmethod
class vehicle(ABC):
    def __init__(self,no_of_wheels):
        self.no_of_wheels=no_of_wheels
    @abstractmethod
    def start(self):
        pass

class bike(vehicle):
    def start(self):
        print("kick start")
        
        
class car(vehicle):
    def start(self):
        print("self start")
        
class bus(vehicle):
    def start(self):
        print("kick start")
        
        
b1=bike(2)
b1.start()

        
b2=car(4)
b2.start()

        
b3=bus(6)
b3.start()
        
