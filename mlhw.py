import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

bankdf = pd.read_csv("bank/bank-full.csv",sep=";")
print(bankdf.head(5))
print(bankdf.info())

bankdf.drop(["contact","day","month","poutcome"],axis=1,inplace=True)
le = LabelEncoder()
col = ["job","marital","education","default","housing","loan","y"]
for i in col:
    bankdf[i] = le.fit_transform(bankdf[i])

y = bankdf["y"]
X = bankdf.drop(["y"],axis=1)

MMS = MinMaxScaler()
scaledX = pd.DataFrame(MMS.fit_transform(X),columns=X.columns)
print(scaledX.head(5))

PCA1 = PCA(9)
PCAdf = pd.DataFrame(PCA1.fit_transform(scaledX))

plt.scatter(PCAdf[0],PCAdf[1],c=[y])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state=1)
LR = LinearRegression()
LR.fit(Xtrain,ytrain)
trainPred = LR.predict(Xtrain)
testPred = LR.predict(Xtest)

trainRMSE = np.sqrt(np.mean((trainPred-ytrain)**2))

testRMSE = np.sqrt(np.mean((testPred-ytest)**2))

f1 = []
for i in range (2,10):
    KNN = KNeighborsClassifier(n_neighbors=i)
    KNN.fit(Xtrain,ytrain)
    pred = KNN.predict(Xtrain)
    f1.append(f1_score(ytrain,pred,average="macro"))

plt.plot(range(2,10),f1)
plt.show()
     
KNN = KNeighborsClassifier(n_neighbors=3)
KNN.fit(Xtrain,ytrain)
trainpred = KNN.predict(Xtrain)
KNN.fit(Xtest,ytest)
testpred = KNN.predict(Xtest)

TrainRMSE = np.sqrt(np.mean((trainpred-ytrain)**2))

TestRMSE = np.sqrt(np.mean((testpred-ytest)**2))

print("TrainRMSE (linear)  ",trainRMSE)
print("TestRMSE (linear)  ",testRMSE)
print("TrainRMSE (KNN)  ",TrainRMSE)
print("TestRMSE (KNN)  ",TestRMSE)