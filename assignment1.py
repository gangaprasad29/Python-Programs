##Q1 Print First 10 natural numbers using while loop ?

i=1
while i in range(0,11):
    print(i) 
    i+=1

##Q2 Print the following pattern
# 1 
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5
    
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


##Q3 Write a program to print multiplication table of numbers in range(1, 12) ?

for i in range(1,13):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")


##Q4     Display numbers from a list using loop which are divisible by 4
#        Numbers =[1,4,9,12,16,425,434,464,512,524,724] ?

num=[1,4,9,12,16,425,434,464,512,524,724]
for i in num[::1]:
    if i%4==0:
        print(i,end=" ")

##Q5 Print the following pattern ?
#    5 4 3 2 1 
#    4 3 2 1 
#    3 2 1 
#    2 1 
#    1 

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()



##Q6 Print list of question 4 in reverse order using a loop ?

num=[1,4,9,12,16,425,434,464,512,524,724]
for i in num[::-1]:
    if i%4==0:
        print(i,end=" ")


##Q7 Find the factorial of a  number 14 ?

n= 14
f = 1

for i in range(1, n + 1):
    f*= i

print(f"The factorial of {n} is: {f}")
