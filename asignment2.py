#Q1 Write a function to add two numbers and print the values.

a,b=map(int,input().split(","))
def addition(a,b):
    print(a+b)
addition(a,b)    

#Q2 Write a function that takes string as an argument and return the reverse of the string.

def reverse_string(input_string):
    return input_string[::-1]
b=input("string:")
print("Reversed string:", reverse_string(b))

#Q3 Write a function that takes string and return the number of vowels and consonant
    
string=input("Enter a string:")
string=string.lower()
vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
def check_no_of_vowels_and_consonants(string):
    no_of_vowels = 0
    no_of_consonants = 0
    for i in range(len(string)):
        if string[i] in vowels:
            no_of_vowels+=1
        if string[i] in consonants:
            no_of_consonants+=1
        else:
            continue

    return no_of_vowels, no_of_consonants
print("the no. of vowel and consonants are:")
print(check_no_of_vowels_and_consonants(string))


#Q4 .Define a function which takes list containing numbers as input 
#Q     and return list containing square of every number

l=list(map(int,input().split(",")))
def square_numbers(l):
    return [x**2 for x in l]
print(square_numbers(l))


#Q5 Define a function which takes list of words as argument and 
#    return list with reverse of every element in that list.

m=list(input("enter a string: "))
def reverse_words(m):
    return m[::-1]
print(reverse_words(m))


#Q6 Define a function which takes list of numbers as a parameter 
#   and return a list which contains the same elements as original 
#   list but even numbers should come at the end of the list.

a=list(map(int,input().split(",")))
def even_numbers_at_end(a):
    even_numbers = [num for num in a if num % 2 == 0]
    odd_numbers = [num for num in a if num % 2 != 0]
    return odd_numbers + even_numbers
print(even_numbers_at_end(a))


#Q7 Write a function that takes a string as input and return true if 
#    String is palindrome and false otherwise.

s = input("Enter a string: ")
def is_palindrome(s):
    reversed_string = s[::-1]
    if s == reversed_string:
        return True
    else:
        return False

print(is_palindrome(s))
