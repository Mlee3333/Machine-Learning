import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import StandardScaler


incomedf = pd.read_csv("adult_income.csv",sep=", ")
print(incomedf.info())
le = LabelEncoder()
RUS = RandomUnderSampler()
SS = StandardScaler()

y = le.fit_transform(incomedf["income"])
print(pd.Series(y).value_counts())
X = incomedf.drop("income",axis=1)
columns = ["workclass","education","marital-status","occupation","relationship","race","gender","native-country"]
X["fnlwgt"] = SS.fit_transform(X["fnlwgt"].reshape(1,-1))

for i in columns:
    X[i] = le.fit_transform(X[i])

X,y = RUS.fit_resample(X,y)
Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state=1)

RFC = RandomForestClassifier(n_estimators=100)
RFC.fit(Xtrain,ytrain)
pred = RFC.predict(Xtest)
print(pred)
cm = confusion_matrix(ytest,pred)
sns.heatmap(cm,annot=True,fmt="d")
plt.show()
print(classification_report(ytest,pred))