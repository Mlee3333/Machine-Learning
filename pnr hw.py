import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import LabelEncoder

Data = pd.read_csv("iris.csv")
print(Data.isnull().sum())
print(Data.info())
X = Data.drop("species",axis=1)
le = LabelEncoder()
y = le.fit_transform(Data["species"])

trainX,testX,trainy,testy = train_test_split(X,y,test_size=0.2,random_state=8)
pf = PolynomialFeatures(2)
polytrainX = pf.fit_transform(trainX)
polytestX = pf.fit_transform(testX)

lr = LinearRegression()
lr.fit(polytrainX,trainy)
pred = lr.predict(polytestX)

MSE = mean_squared_error(testy,pred)
RMSE = np.sqrt(MSE)
print("RMSE= ",RMSE)

#PF1 RMSE = 0.2521
#PF2 RMSE = 0.2126
#PF3 RMSE = 0.2352
#PF4 RMSE = 0.5672
#PF5 RMSE = 23.325