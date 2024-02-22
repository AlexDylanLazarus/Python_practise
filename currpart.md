
# What is Currying and Partials
[Article used](https://medium.com/@aems/closures-vs-curried-functions-vs-partial-application-66889658a03#:~:text=Currying%20takes%20a%20function%20as,data%20and%20no%20execution%20involved.&text=Partial%20application%20takes%20a%20function,since%20some%20are%20already%20bound.)

### Currying:
- Input: A function
- Output: Another function that takes a single argument and returns another single argument function until all original arguments are accounted for.
- Currying transforms a function into a sequence of functions, each taking one argument.

#### Python Example:
```
def add(x):
    def inner(y):
        return x + y
    return inner

add_curried = add(5)
print(add_curried(3))  # Output: 8
```

### Partial Application:
- Input:
  1. A function that accepts N arguments
  2. Data for M arguments, where 1 ≤ M < N
- Output: Another function which accepts N - M arguments.
- Partial application binds some arguments of a function, creating a new function with fewer parameters.

#### Python Example:
```
def multiply(x, y):
    return x * y

multiply_partial = functools.partial(multiply, 5)
print(multiply_partial(3))  # Output: 15
```