# Using function as a decorator
def my_decorator_function(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called")
        result = func(*args, **kwargs)
        print("After the function is called")
        return result

    return wrapper


@my_decorator_function
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


# Using class as a decorator
class MyDecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before the function is called")
        result = self.func(*args, **kwargs)
        print("After the function is called")
        return result


@MyDecoratorClass
def greet(name):
    print(f"Hello, {name}!")


greet("Bob")
