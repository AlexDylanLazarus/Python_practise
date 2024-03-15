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


## test 3 
the total outer width question


which list type displays an items in a numbered format?
<ol>

which html element is used to define a part of text in an inline format?
<span>

which css property is used to changed the background color of an element?
background-color

CSSOM 
cascading stylesheet object model
import

which css property changes he text color of an element?
color

difference between id and class
id can only be used once, class can be used multiple times

in css, if two selectors apply to the same element, what determines which style is applied
the specificity of the selector

what does the !important rule in css do?
overrides all other styling rules

which display value does not preserve the space for the element in the layout
none

which css property adds space between characters?
letter-spacing

in the css model, what propperty adds space inside the border of an element?
padding

which color format allows for specifying transparency?
rgba

in css, which property is inheritied by default from the parent element?
color

which css property creates a transition effect when changing from one style to another?
transition

given <div style="margin:20px;border:5px solid black;">content</div> what is the total outer width if the content width is 100px?
the answer is 170px coz everything doubles


what command initialize a new git repository
git init

which branch is traditionally used for the stable version of a project
master because its the one given to the customer

what does the `git commit -m "message"` command do?
snapshots the current work with a descriptive message

what is the primary purpose of the staging area in git?
to prepare and review before committing

what results from a fast-forward merge in git?
the target branch pointer moves forward to match the source branch
target- master
source- dev

how do you resolve a merge conflict in git
by manually editing the files to resolve conflicts, then staging and committing

wat distinguished git from github
all of the above

what is the best practice for writing commit messages?
including why and what changes were made

how does creating branches in git help with project development?
it allows multiple features to be developed in parallel without affecting the main codebase.

what is the recommended frequency for committing changes in git?
after every few logical changes

in git what does the command `git checkout -b dev` do?
creates and checks out to a new branch named 'dev'

<----git switch is the new command people use---->

what is the primary purpose of a pull request on platforms like GitHub?
To merge changes from your branch into another branch or repositiory after review

which git command shows the changes between commits, the working directory, and the staging area?
git diff

how do you revert to a previous commit in Git, disregarding all changes after that commit?
git reset --hard <commit_hash>



# test 4
what does the json.dumps() function do:
converts a python object into json formatted string

in the context of web development, how is json typically used?
As a lightweight data-interchange format between a server and a web application

what does select distinct manufacturer from  cars order by manufactuer ascc; return?
a list of all manufacturers without duplicates, alphabetically.

which sql clause is used to reurn only a specific number of records from the cars table
limit

how do you find cars manufacture between 1960 and 1970
select * from cars where year between 1960 and 1970

starts with mustang

to add a new column
alter table add column

which command deletes a table
drop 

normal join 

what is the purpose of data normalization
reduce data redundancy and improve data integrity

np.arange(1,20,2)

4, 8

pivot table 
both a and b

scatter plot 
a and b

how do you change index of a dataframe 'df' to be the name column
df.set_index('Name')

replace all occurences of a string in a dataframe 
df.str.replace()