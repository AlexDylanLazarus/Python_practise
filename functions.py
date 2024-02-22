# a = 8
# b= 10
# print("the sum is ", a + b)

# a1= 60
# b1= 70

# print("the sum is ", a1 + b1)

#functions are a way to pack your logic

#Declaration/ Definition. The inside part is called the body. a, b is called 
#parameters/arguments. The sum is called the Function name. Creating the function is abstracted the logic or hiding implementation
# def sum(a,b):
#   return a + b    #If you dont have return it will give none 

# #Abstraction
# print("The sum is: ", sum(30,50))


#default values. Default values argument should always come at the last
# def driving_test(name, age=15, car="Toyota tazz"): #it will give toyota tazz if you dont give 
#   #a car argument when calling the function
#   if age >= 18:
#     return f"You're elegible for driving. You will be tested with {car}"
#   else:
#    return "Try again after few years 👶🍼"

# # print(driving_test(20, "GR Corrolla"))
# # #print(driving_test(10))
# # print(driving_test(20))

# #Types of argument
# #Position argument based on position it sends through. to avoid it you use the keyword when calling
# #keyword argument

# # print(driving_test(21,"dhara"))# this gives an error because it uses dhara as age. to prevent it do the following
# print(driving_test(age= 21,name= "dhara"))
# print(driving_test("Gemma"))
# #[9,3,8].sort(reverse=True)


#functions exercise
#Create a function that adds a new book to the library
#Task 1


# library = [
#     {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
#     {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
#     {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
#     {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
#     {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False},
# ]

# def add_book(library, new_book):
#   for new_book in library:
#     return library.append(new_book)
  
# print(add_book(library, {"title": "Python Programming", "author": "Eric Matthes", 
#                          "year": 2019, "available": True}), library)
                         

#Task 2. youu search author name so create function. takes library name and author name
# [python 1 output and python 2 output]

# def search_book(library, author):
#   for book in library:
#     if book["author"] in author:
#       return book["title"], book["author"], book["year"], book["available"]

# print(search_book(library, "Mark Lutz"))

#Task 3
#check out book function: write a function check(library, title) that marks a book as not available if it exist and is availble in the library

# def check_out_book(library, title):
#   for book in library:
#     if book["title"] == title:
#       if book["available"]:
#         book["available"] = False
#         return f"{title} has been checked out."
#       else:
#         return f"{title} is not available."
    

# print(check_out_book(library, "Adavance Python"))   



# How they did it
# Task 1
# library_list = [
#     {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
#     {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
#     {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
#     {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
#     {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False},
# ]
# book={"title": "Fluent Python II", "author": "Alex", "year": 2016, "available":"True"}
# def add_book(library, new_book):
#   library.append(new_book)

# add_book(library_list.copy(),book)
# print(library_list)


#Task 2
# def search_by_author(library,author_name):
#   # pass #this means you'll implement it later
#   #I want all the book in library where author is makr lutz
#   return  [book for book in library if author_name==book["author"]]
  
  
# print(search_by_author(library_list,"Mark Lutz"))

#Task 3
# def check_out_book(library, title):
#   for book in library:
#     if (book['title']==title) and (book['available']): #You dont have to have == True coz its boolean
#       book['available']=False
#       return f"yes, {title} is availble and successfully checked out"
    
#   return f"{title} is unavailable"
# print(check_out_book(library_list, "Fluent Python"))
# #if you enter a book that doesn't exist it will say its unavailable
# print(check_out_book(library_list, "Hardy Boys"))


#Dictionary is not a sequence

# def sum(a,b):
#   return a+b

# #one line function. You generally tend to keep lambda functions as anonymous. 
# add= lambda a,b: a+ b
# print(add(6,7))

#anonymous - nameless function
#one liner
# Implicitly return (automatically returned after colon)
#can be used when you wanna pass a function as an argument

#functions treated as first class citizens
#1. assign a function to variable
#2. pass a function as argument
#3. Return a function



# def fun(y):
#   x=4 #1
#   return x + y #3

