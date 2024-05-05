import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

titanicdf = pd.read_csv("titanic.csv")
print(titanicdf.isnull().sum())
print(titanicdf.info())

le = LabelEncoder()
titanicdf["Sex"] = le.fit_transform(titanicdf["Sex"])

titanicdf.drop(["Name"],axis=1,inplace=True)
print(titanicdf.info())
print(titanicdf.corr())
sns.heatmap(titanicdf.corr(),annot=True)
plt.show()

y = titanicdf["Survived"]
X = titanicdf.drop("Survived",axis=1)
print(X,y)

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state=4)
LogReg = LogisticRegression()
LogReg.fit(Xtrain,ytrain)
trainpred = LogReg.predict(Xtrain)
testpred = LogReg.predict(Xtest)
print(trainpred[0:9])
print(ytrain[0:9])
print(testpred[0:9])
print(ytest[0:9])

#confusion matrix

from sklearn.metrics import confusion_matrix

cmatrix = confusion_matrix(ytrain,trainpred)
print(cmatrix)
sns.heatmap(cmatrix,annot=True,fmt="d")
plt.show()

#classfication report

from sklearn.metrics import classification_report

creport = classification_report(ytrain,trainpred)
print(creport)

cmatrix2 = confusion_matrix(ytest,testpred)
sns.heatmap(cmatrix2,annot=True,fmt="d")
plt.show()

testreport = classification_report(ytest,testpred)
print(testreport)
