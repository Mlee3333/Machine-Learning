import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

Data = pd.read_csv("HousingData.csv")
Data = Data[["RM","LSTAT","MEDV"]]
print(Data.isnull().sum())
print(Data.info())
Data = Data.dropna()
print(Data.shape)
print(Data.isnull().sum())
X = Data[["RM","LSTAT"]]
y = Data["MEDV"]

trainX,testX,trainy,testy = train_test_split(X,y,test_size=0.2,random_state=4)
pf = PolynomialFeatures(2)
polytrainX = pf.fit_transform(trainX)
print(polytrainX)
polytestX = pf.fit_transform(testX)

lr = LinearRegression()
lr.fit(polytrainX,trainy)
pred = lr.predict(polytestX)

MSE = mean_squared_error(testy,pred)
RMSE = np.sqrt(MSE)
print("RMSE= ",RMSE)