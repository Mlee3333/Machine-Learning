import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

salarydf = pd.read_csv("Salary.csv")
x = salarydf["YearsExperience"]
x = np.array(x)
y = salarydf["Salary"]

meanx = np.mean(x)
meany = np.mean(y)
m = np.sum((x-meanx) * (y-meany))/np.sum((x-meanx)**2)
c = meany-m*meanx
predy = m*x+c
plt.figure()
plt.plot(x,predy,"g")
plt.scatter(x,y)
plt.show()

LR = LinearRegression()
x = x.reshape(-1,1)
LR.fit(x,y)
predY = LR.predict(x)

RMSE = np.sqrt(np.mean((predY-y)**2))
print("RMSE=",RMSE)

from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(y,predY)
RMSE = np.sqrt(MSE)
print(RMSE)