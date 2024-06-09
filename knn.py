import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

Data = pd.read_csv("iris.csv")
X = Data.drop("species",axis=1)
le = LabelEncoder()
y = le.fit_transform(Data["species"])

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state=4)
scaler = StandardScaler()
scaler.fit_transform(Xtrain)

from sklearn.neighbors import KNeighborsClassifier
#finding the best k value
from sklearn.metrics import f1_score
f1 = []
for i in range (2,10):
    KNN = KNeighborsClassifier(n_neighbors=i)
    KNN.fit(Xtrain,ytrain)
    pred = KNN.predict(Xtrain)
    f1.append(f1_score(ytrain,pred,average="macro"))

plt.plot(range(2,10),f1)
plt.plot(range(2,10),[max(f1)for i in range(2,10)],"r")
plt.show()
     
KNN = KNeighborsClassifier(n_neighbors=6)
KNN.fit(Xtrain,ytrain)
trainpred = KNN.predict(Xtrain)

from sklearn.metrics import classification_report, confusion_matrix

cmtrain = confusion_matrix(ytrain,trainpred)
sns.heatmap(cmtrain,annot=True,fmt="d")
plt.show()

crtrain = classification_report(ytrain,trainpred)
print(crtrain)

#Test
scaler.fit_transform(Xtest)
testpred = KNN.predict(Xtest)
cmtest = confusion_matrix(ytest,testpred)
sns.heatmap(cmtest,annot=True,fmt="d")
plt.show()

crtest = classification_report(ytest,testpred)
print(crtest)
