import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

cancerdata = load_breast_cancer()
cancerdf = pd.DataFrame(cancerdata["data"],columns=cancerdata["feature_names"])
print(cancerdf.head(5))
#print(cancerdf.info())

MMS = MinMaxScaler()
scaleddf = pd.DataFrame(MMS.fit_transform(cancerdf),columns=cancerdf.columns)
print(scaleddf.head(5))

PCA1 = PCA(2)
PCAdf = pd.DataFrame(PCA1.fit_transform(scaleddf))
print(PCAdf.shape, scaleddf.shape)
print(PCAdf.head(5))

plt.scatter(PCAdf[0],PCAdf[1],c=cancerdata["target"])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()


PCA2 = PCA(4)
PCADF = pd.DataFrame(PCA2.fit_transform(scaleddf))
print(PCADF.head(5))