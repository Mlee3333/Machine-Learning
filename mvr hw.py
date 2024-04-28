import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

Data = pd.read_csv("iris.csv")
print(Data.isnull().sum())

X = Data.drop(columns=["species"])
le = LabelEncoder()
y = le.fit_transform(Data["species"])

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.8,random_state=10)
LR = LinearRegression()
LR.fit(Xtrain,ytrain)
trainPred = LR.predict(Xtrain)
testPred = LR.predict(Xtest)

trainMSE = mean_squared_error(ytrain,trainPred)
trainRMSE = np.sqrt(trainMSE)
print("TrainRMSE  ",trainRMSE)

testMSE = mean_squared_error(ytest,testPred)
testRMSE = np.sqrt(testMSE)
print("TestRMSE  ",testRMSE)