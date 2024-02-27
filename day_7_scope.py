# ctrl + shift + p -> all commands 
#  ctrl + p -> find file

#Lexical scope
# def market():
#     price=100

#     def get_price():
#         print("the price is :", price)
#     get_price()
# market()



# def cool():
#     x=10
#     print('super') #x is alive from 16-17 becoz the function ends at 14


# cool()
# print("the value x is: ", x) #this gives an error saying x is not defined because it is a local variable

#This is what is known as SCOPE
# It is also known as the lifetime of a variable


#CLOSURE
# Own scope + lexical scope. Many functional language supports this

code_word="Hulk"

def space_ship():
    question="Please provide code word"

    def code_word_check():
        password="Hulk"
        print(question)

        if(password==code_word):
            print(f"Welcome, {password} the strongest avenger")
        else:
            print("Acces denied to ")
    code_word_check()

space_ship()
 
# Output:
# Please provide code word
# Welcome, Hulk the strongest avenger


#Lexical scope is important for currying
#example of currying
def add(x):
    def add1(y):
        return x+y
    return add1
print(add(10)(5)) #this returns function

add= lambda x: (lambda y: x+y)


# Default value copy by reference 

# def fun(nums=[]):
#     nums.append(10)
#     print(nums)
    

def fun(nums=None):
    if nums is None:
        nums = []
    nums.append(10)
    print(nums)

fun()    
fun()
fun()

# fun() #prints [10]
# fun()
# fun()