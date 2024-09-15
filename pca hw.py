import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics 
import seaborn as sns

titanicdf = pd.read_csv("titanic.csv")
le = LabelEncoder()
titanicdf["Sex"] = le.fit_transform(titanicdf["Sex"])
titanicdf.drop(["Name"],axis=1,inplace=True)

y = titanicdf["Survived"]
X = titanicdf.drop("Survived",axis=1)

MMS = MinMaxScaler()
scX = pd.DataFrame(MMS.fit_transform(X),columns=X.columns)

PCA1 = PCA(2)
PCAdf = pd.DataFrame(PCA1.fit_transform(scX))

#plt.scatter(PCAdf[0],PCAdf[1],c=[y])
#plt.xlabel("PC1")
#plt.ylabel("PC2")
#plt.show()

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state=1)
SVC1 = SVC(kernel="linear")
SVC1.fit(Xtrain,ytrain)
trainp = SVC1.predict(Xtrain)
testp = SVC1.predict(Xtest)
print("Test classification report: \n", metrics.classification_report(ytest,testp))
print("Train classification report: \n", metrics.classification_report(ytrain,trainp))