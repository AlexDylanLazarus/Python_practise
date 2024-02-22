# Difference between Argument and Parameter. 
[This is the article I used](https://www.w3schools.com/python/gloss_python_function_arguments.asp#:~:text=A%20parameter%20is%20the%20variable,function%20when%20it%20is%20called.)
## Argument
- An argument is the value that are sent to the function when it is called.

## Parameter
- A parameter is the variable listed inside the parentheses in the function definition

### Example
```
def person(name, surname): ##Here I have 2 parameters
  print(name +" "+ surname)

person("alex") #here I only gave one argument when calling the function, which will give me an error saying that I am missing an argument

person("alex", "Lazarus") #this is the correct way to give both arguments
```