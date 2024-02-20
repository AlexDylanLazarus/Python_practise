person1= input('Please give your name')
height1= int(input('Provide your height in cm'))
person2= input('Please give your name')
height2= int(input('Provide your height in cm'))

#"abc" > "def" is false. Lexical order/lexical comparison.

#version1
# if (int(height1) > int(height2)):
#   print(f"{person1} is taller than {person2}")
# else:
#   print(f"{person2} is taller than {person1}")

#exit() to exit the repl

#version2
if (height1> height2):
  print(f"{person1} is taller than {person2}")
elif(height1==height2):
  print(f"{person1} and {person2} are the same height")
else:
  print(f"{person2} is taller than {person1}")

#elif can be many but ther is only one if and one else.
