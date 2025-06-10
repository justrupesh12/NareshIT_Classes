# IMPORT LIBRARY
import numpy as np 	#Array		

import matplotlib.pyplot as plt		

import pandas as pd	

# IMPORT THE DATASET

dataset=pd.read_csv(r'D:\Naresh IT foundation\Python project\Data preprocessing(ML)\Data.csv')
# INDEPENDENT VARIABLE
X = dataset.iloc[:, :-1].values	
# DEPENDENT VARIABLE
y = dataset.iloc[:,3].values  

# SKLEARN FILL MISSING NUMERICAL VALUE
from sklearn.impute import SimpleImputer

imputer = SimpleImputer() 

imputer = imputer.fit(X[:,1:3]) 

X[:, 1:3] = imputer.transform(X[:,1:3]) 


from sklearn.preprocessing import LabelEncoder

lebelEncoder_X=LabelEncoder()

lebelEncoder_X.fit_transform(X[:,0])
X[:,0]=lebelEncoder_X.fit_transform(X[:,0])


lebelEncoder_y=LabelEncoder()
y=lebelEncoder_y.fit_transform(y)


# Split the Data ratio(80-20)

from sklearn.model_selection import train_test_split


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0) # the value not suffle so we are using the Random_state

