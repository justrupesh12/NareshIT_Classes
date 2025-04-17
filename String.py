# Single Line Comment 
letter='p' # A string should be Single character or bunch of characters
print(letter) # p
print(len(letter)) #1
gretting='Hello, World!' #String Should be in Single or Double quotes
print(gretting) # Hello, World!
print(len(gretting)) # 13

sentence ="Hope you are enjoying the 30 day of python challenge"
print(sentence) # Hope you are enjoying the 30 day of python challenge

#multiple line string
multi_line_string = ''' i am a python developer
i am very happy to learning this course with you
after that i will be a full stack developer'''
print(multi_line_string) 

#Another way to doing multi line string
multi_line_string = """ i am a python developer
i am very happy to learning this course with you
after that i will be a full stack developer"""
print(multi_line_string)

#String concatenation
First_name='Rupesh'
last_name='Kumar'
space=''
full_name=First_name+space+last_name # String concatenation
print(full_name) # Rupesh Kumar
#checking the length of the string
print(len(First_name)) # 6
print(len(last_name)) # 5
print(len(First_name)>len(last_name)) #True
print(len(First_name)<len(last_name)) #False
print(len(full_name))# 11

#### unpacking string
langauge='Python'
a,b,c,d,e,f=langauge # unpacking sequence characters into variables 
print(a) # P
print(b) # y     
print(c) # t
print(d) # h
print(e) # o
print(f) # n

## Accessing characters in string by indexing
langauge='Python'
first_letter=langauge[0] # first character of the string
print(first_letter) # P
second_letter=langauge[1] # second character of the string
print(second_letter) # y
last_index=len(langauge)-1 # last character of the string
print(last_index) # 5
last_letter=langauge[last_index] # last character of the string
print(last_letter) # n  

# if we want to access the last character of the string we can also use negative indexing -1 is the last character of the string
langauge='Python'
last_letter=langauge[-1] # last character of the string
print(last_letter) # n
second_last_letter=langauge[-2] # second last character of the string
print(second_last_letter) # o   

# Slicing string
# p=0 y=1 t=2 h=3 o=4 n=5  ####last index= n-1
langauge='Python'
first_three=langauge[0:3] # first three characters of the string ## n=3 last index=n-1=2
print(first_three) # Pyt
last_three=langauge[3:6] # last three characters of the string ## n=3 last index=n-1=5  
print(last_three) # hon

##Anotherer way to slicing string
langauge='Python'
last_three=langauge[-3:] # last three characters of the string 
print(last_three) # hon
last_three=langauge[3:] # last three characters of the string
print(last_three) # hon

## Skiping characters while slicing python String
langauge='Python'
dynamic=langauge[0:6:2] # 0 is staring number and 6 is end number n-1=5 so 5 is the last index and 2 is the step number jumping the characters by 2
print(dynamic) # Pto

## reversing a string
langauge='Python'
reversed=langauge[-1:-7:-1] #this is the reverse of the string
print(reversed) # nohtyP

## Another quick way to reverse a string
langauge='Python'
reversed=langauge[::-1] #this is the reverse of the string
print(reversed) # nohtyP

#Escaping sequence in string
# \n is used for new line(this means line break)

print("hope every one enjoying the python challenge\n DON'T GIVE UP") # line break

# \t is used for tab space
print("hope every one enjoying the python challenge\t DON'T GIVE UP") # Tab space
# hope every one enjoying the python challenge	 DON'T GIVE UP

print('Days\tTopics\tExercises') # Tab space
# Days	Topics	Exercises  output
print('Day 1\t3\t5') # Tab space
#output Day 1	3	5
print('Day 2\t3\t5') # Tab space
#output Day 2	3	5
print('Day 3\t4\t5') # Tab space
#output Day 3	4	5
print('Day 4\t4\t5') # Tab space
#output Day 4	4	5
print('this is a backslash (\\)') # Backslash
#output this is a backslash (\)
print('this is a single quote (\')') # Single quote
print('every programm will start with \"hello world\"') # Double quote
#output every programm will start with "hello world"
##another way to do double quote
print("every programm will start with \"hello world\"") # Double quote
#output every programm will start with "hello world"    



# String methods
#Capitalize() method and title() method
#Difference between capitalize and title is that capitalize will only capitalize the first letter of the string and title will capitalize the first letter of each word in the string
#capitalize() method
Name='rupesh kumar'
print(Name.capitalize()) # Rupesh kumar 
#title() method
Name='rupesh kumar' 
print(Name.title()) # Rupesh Kumar

challenge='thirty days of python'
print(challenge.capitalize()) # Thirty days of python
print(challenge.title()) # Thirty Days Of Python
print(challenge.upper()) # THIRTY DAYS OF PYTHON
print(challenge.lower()) # thirty days of python
print(challenge.swapcase()) # THIRTY DAYS OF PYTHON 
Name='Rupesh Kumar'
print(Name.swapcase()) # rUPESH kUMAR


#count() method
#count() method is used to count the number of occurrences of a substring in a string,substring ,start=.., end=..)
#count() method is case sensitive

challenge='thirty days of python'
print(challenge.count('t')) # 3
print(challenge.count('T')) # 0
print(challenge.count('thirty')) # 1
print(challenge.count('days')) # 1
print(challenge.count('o')) # 2
print(challenge.count('y', 7, 14)) # 1(counting from index 7 to 14 it will count 'days of' for y only)
print(challenge.count('th')) # 2
print(challenge.count('th', 0, 10)) # 1(counting from index 0 to 10 it will count 'thirty days' for th only)

