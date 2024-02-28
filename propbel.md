## Assignment with @property and @balance.setter in a class
[Article used](https://medium.com/@pijpijani/understanding-property-in-python-getters-and-setters-b65b0eee62f9)

### @property
-is a built-in decorator for the property() function in Python. It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class.

### @balance.setter
[Article used](https://www.datacamp.com/tutorial/property-getters-setters)

-setter will set the value of a property by checking the conditions we have mentioned in the method.

#### Example
```
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{value} is not a valid input for balance")
        self._balance = value
    def deposit(self, amount):
        if not isinstance(amount, int) or amount < 0:
            raise ValueError(f"{amount} is not a valid input for amount")
        self.balance += amount
    def withdraw(self, amount):
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Withdrawal amount must be a positive number")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
```