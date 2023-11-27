#addition of two complex numbers

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def display(self):
        print(self.real,"+i",self.img)
        
    def add(c1,c2,c3):
        c3.real=c1.real+c2.real
        c3.img=c1.img+c2.img
        
        
c1=complex(5,9)
c2=complex(3,1)
c3=complex(0,0)
c1.display()
c2.display()
complex.add(c1,c2,c3)
c3.display()

        
        
