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

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y)
scaler = StandardScaler()
scaler.fit_transform(Xtrain)

from sklearn.neighbors import KNeighborsClassifier

KNN = KNeighborsClassifier(n_neighbors=5)
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