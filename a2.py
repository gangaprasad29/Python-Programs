#Q1
def add_and_print(num1, num2):
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", result)

# Example usage:
num1 = 5
num2 = 7
add_and_print(num1, num2)


#Q2
def reverse_string(input_string):
    return input_string[::-1]

# Example usage:
original_string = "hello"
reversed_string = reverse_string(original_string)
print("Reversed string:", reversed_string)


#Q3

def count_vowels_consonants(text):
  
  vowels = 'AEIOU'
  consonants = 'BCDFGHIJKLMNPQRSTVWXYZ'
  vowel_count = 0
  consonant_count = 0

  for char in text:
    if char in vowels:
      vowel_count += 1
    elif char in consonants:
      consonant_count += 1

  return {'vowels': vowel_count, 'consonants': consonant_count}

# Example usage:
text = "Hello, world!"
result = count_vowels_consonants(text)
print(f"The text '{text}' has {result['vowels']} vowels and {result['consonants']} consonants.")


#Q4

def square_list(numbers):
  
  squared_numbers = []
  for number in numbers:
    squared_numbers.append(number * number)
  return squared_numbers

# Example usage:
numbers = [1, 2, 3, 4, 5]
squared_list = square_list(numbers)
print(squared_list) 


#Q5

def reverse_words(words):
  
  reversed_words = []
  for word in words:
    reversed_words.append(word[::-1])
  return reversed_words

# Example usage:
words = ["hello", "world", "how", "are", "you"]
reversed_words = reverse_words(words)
print(reversed_words)  

#Q6

def separate_even_odd(numbers):
  
  even_numbers = []
  odd_numbers = []
  for number in numbers:
    if number % 2 == 0:
      even_numbers.append(number)
    else:
      odd_numbers.append(number)
  return odd_numbers + even_numbers

# Example usage:
numbers = [1, 2, 3, 4, 5]
separated_list = separate_even_odd(numbers)
print(separated_list)  


#Q7

def is_palindrome(text):
  
  # Make the string lowercase and remove non-alphanumeric characters
  processed_text = ''.join(char.lower() for char in text if char.isalnum())

  # Check if the reversed string is equal to the original string
  return processed_text == processed_text[::-1]

# Example usage
text1 = "racecar"
text2 = "hello"

print(is_palindrome(text1)) 
print(is_palindrome(text2))  
