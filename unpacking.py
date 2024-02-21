# a = 10
# b = 10
# c = 10

# Mulitiple variable assignment:
# a = b = c = 10
# print(a,b,c)

# lilitha, dhara, quinlan = "chocolate","lime",  "vanilla"
# print(lilitha,dhara,quinlan)
#output will be chocolate lime vanilla 

#unpacking
# movies=["Remember the Titans","Juno","Lucy"]
# caleb, gemma, yolanda  = movies
# print(gemma) 
# #will return juno

# t1, _  ,t2, t3= [100, 200, 300, 400]

# print(t1,t2,t3)#will gve an error saying too many values to unpack. The ' _ ' skips the last value. You can also have it in other places to skip it. 


# t1, t2, *t3= [100, 200, 300, 400, 60, 40, 30]
# #to put all into t3, use *
# print(t1,t2,t3)


# t1, t2, *t3= (100, 200, 300, 400, 60, 40, 30)
# print(t1,t2,t3) #this also makes t3 a list even tho it is a tuple.

#exercise. 
coordinates = [(5,4), (1,1), (6,10), (9,10)]
# distances = []
# for x,y in coordinates:
#   distance = (x**2 + y**2)**0.5
#   distances.append(distance)  
# print(distances)

#ORRRRR
# distances = []
# for x,y in coordinates:
#   distances.append(((x**2 + y**2)**0.5))
# print(distances)

#using unpacking and list comprehension
import math
answers = [math.sqrt(x**2 + y**2) for x,y in coordinates]
print(answers)

#Only list or tuple can be unpacked.





