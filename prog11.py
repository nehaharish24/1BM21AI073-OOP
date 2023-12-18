'''create a class called CREDITCARD, make limit variable completely private to the outside
   of the class and balance should be accessible outside the class, but not modifiable.
   To acheive this, make a get_balance() field public, however balance can only be modified 
   via withdraw() and deposit() methods that have safegaurd checks in place.'''
   
class CREDITCARD:
    def __init__(self,limit,balance):
        self.__limit=limit
        self.balance=balance
        
    def get_balance(self):
        print("Balance:", self.balance)
        
    def deposit(self,amount):
        self.balance += amount
        
    
    def withdraw(self, amount):
        if self.balance >= amount and self.balance - amount >= -self.__limit:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Withdrawal failed. Insufficient funds or over limit.")

            
c1=CREDITCARD(3000,15000)
c1.get_balance()
c1.deposit(2000)
c1.get_balance()
c1.withdraw(15000)
c1.get_balance()
