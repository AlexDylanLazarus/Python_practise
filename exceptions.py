from datetime import datetime

# def math_divide(n1, n2):

#     try:
#         result = n1 / n2
#         print("the answer is", result)

#     except ZeroDivisionError:
#         print("You cannot divide by zero")
#     except TypeError:
#         print("Do not enter a string")
#     else:
#         # when no errors happen
#         print("Division was successsful")
#     finally:
#         # No Error. We generally run cleanup code here. No matter what it'll print finally.
#         print("Operation done")


# math_divide(10, 5)
# math_divide("abd", 2)  # gonna give you another error


# print("hiii")


def calculate_age():

    try:
        user_input = input("please tell me your year of birth")
        current_year = datetime.now().year
        birth_year = int(user_input)
        age = current_year - birth_year

        if birth_year <= 0:
            # raise -> Stops further execution
            raise ValueError("Year cannot be negative")
        if birth_year > current_year:
            raise ValueError("You are not flash to be from the future")
        print(f"You are {age} years old")
    except ValueError as e:
        print(f"Invalid number: {e}")
    except Exception as e:
        # Catch all errors
        print("This is catch all: ", e)


# How to create own Error class


class NegativeNumberError(Exception):

    def __init__(self, value):
        self.value = value
        self.message = "Negative numbers are not allowed"
        super().__init__(self.message)  # this passes it to base class

    def __str__(self):  # string dunder method
        return f"{self.value} -> {self.message}"


def only_positive_num():
    try:
        x = -10
        if x < 0:
            raise NegativeNumberError(x)

    # Match what type of error it is:
    except NegativeNumberError as e:  # assigning e to line 67
        print(e)


if __name__ == "__main__":
    calculate_age()
    only_positive_num()  # -10 -> Negative numbers are not allowed
