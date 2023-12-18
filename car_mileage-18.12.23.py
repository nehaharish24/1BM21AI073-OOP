'''import the ABC module to create the abstract base class.
Create the car class that inherits the ABC class and defined an abstract
method named mileage().
Inherit the base class from 3 different subclasses and implement the abstract methods differently.
Create the objects to call the abstract method.'''

from abc import ABC,abstractmethod

class car(ABC):
    def __init__(self,mil):
        self.mil=mil
    @abstractmethod
    def mileage(self):
        pass
    
class car1(car):
    def mileage(self):
        print("Mileage: ",self.mil,"km/hr")
        
class car2(car):
    def mileage(self):
        print("Mileage: ",self.mil,"km/hr")
        
class car3(car):
    def mileage(self):
        print("Mileage: ",self.mil,"km/hr")
        
c1=car1(50)
c1.mileage()

c2=car2(40)
c2.mileage()

c3=car3(70)
c3.mileage()
    
