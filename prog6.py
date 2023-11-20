'''write a program to create two empty classes, Student and Marks. Now create some instances
   and check whether they are  instances of the said classes or not.Also, check whether the 
said classes are subclasses of the built-in object class or not.'''

class student:
    pass
    
class marks:
    pass

s1=student()
m1=marks()
print(isinstance(s1, student))
print(isinstance(m1, marks))
print(isinstance(s1, marks))

print(issubclass(student,object))
print(issubclass(marks,object))