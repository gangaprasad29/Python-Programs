# # VARIABLES
# name="gnaga"
# age=19
# print(name,age)


# #EXPRESSION EXWCUTION

# (REPEATATION)
# a,b=2,3
# text="@"
# print(2*text*3) #output : @@@@@@(6 times @)

# #(CONCATINATION: ADDITION OF STRINGS)
# A,B="2",3
# Text="@"
# print((A+Text)*B)

# A,B=2,3
# C=4
# print(A+B*C)  #output will int

# a,b=10,5.0
# c=a*b
# print(c) # output will float

# a,b=2,1
# c=a/b
# print(c)  #output will float

# a,b=2,1.5
# c=a/b
# print(c)  # output will float

# a,b=2,1.5
# c=a///b
# print(c)  # output will int which is closest integer which is <= that no.


# ###INPUT IN PYTHON

# #STRING INPUT
# name=input("name:")

# #INT INPUT
# age=int(input("age :"))

# #FLOAT INPUT
# price=float(input("price:"))

# # FOR 2 OR MORE INPUT (INT,FLOAT)
# a,b=map(int,input().split(","))
# print(a+b)


# #CONDITION STATEMENT
# SINGLE LINE IF / TURNARY OPERATOR

# food=input("food:") 
# eat="yes" if food=="cake" else "no"
# print(eat)

# 2 way

# food=input("food:")
# print("sweet") if food=="cake" or food=="jalabi" else print("not sweet")

# #clever if / ternary operator

# age=int(input("age: "))
# vote=("yes","no") [age>=18]


# sal=float(input("salary: "))
# tax= sal*(0.1,0.2) [sal<=50000]
# print(tax)


# # STRING OPERIATIONS
# # CONCATENATION (addition of 2 string)

# a="hello"+"word"
# print(a)

# a="ganga"
# b="prasad"
# print(a+""+b)

# a="ganga"
# print(len(a))

# #INDEXING
# a="gangaprasad"
# print(a[4])

# #SLICING
# a="gangaprasad"
# print(a[1:6])
# print(a[:6])
# print(a[5:])
# print(a[-3:-1])
# print(a[0::2])

# #STRING FUNCTIONS (immutable)
# str="i am coder"
# str.endswith("er.") # return true if string ends with substr
# str.capitalize() # capitalize 1st string
# str.replace(old,new)
# str.find(word)
# str.count("am")

# ## LIST (mutable) & TOUPLES(3:27)

# marks=[94.4,87.5,95.2,66.4,445.1]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[2])
# print(marks[0])

##we are changing the list

# student =["mark",20.2,19,"delhi"]
# print(student[0])
# student[0]="arjun"
# print(student)

##LIST SLICING (just like string slicing)
# marks=[212,122,34,554,453]
# print(marks[1:4])


## methods in list

l=[212,122,34,554,453]
print(l.append(222)) # it will print none
print(l)
print(l.sort())
print(l)
print(l.sort(reverse=True))
print(l)














