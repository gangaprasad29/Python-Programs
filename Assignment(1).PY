##Q1  Print First 10 natural numbers using while loop ?

i=1
while i in range(0,11):
    print(i) 
    i+=1

##Q2 Print all elements in list using for loop and while loop ?

# List of elements
my_list = [1, 2, 3, 4, 5]

# Using a for loop
print("Using for loop:")
for element in my_list:
    print(element,end=" ")

# Using a while loop
print("\nUsing while loop:")
index = 0
while index < len(my_list):
    print(my_list[index],end=" ")
    index += 1


##Q3 Write a program to find the largest number and smallest number in a list ?

numbers = list(map(int,input("enter a list:").split(",")))
# Find the largest number
largest = numbers[0]
for num in numbers:
  if num > largest:
    largest = num

# Find the smallest number
smallest = numbers[0]
for num in numbers:
  if num < smallest:
    smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)


##Q4 Write a program to check if a number is even or odd ?

a=int(input("enter a number:"))
if(a%2==0):
    print("number is even")
else:
    print("number is odd")

##Q5 Write a program to find area and circumference of circle by taking radius as input ?

import math
radius = float(input("Enter the radius of the circle: "))
pi = 3.14159
area = pi * radius * radius
circumference = 2 * pi * radius
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)


##Q6 Write a program to convert Celsius to Fahrenheit ?

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = (celsius * 9//5) + 32

print("te fahrenheittempeature is:",fahrenheit)

##Q7 Find the factorial of a number 14 using loops ?

n= 14
f = 1

for i in range(1, n + 1):
    f*= i

print(f"The factorial of {n} is: {f}")


##Q8 Create a dictionary containing your personal information like name, age, branch ?

my_info = {"name": "Gangaprasad", "age": 19 , "branch": "Computer science"}

print(my_info)

##Q9 Print the multiplication tables of numbers between 2 and 10 ?

for i in range(2, 11):
    for j in range(1, 11):
        print(f"{i}*{j} = {i*j}")


##Q10 Write a program to return true or false based on 
#     whether a given number is greater than a particular 
#     number using random datatype ?

import random
random_number = random.randint(1, 100)
a = int(input("Enter a number: "))
b = a > random_number

print("Is", a, "greater than", random_number, "?", b)
