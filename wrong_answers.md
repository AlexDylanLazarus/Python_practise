it was both A and B and not none. sort(reverse=true) does not reverse it

remember set is {} as well. 

method used to remove an item from a list by its index -> .pop()

bool("False")- > will give you true. If it was 0 or empty it would return false.

* used for unpacking a sequence

"python is fun".split()?
['python','is','fun']

{'apple','banana'}=={'banana','apple'}
TRUE coz sets order dont matter

what does the break do?
Immediately exits the loop

print((1,2)+(3,4))
gives (1,2,3,4)

BODMAS
print("a"+"bc"*2)
"abcbc"

whatdoes this code output? tuple= (1,2,[3,4]); tuple[2][0]=7; print(tuple)
(1,2,[7,4])

predict the output: a, *_, b = range(5);print (a+b)
4 because range starts from 0 and ends at 4

What will print([x for x in "python" if x in "aeiou"]) output?
['o'] returns a list with only o in

floor division is the lesser side. 

Test 2
what does the following code output?
nums= (1,[2,3],4)
nums[1][0]=10
print(nums)

(1,[10,3],4)

given t1= (1,2) and t2=(3,4), how do you create t3 as a concatenation of t1 and t2
t3=t1+t2

what is the correct way to remove smartwatch from the set. 
Both A and B

what is the purpose of the finally block in a try-except statement
to execude code regardless of whether an excpetion occurs

what does the @staticmethod decorator indicate in a python class?
the method it decorates can be called without creating an instance of the class.

In the context of exception handlin, what does the else block do?
Executes if no exceptions are raised in the try block.

How can you extract all hashtags from a social media post using regex?
uusing re.findall

What role does the __init__ method play in apython class?
It acts as the constructor for a class, initializing instance attributes

Which block of code is guaranteed in a try-except statement, regardless of whether an exception occured?
finally

what is the primary benefit of using class methods in python?
to enable the method to access and modify class state that applies across all instances

In OOp, what does encapsulation refer to?
combing data and methods that operate on that data within a class

what is the output of 
re.finall(r'#\w+', Love #python and #coding!")?
['#python','#coding']

rhow to refactor this nested loop using list comprehension?

results=[]
for i in range(3):
    for j in range(2):
        results.append((i,j))

[(i,j) for i in range(3) for j in range(2)]

which function would you use to find all occurences of a pattern in a string?
re.findall()

How to debug a python script in vscode?
set a breakpoint and press F5

"what does
re.sub(r'\s+',' ', Multiple spaces')return?
    "Multiple spaces"

what is the output of 
re.search(r'^Hello','Hello World!).group(0)
"Hello"

what advantage does the finally block have in exception handling
it executes regardless of whether an exception was caugh or not

how do you correctly import and use the pi constant from the math module

Both A and B are correct

for i in range(2):
    for j in ['a','b']:
        print(i,j)

0 a 0 b 1 a 1 b

How do you align a string name to the right and fill the space with "-" in a field of 20 characters?
Both A and C are correct

names=['alice','bob','charlie]
lengths=map(len,names)
print(list(lengths)
prints the length of each name)

filters out even numbers

3.142

what is the primary purpose of virtual environments in python?
To isolate project dependencies

Class A:
    def __init__(self):
        self.__private()
    def __private(self):
        print("A):

class B(A):
    def __private(self):
    print("B")
B()

output will be "A"

In python exception handling, what is the difference between exceptException as e and a bare except: block


except Exception as e catches all exception that inherit from Exception, while a bare except: catches all possible exceptions, including system-exiting expertions like SystemExit


Both A and B 