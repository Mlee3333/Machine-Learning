from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics 
import matplotlib.pyplot as plt
import seaborn as sns

set1 = datasets.load_breast_cancer()
print(set1.keys())
cancerdf = pd.DataFrame(set1.data, columns=set1.feature_names)
print(cancerdf.head(5))
print(cancerdf.info())
y = set1.target

Xtrain, Xtest, ytrain, ytest = train_test_split(cancerdf,y,test_size=0.8,random_state=1)
SVC1 = SVC(kernel="linear")
SVC1.fit(Xtrain,ytrain)
testypred = SVC1.predict(Xtest)
trainypred = SVC1.predict(Xtrain)

testcm = metrics.confusion_matrix(ytest,testypred)
traincm = metrics.confusion_matrix(ytrain,trainypred)
print("Test classification report: \n", metrics.classification_report(ytest,testypred))
print("Test accuracy score: \n",metrics.accuracy_score(ytest,testypred))
print("Train classification report: \n", metrics.classification_report(ytrain,trainypred))
print("Train accuracy score: \n", metrics.accuracy_score(ytrain,trainypred))
sns.heatmap(testcm, annot=True,fmt="d")
plt.show()
sns.heatmap(traincm,annot=True,fmt="d")
plt.show()
