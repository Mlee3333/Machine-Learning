import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

Data = pd.read_csv("car.csv")
X = Data.drop("class",axis=1)
le = LabelEncoder()
y = le.fit_transform(Data["class"])
print(y.shape)
X["sales"] = le.fit_transform(X["sales"])
X["maintenance"] = le.fit_transform(X["maintenance"])
X["boot_space"] = le.fit_transform(X["boot_space"])
X["safety"] = le.fit_transform(X["safety"])
X["doors"] = le.fit_transform(X["doors"])
X["persons"] = le.fit_transform(X["persons"])
print(X.shape)

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state=1)

from sklearn.tree import DecisionTreeClassifier
DTC = DecisionTreeClassifier(criterion="entropy")
DTC.fit(Xtrain,ytrain)
trainpred = DTC.predict(Xtrain)
testpred = DTC.predict(Xtest)
print(classification_report(ytrain,trainpred))
sns.heatmap(confusion_matrix(ytrain,trainpred),annot=True,fmt="d")
plt.show()
print(classification_report(ytest,testpred))
sns.heatmap(confusion_matrix(ytest,testpred),annot=True,fmt="d")
plt.show()