#from flask import Flask

#app = Flask('app')#

#@app.route('/')
#def hello_world():
#  return 'Hello, World!'
#
#app.run(host='0.0.0.0', port=8080)
#name=input("what is your name")
#print(name)
#print("hello my name is ",name)

# task -> farenhite to celcius
# farenhite= input("insert a number you want to convert to celcius ")
# result= (float(farenhite)-32)*(5/9)
# # print("The "+str(farenhite)+" farenhite is " +str(result) +" celcius")
# print(f"The {farenhite} farenhite is {result} celcius")

#find the age of the person if their birth year is given
# birth_year=input("what is your birth year: ")
# print(f"you are {2024-int(birth_year)} years old")

# #given the radius you need to find the area
# rad=input("give the radius")
# print(f"the area of the circle is {3.14*float(rad)**2}")

#input: 70
#output: [=======70%]

# percent_completed=input("please provide percent complete: ")
# p_part= int(percent_completed) // 10
# remaining_part= 10 - p_part
# print(f"[{'='*p_part}{' '*remaining_part}] {percent_completed}%")

quote="I love python"
# print(quote[0])
# print(quote[2])
# strings are immutable but will give you a copy.
# print(quote.replace('l','x'))
# print(quote.upper())

# # Slicing operator
# #print(quote[2:5]) #the end value is not included so you add one 
# print(quote[2:6])
# print(quote[7:13]) # OR you can use
# print(quote[7:]) #this means till the end
# print(quote[100]) # will give index out of range error
#print(quote[-6:-1)
# print(quote[0:6:2]) #tells you to skip by 2
# print(quote[::3])
#print(quote[::-1]) #reverse the string


# x=10
# while x>=0:
#   print(x)
#   x=x-1

x = None