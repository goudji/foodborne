
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor

from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC



def randomForestRegressor(dataset):
 #Importing data and creating datasets
  
  
  scaler = StandardScaler()
  df=pd.read_csv("salmonella.csv",sep=',')
  
  
  X=df.iloc[:,2:6]
  Y=df.iloc[:,6]
  x=np.array(X)
  y=np.array(Y)
  p=y
  
  y=np.reshape(y, (25,1))
  
  
  
  enc = OneHotEncoder(handle_unknown='ignore',sparse=False)
  
  y=enc.fit_transform(y)
  
  #scaling data using standard scalar
  x=scaler.fit_transform(x)
  y=scaler.fit_transform(y)
 # x, x_test, y, y_test = train_test_split(x, y, test_size=0.20, random_state=42)
  #Splitting the code into test and train dataset
  
  
  
  
  
  regr = linear_model.LinearRegression()
  regr2=DecisionTreeRegressor()
  regr3=RandomForestRegressor()
  #Fitting the model onto the data
  regr.fit(x,y)
  regr2.fit(x,y)
  regr3.fit(x,y)


  print(dataset)
  #Making a prediction on the test dataset
  pred=regr.predict(dataset)
  pred2=regr2.predict(dataset)
  pred3=regr3.predict(dataset)

  inverted = enc.inverse_transform(pred3)

  inverted=inverted.astype(str)

  
  return inverted

