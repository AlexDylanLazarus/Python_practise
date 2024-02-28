# Object oriented programming?
# If we could model our problem as real life object then our solution is done
#You are trying to model the real world

import pprint

# car
# 1. engine
# 2. wheels
# 3. doors
# 4. name

        # car
#Ferrari
# 1. engine - v8 
# 2. wheels- 4
# 3. doors  2

#Toyota taz
# 1. engine - v4
# 2. wheels - 4
# 3. doors - 4

# Use init so you dont have to repeat
class Car:
    def __init__(self, name, engine, wheels, doors):
        self.name=name
        self.engine=engine
        self.wheels=wheels
        self.doors=doors

    def horn(self):
        return "Vroom Vroom"


#self-> to the object created
# ferrari -> object        
ferrari=Car('Ferrari','v8',4,4)
toyota=Car('Toyota','v4',4,4)
bugatti=Car('Bugatti','w16',4,2)
GTR=Car('GTR','v6',4,2)

print(ferrari.name,ferrari.wheels)
print(toyota.name,toyota.wheels)
print(bugatti.name,bugatti.wheels)
print(GTR.name,GTR.wheels)
print(ferrari.horn())



# this is too long thats why we use __init__
# ferrari=Car()
# ferrari.name="Ferrari"
# ferrari.engine="v4"
# ferrari.wheels=4
# ferrari.doors=4
# print(ferrari.name, ferrari.engine, ferrari.wheels, ferrari.doors)

#Bank Account 
# 1. accno
# 2. name
# 3. balance




class Bank:
    def __init__(self, accno, name, balance):
        self.accno=accno
        self.name=name
        self.balance=balance
    def display_balance(self):
        return f"Your balance is : R{self.balance:,}"
    def withdraw(self,num):
        return self.balance-num
    def deposit(self,numb):
        return self.balance+numb

gemma= Bank("123","Gemma Porill", 15_000)
dhara= Bank("124", "Dhara Kara", 50_001)
caleb= Bank("125", "Caleb Potts", 100_000)


print(gemma.display_balance())
print(gemma.withdraw(200))
print(gemma.deposit(200))


# Assignment - Transactions Tomorrow
# #  id   Date       Type     Amount  
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000  


class transactions:
    def __init__(self, id, date, type, amount):
        self.id = id
        self.date = date
        self.type = type
        self.amount = amount

trans = {
    'first=transactions': [transactions(1, '29 Feb', 'withdraw', 2000)],
    'second': [transactions(2, '1 Mar', 'deposit', 6000)],
    'third': [transactions(3, '3 Mar', 'deposit', 7000)]
}

print(" #  id   Date       Type     Amount  ")

for key, value in trans.items():
    for i, transaction in enumerate(value, start=1):
        print(f" {i}. {transaction.id}  {transaction.date}   {transaction.type}       {transaction.amount}")

