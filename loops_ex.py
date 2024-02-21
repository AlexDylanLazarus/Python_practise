numbers=[8,5,7,4,6,2]
# odd=["odd" for odd in numbers if odd%2==1]
# even=["even" for even in numbers if even%2==0]
# output=odd+even
# print(output)

# evenorodd = ["Even" if number % 2 == 0 else "Odd" for number in numbers ] 

# print(evenorodd)

# numbers_copy=[]
# for num in numbers:
#   numbers_copy.append("even" if num % 2 ==0 else "odd")
# print(numbers_copy)#haing print outside of for loop wont give the stair looking output

result=["even" if num%2 == 0 else "odd" for num in numbers]
print(result)

