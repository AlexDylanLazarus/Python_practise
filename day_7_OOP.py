# Object oriented programming?
# If we could model our problem as real life object then our solution is done
# You are trying to model the real world

import pprint

# car
# 1. engine
# 2. wheels
# 3. doors
# 4. name

# car
# Ferrari
# 1. engine - v8
# 2. wheels- 4
# 3. doors  2

# Toyota taz
# 1. engine - v4
# 2. wheels - 4
# 3. doors - 4


# # Use init so you dont have to repeat
# class Car:
#     def __init__(self, name, engine, wheels, doors):
#         self.name = name
#         self.engine = engine
#         self.wheels = wheels
#         self.doors = doors

#     def horn(self):
#         return "Vroom Vroom"


# # self-> to the object created
# # ferrari -> object
# ferrari = Car("Ferrari", "v8", 4, 4)
# toyota = Car("Toyota", "v4", 4, 4)
# bugatti = Car("Bugatti", "w16", 4, 2)
# GTR = Car("GTR", "v6", 4, 2)

# print(ferrari.name, ferrari.wheels)
# print(toyota.name, toyota.wheels)
# print(bugatti.name, bugatti.wheels)
# print(GTR.name, GTR.wheels)
# print(ferrari.horn())


# this is too long thats why we use __init__
# ferrari=Car()
# ferrari.name="Ferrari"
# ferrari.engine="v4"
# ferrari.wheels=4
# ferrari.doors=4
# print(ferrari.name, ferrari.engine, ferrari.wheels, ferrari.doors)

# Bank Account
# 1. accno
# 2. name
# 3. balance


# encapsulation | putting in all together container | giving access
class Bank:
    # Class variable if you want to share the same value
    interest_rate = 0.02
    no_of_accounts = 0

    @classmethod
    def update_interest_rate(cls, rate):
        Bank.interest_rate = rate

    # we generally dont use cls methods if we are not updating anything. You should rather use static methods @staticmethod
    @staticmethod
    def get_total_no_accounts():
        return f"In total we have {Bank.no_of_accounts} accounts"

    # instance method
    # self points to the instance we created
    def __init__(self, accno, name, balance):
        # instance variable
        self.accno = accno
        self.name = name

        # private varaible. __ makes it private
        # self.__balance = balance

        # protected. You can use it in child but not outside
        self._balance = balance

        Bank.no_of_accounts += 1
        print(self.name, Bank.no_of_accounts)

    # you can also have private methods like def __display_balance
    def display_balance(self):
        return f"R{self._balance:,}"

    def withdraw(self, num):
        if num < self._balance:
            self._balance -= num
            return f"Your balance is: {self.display_balance()}"
        else:
            return f"you do not have enough in your account to withdraw"

    def deposit(self, numb):
        if numb > 0:
            self._balance += numb
            return f"Successfully deposited. {self.display_balance()}"

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate


# interest rate is higher. 0.05. If you apply interest on her and check her balance, it would be
class SavingsAccount(Bank):
    interest_rate = 0.05

    ##private variables and methods dont get inherited

    # dont need the following:
    # def __init__(self, accno, name, balance):
    #     super().__init__(accno, name, balance)

    # def apply_interest(self):
    #     self.update_balance(self.get_balance * self.interest_rate)


# Magic methods __repr__, __str___


# whenever you withdraw, you are charged a checking fee of R1
class CheckingAccount(Bank):
    transaction_fee = 1

    def withdraw(self, num):
        """This is for withdraw money with transaction fee"""
        total_amount = num + CheckingAccount.transaction_fee
        return super().withdraw(
            total_amount
        )  # you call it from base class but add the child's stuff

    def __str__(self):
        """Human readable output"""
        return (
            f"This account belongs to {self.name} and has a balance of {self._balance}"
        )

    def __repr__(self):
        """DX: String -> Class"""
        return f"Checking account ({self.accno}, {self.name}, {self._balance})"

    def __add__(self, other):
        return self._balance + other._balance


gemma = Bank("123", "Gemma Porill", 15_000)
dhara = Bank("124", "Dhara Kara", 50_001)
# caleb = Bank("125", "Caleb Potts", 100_000)
Alex = CheckingAccount(126, "Alex Lazarus", 100)
caleb = CheckingAccount("125", "Caleb Potts", 100_000)

gemma = SavingsAccount(123, "Gemma Porill", 1_000)

# print(Bank.get_total_no_accounts())
print(gemma.apply_interest())
print(gemma.display_balance())
print(Alex.withdraw(50))
print(Alex.display_balance())
print(
    Alex
)  # behind the scene this is doing alex.__str__ . It wont print out the object main thing.
# print(Alex._balance)will give error
# print(caleb)
# print(Alex.__repr__())
print(repr(Alex))  # better than print(Alex.__repr__()). It is reconstruct -> instance
# print(type(Alex))
print(Alex + caleb)  # returns 100049


# print(gemma.withdraw(200))
# print(gemma.display_balance())

# print(gemma.accno)
# # print(gemma.__balance) gives an error
# print(gemma.apply_interest())

# Bank.update_interest_rate(0.10)

# apply interest
# caleb.apply_interest()
# print(caleb.display_balance())

# print(gemma.display_balance())
# print(gemma.withdraw(200))
# print(gemma.deposit(200))


# Assignment - Transactions Tomorrow
# #  id   Date       Type     Amount
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000


# class transactions:
#     def __init__(self, id, date, type, amount):
#         self.id = id
#         self.date = date
#         self.type = type
#         self.amount = amount


# trans = {
#     "first=transactions": [transactions(1, "29 Feb", "withdraw", 2000)],
#     "second": [transactions(2, "1 Mar", "deposit", 6000)],
#     "third": [transactions(3, "3 Mar", "deposit", 7000)],
# }

# print(" #  id   Date       Type     Amount  ")

# for key, value in trans.items():
#     for i, transaction in enumerate(value, start=1):
#         print(
#             f" {i}. {transaction.id}  {transaction.date}   {transaction.type}       {transaction.amount}"
#         )


# class Circle:
#     pi = 3.14159  # class variable

#     @staticmethod  # doesnt take cls or itself
#     def perimeter(radius):
#         return 2 * Circle.pi * radius

#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return Circle.pi * self.radius**2

#     @classmethod
#     def from_diameter(cls, diameter):
#         radius = diameter / 2
#         return cls(radius)


# print(Circle.perimeter(10))

# circle1 = Circle(2)

# circle_from_dia = Circle.from_diameter(20)
# print(circle_from_dia.calculate_area())


# # Inheritence. Whatever is yours is mine. Animal(Base) (name, speak)  -> Dog (child) (name, speak, run)
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some sound"


# class Dog(Animal):

#     def __init__(self, name, speed):
#         # use the keyword super to pass the name to animal
#         super().__init__(name)
#         self.speed = speed

#     #overriding things/polymorphism
#     def speak(self):
#         return "Woof!! "

#     def run(self):
#         return "🐶 wags tail"

#     def speed_bonus(self):
#         return f"Running at {self.speed*2} km/h"


# toby = Animal("toby")
# maxy = Dog("maxy", 20)
# print(toby.speak())
# print(maxy.speak())
# print(maxy.run())
# print(maxy.speed_bonus())
# print(toby.run()) methods are attributes. Toby does not have run.
