# Variable in Python
First_name='Rupesh'
Last_name='Kumar'
city='hydrabad'
age=40087
is_married=False
skills=['python','java','c++']

personal_info={
    'First_name':'Putush',
    'Last_name':'Kumar',
    'city':'Bangalore',
    'age':28,
    'is_married':True,
    'skills':['python','java','Ruby','C++']
}
    
## print the value store in the variable 

print("First name is :" + First_name)
print("last name is "+ Last_name)
print('city is '+ city)
print('age is '+ str(age)) # type casting
print("is married? "+str(is_married)) # type casting
print('my skills are: '+ str(skills)) # type casting
print('my personal info is: '+ personal_info) 

## Variable Assignment in one line
First_name,Last_name,city,age,is_married,skills = 'Rupesh','Kumar','hydrabad',40087,False,['python','java','c++']
print("First name is :" + First_name)
print("last name is "+ Last_name)
print('city is '+ city)
print('age is '+ str(age)) # type casting
print("is married? "+str(is_married)) # type casting
print('my skills are: '+ str(skills)) # type casting
