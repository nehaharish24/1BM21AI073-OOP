

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
        
    def work(self):
        print(f"{self.name} is working.")

    def show(self):
        print(f"Employee: {self.name}\nSalary: {self.__salary}")
        
employee1 = employee("John Doe", 50000)
# Access public instance variable (name)
print("Employee Name:", employee1.name)

# Access private instance variable using getter method (show())
employee1.show()

# Call the work method
employee1.work()
