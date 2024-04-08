import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([1,3,2,3,5])
plt.scatter(x,y)
plt.show()
#m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi – mean(x))^2)
meanx = np.mean(x) #x.mean()
meany = np.mean(y) #y.mean()

m = np.sum((x-meanx) * (y-meany))/np.sum((x-meanx)**2)
print(m)

#c = mean(y) – m * mean(x)

c = meany-m*meanx
print(c)

predy = m*x+c
plt.figure()
plt.plot(x,predy,"r-o")
plt.scatter(x,y)
plt.show()

#Root Mean Squared Error(RMSE)

RMSE = np.sqrt(np.mean((predy-y)**2))
print(RMSE)

#direct implementation

from sklearn.linear_model import LinearRegression
LR = LinearRegression()
x = x.reshape(-1,1)
LR.fit(x,y)
print("m",LR.coef_,"c",LR.intercept_)
predY = LR.predict(x)
print(predy)
print(predY)

#MSE
from sklearn.metrics import mean_squared_error
MSE = mean_squared_error(y,predY)
RMSE2 = np.sqrt(MSE)
print(RMSE2)