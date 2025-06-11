import numpy as np 	#Array		
import matplotlib.pyplot as plt		
import pandas as pd	
# load the dataset
dataset=pd.read_csv(r"D:\Naresh IT foundation\Python project\simple liner reg modal\Salary_Data.csv")
# this formula will apply entired data set y=mx+c
# split the data set to x and y
x= dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

# there is no missing value we can check by using(dataset.inull() all is false value so will not apply )
'''
from sklearn.impute import SimpleImputer # spyder4

imputer= SimpleImputer()
imputer.fit.transform(x[:,-1])

'''
# this is used for standerd split ration
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor= LinearRegression()   
regressor.fit(x_train,y_train) 
# the moment i fit this regrerssion become ML regression modal(regrssor will hold Ligration model ALGO)
# remaining is y test and x test 

#this will be a predict value (this means what ever this reg mode will build weather this modal is acurate or not ?)
y_pred=regressor.predict(x_test)
# compare predicted  and actual data salieris from the test set
comparison=pd.DataFrame({'Actual':y_test,'predicted':y_pred})

plt.scatter(x_test, y_test,color='red') # real sal data testing
plt.plot(x_train,regressor.predict(x_train),color='blue')# regression
plt.title('Salary vs Experience (Test set)')
plt.xlabel("Years of experience ")
plt.ylabel("Salary")
plt.show()

m_slop=regressor.coef_
print(m_slop)

c_intercept= regressor.intercept_
print(c_intercept)

emp_12y=m_slop*12+c_intercept
print(emp_12y)
