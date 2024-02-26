classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]}
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]}
    ]
}

# for classy, students in classes.items():
#   for student in students:
#     average = sum(student['grades'])/len(student['grades'])
      # print(f"{average:.2f}")}")


#Task 2 
# for classy, students in classes.items():
#   for student in students:
#     average = sum(student['grades'])/len(student['grades'])
#     print(classy, student['name'], average)


#How they did it
#Task 1
# classes_avg={}
# def find_avg(student):
#   return sum(student['grades'])/len(student['grades'])
  
# for cls_name, students in classes.items():
#   class_students_avg=[]
#   for student in students:
#     class_students_avg.append(find_avg(student))
#   # print(cls_name, sum(class_students_avg)/len(class_students_avg))
#   classes_avg[cls_name]=sum(class_students_avg)/len(class_students_avg)
# print(f"{classes_avg}")  



#Task 2 
# output = {
#     "Class A": {
#         "Alice": 90.5,
#         "Bob": 84.5,
#         "Charlie": 90
#     },
#     "Class B": {
#         "Dave": 92.5,
#         "Eve": 86.5,
#         "Frank": 95
#     }
# }

# student_avg_dict={}
# classes_avg={}
# def find_avg(nums):
#   return round(sum(nums)/len(nums) , 2)

# for cls_name, students in classes.items():
#   student_dict={}
#   for student in students:
#     student_name=student['name']
#     student_avg=find_avg(student['grades'])
#     student_dict[student_name]=student_avg
#   student_avg_dict[cls_name]=student_dict
# print(student_avg_dict)

#Task 3 list comprehension for question 1 
# example
# dbl=[x*2 for x in range(3)]
# print(dbl)






#computer science terms/concepts
#it is engaging and i feel thats the right way to learn
#what can sort of be a bit confusing is that things can sometimes blend together. 
#overthinking is more likely because you are learning so much in a short time.

# task 1 list comprehension
# classes_avg = {}

# for cls_name, students in classes.items():

#   classes_avg[cls_name] = find_avg(

#       [find_avg(student['grades']) for student in students])

# print(classes_avg)

def find_avg(nums):

  return round(sum(nums) / len(nums), 2)





# Normal version
# classes_avg = {}

# for cls_name, students in classes.items():

#   class_students_avg = []

#   for student in students:

#     class_students_avg.append(find_avg(student['grades']))

#   classes_avg[cls_name] = find_avg(class_students_avg) #for task 2.2

# print(classes_avg)


#list comprehension for dict to dict
# students_avg_dict = {}
# for cls_name, students in classes.items():
#   students_avg_dict[cls_name]={student['name']:find_avg(student['grades']) for student in students}
  
# print(students_avg_dict)

#Task 2.2 

students_avg_dict={cls_name: {student['name']:find_avg(student['grades']) for student in students} for cls_name, students in classes.items()} #whatever is after the equal to is the value of the key.
print(students_avg_dict)