'''create a python class called birthdayboy that takes 2 variables:
   string name and integer age.Within birthdayboy, create a method called birthday 
   that increase the age by 1. Once this class has been created, create an instance
   of the class then call birthday methods to increase its age and print the same'''
   
class birthdayboy:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def birthday(self):
        self.age+=1
        print(self.age)
        
boy1=birthdayboy('tommy',20)
boy1.birthday()

boy2=birthdayboy('john',44)
boy2.birthday()
