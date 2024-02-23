
# utility functions, so you dont have to recode it again again. see fun.py
def to_upper_case(text):
  return text.upper()

# print(__name__, type(__name__)) ##this will print __main__ if u run from this file

# break into function. Don't write a lot of lines into the if. Have functions outside

# __ are called dutter variables
# x=[3,5,6]
# x.__ge__ -> dont use unless necessary. This is internal methods. This will give dunder methods.

if __name__ == "__main__":
  print(to_upper_case("quinlan"))
  print(__name__, type(__name__))

# x=[3,5,6]
#you can say dir(x) to get all the methods you can use for it