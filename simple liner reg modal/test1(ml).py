import numpy as np 	#Array		
import matplotlib.pyplot as plt		
import pandas as pd	
# load the dataset
dataset=pd.read_csv(r"D:\Naresh IT foundation\Python project\simple liner reg modal\Salary_Data.csv")
# INDEPENDENT VARIABLE
x = dataset.iloc[:, :-1].values	
# DEPENDENT VARIABLE
y = dataset.iloc[:,-1].values  
# Split the Data ratio(80-20)
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression

regression = LinearRegression()
regression.fit(x_train,y_train)

y_pred=regression.predict(x_test)

comparison=pd.DataFrame({'Actual':y_test,'predicted':y_pred})

plt.scatter(x_test,y_test,color='red')
plt.plot(x_train,regression.predict(x_train),color='blue')
plt.title('Salary vs Experience (test set')
plt.xlabel("year of experience ")
plt.ylabel("Salary")
plt.show()

m_slop=regression.coef_
print(m_slop)

c_intercept= regression.intercept_
print(c_intercept)

emp_12y=m_slop*12+c_intercept
print(emp_12y)
