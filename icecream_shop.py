stock1="vanilla"
stock2="lime"
stock3="chocolate"
#lime
#yes, we do have it

#strawberry
#no, we ran out of stock
#task 1
# ask=input("what flavour do you want?")
# if(ask==stock1):
#   print("yes, we do have it")
# elif(ask==stock1):
#     print("yes, we do have it")
# elif(ask==stock3):
#   print("yes, we do have it")
# else:
#   print("no, we ran out of stock")

#You can use logical operators to combine conditions. 

#ask=input("what flavour do you want?")
# if(ask==stock1 or ask==stock2 or ask==stock3):
#   print("yes, we do have it")
# else:
#   print("no, we ran out of stock")


#task 2
shop_stock="vanilla, lime, chocolate"
que=input("what flavour do you want")
# if(que in shop_stock):
#   print("yes, we do have it")
# else:
#   print("no, we ran out of stock")

#DRY- Don't Repeat Yourself

#TERNARY operators
# takes 3 operants
#in it is a membership operator
#a concise way to performa an if-else in single line

#unary operators
#not
# ~ (not for practical use)

#binary operators(2 operatorants)
# >, <, ==, and, or, >=, <=, !=
  

#bitwise operators
# & and, | or, ^, ~, <<, >>

# 1= 1
# 2= 10
# 3= 11
# 32 bit
# 4= 000000000100

#1111111111011 (flip the zeros to ones and ones to zeros)

#Making it simpler
shop_stock="vanilla, lime, chocolate"
que=input("what flavour do you want")
print('"yes, we do have it" if que in shop_stock else "no, we ran out of stock"')


