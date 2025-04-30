#1. What is the input() function in Python used for?
#Ans: The input() function in Python is used to take input from the user. 
# It reads a line from input, converts it into a string (stripping a trailing newline),
# and returns that string. The function can also take an optional prompt string as an argument,
# which is displayed to the user before taking input.
#--------------------------------------------------------

#2. How can you accept an integer as input from the user using input()?
#Ans: To accept an integer as input from the user using the input() function,
#int(input()) can be used. This converts the string input from the user into an integer.
#--------------------------------------------------------

#3.How do you accept a float input from the user?
#Ans: To accept a float input from the user, you can use the float() function in combination with input().
# For example: float(input("Enter a float number: ")). This will convert the string input into a float.
#--------------------------------------------------------

#4.How can you take multiple space-separated values as input?
#values = input("Enter multiple space-separated values: ").split()
#print(values)  # Output will be a list of values  
#Enter multiple space-separated values: 10 20 30 40
#Output: ['10', '20', '30', '40']       
#--------------------------------------------------------

#5.How do you check if a number entered by the user is positive, negative, or zero?
'''num=int(input("Enter a number: "))

if num>0:
    print("The number is positive.")
elif num<0:
    print("this number is negative.")
else:
    print("The number is zero.")
    
'''

#--------------------------------------------------------
#6. How do you convert user input to a list of integers?
#Ans: You can convert user input to a list of integers by using the split() method to separate the input string into individual elements,
#and then using a list comprehension or the map() function to convert each element to an integer.

#---------------------------------------------------------
#7. How do you accept a string input and print it in uppercase?
#Ans: You can accept a string input and print it in uppercase using the upper() method.
#------------

#8. Write a Python program that accepts a string and prints the number of vowels in it.
'''
user_input = input("Enter a string: ")  
vowels = "aeiouAEIOU"
count = 0
for char in user_input:
    if char in vowels:
        count+=1
'''
#9.Write a program that takes a number as input and checks if it is even or odd.

'''
user_input=int(input("Please enter your number"))
if user_input%2==0:
  print("Even number")
else:
  print("Odd number")  
  
'''
#---------------------------------------------------------

#10How would you check if a string is a palindrome using input()?
'''
# to check palendrom
name=str(input("Enter the name").lower())
if name==name[::-1]:
  print('palendrom')
else:
  print('not palendrom')

'''
#---------------------------------------------------------

#11 Write a program that takes a number as input and prints its square.
''' 
num=int(input("Enterthe number"))
Square=num**2
print(Square)
or
print(int(input("Enter the number"))**2)
or
print("Square:",num**2)
    
'''
#12Write a program that asks for a number and prints whether it is divisible by 3.
'''
num1=int(input("enter the number"))
if num1%3==0:
  print("Divisible by 3")
else:
  print("Not divisible by 3")


'''
#---------------------------------------------------------

#13How would you check if a number is divisible by both 3 and 7?
'''
num1=int(input("enter the number"))
if num1%3==0 and num1%7==0:
  print("Divisible by both 3 and 7")
else:
  print("Not divisible by both 3 and 7")

'''
#---------------------------------------------------------
#14 How do you accept a list of comma-separated values as input?
'''
values=input("Enter the name:").split(',')
print(values)

'''
#15Write a Python program that takes two numbers as input and prints their product.
'''
values1=int(input("Enter the 1st number:"))
values2=int(input("Enter the 2nd number:"))
print(f"Product of{values1} and {values2}is = {values1*values2} ")
'''

#16.Write a program that checks if the input number is a prime number.
'''

num=int(input("enter the value"))
if num>1:
  for i in range(2,num):
    if num%i==0:
      print("Not a prime number")
      break
  else:
    print("Prime number")
else:
  print("Not a prime number")

'''
#---------------------------------------------------------
#17How can you accept a boolean value (True/False) from the user?
'''

name =(input("please enter true of false:").lower()=="true")
print(name)

'''

#---------------------------------------------------------
#18. Write a program that accepts a string and prints the reverse of that string.
'''
name=input("Enter the name")
print(name[::-1])

'''

#---------------------------------------------------------
#19 Write a program that asks for a user's name and age and prints a message.
'''

name=input("Enter your name ")
age=int(input("enter your age"))
print(f'your name is {name} and your age is {age}')

'''
#---------------------------------------------------------
'''
#20. Write a program to calculate the factorial of a number using input().

num=int(input("Enter the number"))
factorial=1
for i in range(1,num+1):
  factorial=factorial*i
print(factorial)

'''
#---------------------------------------------------------
'''
#21How do you prevent a user from entering an empty string?

userinput=input("Enter the number").strip()
if not userinput:
  print("value cann't be empty")
else:
  print("username :",userinput)

'''
#---------------------------------------------------------
'''
 #22 Write a program to check if the entered number is a perfect square.
 
import math
num=int(input("Enter the number"))
if math.sqrt(num)**2==num:
  print("perfect square")
else:
  print("not a perfect square")

'''
#---------------------------------------------------------
'''
#23.Write a program that asks for a year and determines if it's a leap year.
year=int(input("Enter the year"))
if (year%4==0 and year%100!=0) or(year%400==0):
  print("leap year")
else:
  print("not a leap year")

'''
#---------------------------------------------------------
'''
#24. How can you remove leading and trailing spaces from a string input?
name=input("Enter the name")
print(name.strip())

'''
#---------------------------------------------------------
'''
#25 How do you handle incorrect inputs when you expect an integer using input()?

try:
  num=int(input("Enter the number"))
  print(num)
except ValueError:
  print("invalid input .please enter valid number ")

'''
#---------------------------------------------------------
'''
# 26Write a program that accepts a string and counts the occurrence of a particular character.

name=input("Enter the name").lower()
char=input("Enter the character").lower()
print(f'Occurence of {char} is {name.count(char)}')

'''
#---------------------------------------------------------
'''
#27  How would you convert user input to lowercase using input()?
n=input("Enter the name").lower()
print(n)
'''
#---------------------------------------------------------
'''
#28 Write a program that accepts a number and prints whether it is a multiple of 10.

num=int(input("enter the number"))
if num%10==0:
  print("mutiple of 10")
else:
  print("not a multiple of 10")
'''

