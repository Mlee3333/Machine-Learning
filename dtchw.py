import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from imblearn.under_sampling import RandomUnderSampler

bankdf = pd.read_csv("bank.csv",sep=";")
print(bankdf.info())
X = bankdf.drop(["y","poutcome","contact","day","month","education"],axis=1)
le = LabelEncoder()
y = le.fit_transform(bankdf["y"])
RUS = RandomUnderSampler(sampling_strategy="majority")
X,y = RUS.fit_resample(X,y)
print(bankdf["y"].value_counts())
X["job"] = le.fit_transform(X["job"])
X["marital"] = le.fit_transform(X["marital"])
X["default"] = le.fit_transform(X["default"])
X["housing"] = le.fit_transform(X["housing"])
X["loan"] = le.fit_transform(X["loan"])

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state=1,stratify=y)
print(pd.Series(ytrain).value_counts())
print(pd.Series(ytest).value_counts())
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