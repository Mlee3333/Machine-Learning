import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

irisdf = pd.read_csv("iris.csv")
print(irisdf.info())
le = LabelEncoder()

y = le.fit_transform(irisdf["species"])
X = irisdf.drop("species",axis=1)
Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state=1)

DTC = DecisionTreeClassifier(criterion="entropy")
DTC.fit(Xtrain,ytrain)
dtcpred = DTC.predict(Xtest)
dtccm = confusion_matrix(ytest,dtcpred)
sns.heatmap(dtccm,annot=True,fmt="d")
plt.show()
print(classification_report(ytest,dtcpred))

RFC = RandomForestClassifier(n_estimators=100)
RFC.fit(Xtrain,ytrain)
rfcpred = RFC.predict(Xtest)
rfccm = confusion_matrix(ytest,rfcpred)
sns.heatmap(rfccm,annot=True,fmt="d")
plt.show()
print(classification_report(ytest,rfcpred))