#---------------------------------------------------------
'''

#29.How would you check if a string entered by the user contains only alphabets using input()?

value=input("Enter the String").isalpha()=='true'
print(value)

#29 ANOTHER WAY
value=input("Enter the String")
if value.isalpha():
  print("only Alphabets")
else:
  print("not only alphabets")

'''
#---------------------------------------------------------
'''
#30 Write a program to count the number of words in a sentence entered by the user.
sentence=input("Enter the sentence")
split=sentence.split()
print(len(split))
#print(f'number of word in sentence:=len(sentence.split()))

'''
#---------------------------------------------------------
'''


#31. How would you accept a date input from the user in Python?
from datetime import datetime
date_str=input("Enter the date(yyyy-mm-dd):")
date_obj=datetime.strptime(date_str,"%Y-%m-%d")
print(date_obj)

'''
#---------------------------------------------------------
'''


#32. Write a program that checks if the entered number is divisible by both 3 and 5.
n=int(input("Enter the number"))
if n%3==0 and n%5==0:
  print("Divisible by both 3 and 5")
else:
  print("Not divisible by both 3 and 5")
  
  '''

#---------------------------------------------------------
'''
#33 Write a program to swap the values of two variables using input().
n1=int(input("enter the 1st number"))
n2=int(input("enter the 2nd number"))
print("before swapping the numbers are",n1,n2)
n1,n2=n2,n1
print("after swapping the numbers are",n1,n2)
'''
#---------------------------------------------------------
'''
#34. Write a program to take user input and print it without spaces between words.
name=input("Enter the name")
print(name.replace(" ",""))

'''
#---------------------------------------------------------
'''
#35. How do you validate if an entered input is a valid email address?
import re
email=input("Enter the email")
if re.match(r"[^@]+@[^@]+\.[^@]+",email)
  print("valid email")
else:
  print("invalid email")
  
  '''
 #---------------------------------------------------------
'''

#36 Write a program that accepts a number and prints its cube.
n=int(input("Enter the number"))
print(n**3)

'''
#---------------------------------------------------------
'''
 #37.How would you accept and store multiple names from the user?
name=input('Enter the names').split(',')
print(name)
'''
#---------------------------------------------------------
'''
#38How would you extract numbers from a string entered by the user?
import re
text=input("Enter the text")
numbers=re.findall(r'\d+',text)
print(numbers)

'''
#---------------------------------------------------------
'''
#39. How do you find the maximum number from a list of integers entered by the user?
num=list(map(int,input("Enter the numbers").split(',')))
print(max(num))

'''
#---------------------------------------------------------
'''
#40. How would you prompt the user for input until they enter a valid number?
while True:
  try:
    num=int(input('enter valid number :'))
    break
  except ValueError:
    print("invalid input.please enter a valid number")
'''
#---------------------------------------------------------
'''

#41. Write a program to check if the entered string has digits.
user_input=input("Enter the latter")
if any(char.isdigit() for char in user_input):
  print("contain digit")
else:
  print("not contain digit")
  
  '''
#---------------------------------------------------------
'''


#42. Write a program to check if the entered string has only whitespace character
text=input("Enter the text")
if text.isspace():
  print("only whitespace character")
else:
  print("not only whitespace character")
    
    
    '''
#---------------------------------------------------------


'''

# 43. Write a program to find the sum of all digits in a string entered by the

text=input("Enter the text")
sum=0
for char in text:
  if char.isdigit():
    sum+=int(char)
print(sum)

'''
#---------------------------------------------------------
'''

#44. Write a program that accepts a number and prints its absolute value.
num=int(input("enter the number"))
print(abs(num))

'''
#---------------------------------------------------------
''' 

#45. How would you check if a string entered by the user contains any uppercase letters?
text=input("enter the number ")
if any(char.isupper() for char in text):
    print("contain uppercase")
else:
    print("Not contain upper case in string")
    
    
'''
#---------------------------------------------------------
'''
#46Write a program that converts Celsius to Fahrenheit.
celcius=int(input("Enter the celcius value"))
F=(celcius*9/5)+32
print(F)

'''
#---------------------------------------------------------
'''
#47.Write a program to find the average of a list of numbers entered by the user.
num=list(map(int,input("enter the number").split(',')))
print(sum(num)/len(num))

'''
#---------------------------------------------------------
'''
#48. Write a program to count the number of consonants in a string entered by the user.
user_input=input("enter the text").lower()
count=0
for char in user_input:
  if char not in 'aeiou':
    count+=1
print(count)

'''
#---------------------------------------------------------
'''
#49. How do you check if a string entered by the user contains any punctuation?
import string
user_input=input("enter the text")
if any(char in string.punctuation for char in user_input):
  print("contain punctuation")
else:
  print("not contain Punctuation")
  
'''
#---------------------------------------------------------
'''
#50.Write a program that accepts a sentence and prints the longest word.
sentence=input("Enter the sentence").split()
longest_word=max(sentence,key=len)
print(longest_word)

'''