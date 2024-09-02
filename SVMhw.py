import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics 
import matplotlib.pyplot as plt
import seaborn as sns

heartdf = pd.read_csv("heart.csv")
print(heartdf.info())
y = heartdf["target"]
X = heartdf.drop("target",axis=1)

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state=1)
SVC1 = SVC(kernel="linear")
SVC1.fit(Xtrain,ytrain)
trainp = SVC1.predict(Xtrain)
testp = SVC1.predict(Xtest)
trainCM = metrics.confusion_matrix(ytrain,trainp)
testCM = metrics.confusion_matrix(ytest,testp)
sns.heatmap(trainCM,annot=True,fmt="d")
plt.show()
sns.heatmap(testCM,annot=True,fmt="d")
plt.show()
print("Test accuracy score: \n",metrics.accuracy_score(ytest,testp))
print("Train accuracy score: \n", metrics.accuracy_score(ytrain,trainp))
print("Test classification report: \n", metrics.classification_report(ytest,testp))
print("Train classification report: \n", metrics.classification_report(ytrain,trainp))