#endswith() method
#endswith() method is used to check if a string ends with a specified suffix or not
# it will return True or False
#endswith() method is case sensitive

challenge='thirty days of python'
print(challenge.endswith('thon')) # True
print(challenge.endswith('th')) # False
print(challenge.endswith('thirty')) # False
print(challenge.endswith('thirty days of python')) # True
print(challenge.endswith('thirty days of python', 0, 30)) # True
print(challenge.endswith('thirty days of python', 0, 10)) # False

#expendtabs() method
#expendtabs() method is used to set the tab size of the string
#replace tab characters with spaces tab size is 8 by default

challenge='thirty\tdays\tof\tpython'
print(challenge.expandtabs())   

##find() method
#find() method is used to find the first occurrence of a substring in a string
# it will return the index of the first occurrence of the substring
# in simple this will give the First index of the substring in the string
# if the substring is not found it will return -1

challenge='thirty days of python'
print(challenge.find('t')) # 0
print(challenge.find('T')) # -1 (not found) 
print(challenge.find("thirty")) # 0
print(challenge.find("days")) # 7


##format() method
#format() method is used to format a string
# it will replace the placeholders with the values
# {} is used as a placeholder  
# {} is used to replace the values in the string

first_name='Rupesh'
Last_name='kumar'
age=28
Country='India'
job='Software '
language='Python'
# using format() method
sentence='i am {} {}. i am {} year old. i am from {}. i am a {} developer and i am learning {} programming.'.format(first_name,Last_name,age,Country,job,language)
print(sentence) # i am Rupesh kumar. i am 28 year old. i am fromIndia. i am a Software developer and i am learning Python programming.

# Area of circle Pie r^2
# using format() method
r=10
pie=3.14
area=pie*r**2
result='The area of the circle with radius{} is {} meters  square'.format(str(r),str(area))
print(result) # The area of the circle with radius10 is 314.0 meters  square


# index() method
#index() method is used to find the first occurrence of a substring in a string

challenge='thirty days of python'
print(challenge.index('t')) # 0
#print(challenge.index('T')) # error (not found)
print(challenge.index('thirty')) # 0
print(challenge.index('days')) # 7

# isalnum() method
#this means no spaces and no special characters in the string
#this will also not accept special characters like @, #, $, %, ^, &, *, (, ), -, +, =, {, }, [, ], ;, :, ", ', <, >, ?, /, \, |, `, ~
# it will only accept letters and numbers
# it will return True or False

challenge='thirty days of python'
print(challenge.isalnum()) # False

challenge='thirtydays'
print(challenge.isalnum()) # True

challenge='300days'
print(challenge.isalnum()) # True

challenge='thirty123'
print(challenge.isalnum()) # True
challenge='thirty@123'
print(challenge.isalnum()) # False
challenge='thirty_123'
print(challenge.isalnum()) # False

## isalpha() method
#this means no spaces and no special characters in the string
#this only accepts letters only
# it will return True or False

# isdicimal() method this only check for number only no other letters or special characters
# it will return True or False
age='28'
print(age.isdecimal()) # True
age='28.5' 
print(age.isdecimal()) # False
age='28.0'        
print(age.isdecimal()) # False


##isidentifier() method check string is valid identifier or not
# it will return True or False
challenge="300days"
print(challenge.isidentifier()) # False(it started with  number which is not valid identifier)
challenge="thirtydays"  
print(challenge.isidentifier()) # True
challenge="thirty_days"     
print(challenge.isidentifier()) # True
challenge="thirty days"


#join() method join(): Returns a concatenated string from the iterable
#join() method is used to join the elements of an iterable (like a list or tuple) into a single string
# it will return a string
# it will join the elements of the iterable with the specified separator

challenge=["thirty", "days", "of", "python"]
sentence="-".join(challenge)# this will join the elements of the list with space as a separator
print(sentence) # thirty-days-of-python

# another example of join() method
challenge=["thirty", "days", "of", "python"]   
sentence=" ".join(challenge)# this will join the elements of the list with space as a separator
print(sentence) # thirty days of python
 
 # Strip() method basically used to remove the spaces from the string
 
text = "   Hello, World!   "
print(text.strip())  # Output: "Hello, World!"

# Strip() method is used to remove the specified characters from the beginning and end of the string
# it will not remove the characters from the middle of the string
challenge = ' thirty days of python '
print(challenge.strip('y')) # 5

challenge='ythirty days of python y'
print(challenge.strip('y')) # output: thirty days of python

### replace(): Replaces substring inside the string with another substring
# replace() method is used to replace a substring with another substring in the string
# it will return a new string with the replaced substring   
# it will not change the original string
# it will replace all the occurrences of the substring in the string
# it will not replace the substring in the middle of the string
# it will replace the substring in the beginning and end of the string  

challenge='hello world'
print(challenge.replace('hello','hi')) # hi world

#split() method
# this is used to  split from left to right it returns a list of strings
# it will split the string into a list of substrings based on the specified separator

challenge='thirty days of python'
print(challenge.split()) # output: ['thirty', 'days', 'of', 'python']
print(challenge.split('_')) # output: ['thirty days of python']
print(challenge.split('t')) # output: ['', 'hir', 'y days of py', 'hon']



# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

