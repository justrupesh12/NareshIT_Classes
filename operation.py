## Arithimatic Operations
#integers  
print('Addition : ', 1 + 2)
print('Subtraction : ', 2 - 1)
print('Multiplication : ', 2 * 3)
print('Division : ', 4 / 2) # Division in python gives floating number
print('Division :', 6/2)
print("Division :",7//2) # given without floating number or without the remaining
print('modulus :', 3%2) # gives the remainder
print("Division Without the reminder:", 7//3)
print('exponential :', 3**2) # it means 3*3

#Floating Numbers 
print('Floating Number,PI', 3.14)
print('Floating number ,Gravity', 9.81)

#complex numbers 
print('Complex number :', 1 + 1j)
print('Multiplying complex number :',(1+1j)*(1-1j))#out put is 2.0


a=2 # a is a variable name and 2 is an integer data type
b=3 # b is a variable name and 3 is an integer data type
total=a+b
diff=a-b
product=a*b
Division=a/b
reminder=a%b
Floor_division=a//b# which not return the floating number
exponential=a**b

# Decleration value organizing them together
num_one=3
num_two=4

# Arithmetic operations
total=num_one+num_two
diff=num_two-num_one
product=num_one*num_two
div=num_two/num_one
reminder=num_two%num_one

#printing values with label
print('total:',total)
print('difference:',diff)
print('multiply:',product)
print('division:',div)
print('remider:',reminder)


##calculating the area of a circle
r=10
pi=3.14
area=pi*r**2
print(f'Area of circle with radius {r} is {area}')

#calculating the area of a rectangle
l=15
b=10
area=l*b
print('Area of rectengel with length {l} and breadth {b} is {area}'.format(l=l,b=b,area=area))

#Calulate a weight of an object
mass=10 # mass in kg
gravity=9.81 # gravity in m/s^2
weight=mass*gravity # weight in Newton
print(f"Weight of an object with mass {mass} kg is {weight} N")

## true false condition



print(3>2) # True
print(3<2) # False  
print(3==2) # False
print(3!=2)# means 3 is not equal to 2 # True
print(3>=2) # True becuase 3 is greater than 2
print(3<=2) # False because 3 is not less than or equal to 2
print(3 is 2) # False because 3 is not equal to 2


## boolean comparison
print('true==true:',True==True) # True
print('true==false:',True==False) # False
print('false==false:',False==False) # True
print('true and true:',True and True) # True
print('true and false:',True and False) # False 
print('false and false:',False and False) # False
print('true or true:',True or True) # True
print('true or false:',True or False) # True    
print('false or false:',False or False) # False
print('true or false:',True or False) # True


#another Way of doing the same thing

print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False