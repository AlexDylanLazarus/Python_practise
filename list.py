#Mutable
# marks=[98, 75, 40, 45, 80, 90, 45, 80, 60]
# print(type(marks))
# # marks.pop()
# # marks.pop() #does mutate the list. By deafult it removes the last element
# #marks.pop(3)# removes index
# print(marks[0:len(marks)-3])
# #another way to do it:

# #slice do not mutate the list
# print(marks[0:-3])
# print(marks) #returns original array so nothing is removed. 

# marks=[98, 75, 40, 45, 80, 90, 45, 80, 60]
# marks.remove(40) #mutates because the original array/list is changes. Also a mutation
# print(marks)

# marks.append('hello')#adding to the end of the list
# print(marks)

# marks.insert(0, 'hello')#adding to the beginning of the list. Also a mutation.
# sci= 85
# marks.insert(2,sci)
# print(marks)

#[5,6]*2 # will give u [5,6,5,6]

#combining lists
# price_list1= [1000, 1500, 400]
# price_list2= [2000,500]
# print(price_list1+price_list2)

#to duplicate array you just say * 2

# copy list
# C
# price_list1_copy=price_list1 
# print(price_list1_copy.append(600))
# print(price_list1.append(700))
# print(price_list1, price_list1_copy)
# they both will have 600 and 700. 

#price_list1 stores the first item's memory address thats why it is 0. 

#creating a copy. They wont look the same 
#  price_list1= [1000, 1500, 400]
# # price_list2=price_list1[:] OR
# price_list2 =price_list1.copy()
# print(price_list1.append(600))
# print(price_list2.append(700))
# print(price_list1, price_list2)

#remove is different from pop because it uses the value where as pop uses the index.


# subjects= ["eng","maths","science"]
# print(", ".join(subjects))
# #output will be eng, maths, science
# subjects.sort(reverse=True)
# print(subjects)

#combinig 2 list just +.

# list=[1,3,3,2,5,6]
# # .sort is mutable

# print(list.sort(), list)