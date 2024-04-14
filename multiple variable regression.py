import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

Data = pd.read_csv("HousingData.csv")
Data = Data[["RM","LSTAT","MEDV"]]
print(Data.isnull().sum())
print(Data.info())
Data = Data.dropna()
print(Data.shape)
print(Data.isnull().sum())
X = Data[["RM","LSTAT"]]
y = Data["MEDV"]

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.8,random_state=1)
LR = LinearRegression()
LR.fit(Xtrain,ytrain)
print("m1=",LR.coef_[0],"m2=",LR.coef_[1],"c=",LR.intercept_)
trainPred = LR.predict(Xtrain)
testPred = LR.predict(Xtest)

trainMSE = mean_squared_error(ytrain,trainPred)
trainRMSE = np.sqrt(trainMSE)
print(trainRMSE)

testMSE = mean_squared_error(ytest,testPred)
testRMSE = np.sqrt(testMSE)
print(testRMSE)