# fun(5)#2

#How to pass function as argument
# player_stats=[10,30,60]
# # boosted_stats=map(lambda x: x*2,player_stats)#takes a function as an argument and a list
# # print(boosted_stats, list(boosted_stats))

# # double_values=lambda x: x *2
# # boosted_stats=map(double_values, [10,30,60])

# def square(x):
#   return x * x

# super_boosted_stats=map(square,[10,30,60])
# print(list(super_boosted_stats)) #Dont forget to convert to list


# result1= map(lambda x:x*2,[(10,6),(30,8),(5,60)])
# print(list(result1)) #result will be [(10, 6, 10, 6), (30, 8, 30, 8), (5, 60, 5, 60)]
# #So you would want to use lambda if you have a short function. If u use the normal function defintion you are using it for more than one time use. Lambda expects a one argument function

# # def is_even(x):
# #   if x%2==0:
# #     return True

# # print(is_even(2))

# def say_hello():
#   return "Hello, "

# def greeting(hello_message, name):
#   print(hello_message()+name) #the function you are calling is say_hello. A function that accepts a function as an argument is called a higher order function. Map is a higher order function as well

# greeting(say_hello, 'Caleb') #Output is Hello, Caleb

# print(say_hello()) #returns hello, but without () it will give an error


# def map_own(fn, arr):
#   return [fn(a) for a in arr]
  
  

# map_own(lambda x: x*2, [10,30,60])

#their version

# def map_own(fn,arr):
#   return[fn(val) for val in arr]

# print(map_own(lambda x: x*2, [10,30,60]))
# print(map_own(lambda x: x*x, [10,30,60]))

# ##ORRR

# def map_own(fn, arr):
#   result = []
#   for i in arr:
#     result.append(fn(i))
#   return result
# output = map_own(lambda x: x * 2, [10,30,60])

# mul= lambda x : lambda y: x * y, 

# def sayHello1():
#   def msg():
#     return "Hello, "
#   return msg

# print(sayHello1()())
# print(sayHello1)
# ##OR
# msg_function=sayHello1()
# print(msg_function())


# #implicity return so lambda x returns a function definition as its output. Lambda x is returning lambda y
# #Paradigm (styles)
# #Functional programming F#, Haskell (no loops. So you use recursion)
# #OOP- inheritence. Python supports functional and OOP
# #Procedural programming
# #Mathematical programming
# # Currying, Partials
# mul= lambda x: lambda y: x * y #lambda y is function inside x function. So lambda y is a function that takes x as an argument. This is also a concept in functional programming called currying.

# print(mul(3)(6)) ## returns 18
# mul_5=mul(5) #naming it mul_5 will let you know the print result will be a multiple of 5
# print(mul_5, type(mul_5))  ##returns type lambda

# print(mul_5())


#HOF (High Order Function)- Argument function
# result1=map(lambda x:x*2,[10,30,60])
# result2=filter(lambda x:x>10,[10,50,60,100,6,8,30])
# print(list(result1))
# print(list(result2))#will return all values greater han 10

#Pythonic way
#recommended by most python developers like list comprehension


#Sequence- List
# 1. len
# 2. sum
# 3. sorted
# 4. max
# 5. min




# print(sum([10,30,60])) #will return 100
# print(max([10,30,60])) #will return 60
# print(min([10,30,60])) #will return 10

# print(all([True, False, True])) #all has to be true to return true. Behaves like an `an`
# print(any([True, False, True])) #any can be true. Behaves like an `or`

print(all([10,0,30,-1])) #will give false coz 0 is considered false

#Falsy values. When convered to boolean it will be false. Other values are Truthy
# 1. 0
# 2.[] lists
# 3. none
# 4. {} dictionaries
# 5. ""
# 6. set() sets
# 7. () tuple

# x=[]

# #if requires a booleans and will try to convert your x into a boolean. If x is empty it will give false. If x is not empty it will give true.
# if(x):
#   print("cool")
# else:
#   print("super")
# #this will only print super coz its falsy values. 

