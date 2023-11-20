from datetime import datetime

class dog:
    def __init__(self,name,size,breed="unknown",dob="unknown"):
        self.name=name
        self.size=size
        self.breed=breed
        self.dob=dob
        
        
        
    def bark(self):
        print("wooff")
        
    def get_name(self):
        print("the name of dog is",self.name)
        
    def set_name(self,new_name):
        if len(new_name)>2 and len(new_name)<30:
            new_name.title()
            self.name=new_name
        
    def dog_years(self):
        if self.dob=="unknown":
            print("unknown date of birth")
        else:
            birth_year = int(self.dob[-4:])
            today = datetime.now()
            today_year=today.year
            age_in_years = (today_year - birth_year)
            dog_age = age_in_years * 7 
            print("the dog age is",dog_age)
            
dog1=dog('tom','small','beagle','28/10/2021')
dog1.bark()
dog1.get_name()
dog1.set_name('max')
dog1.get_name()
dog1.dog_years()

