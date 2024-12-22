import pandas as pd
from sklearn.model_selection import train_test_split

sentimentdf = pd.read_csv("sentiments.txt",sep=";",names=["text","label"])
print(sentimentdf.head(5))
sentimentdf["label"]=sentimentdf["label"].replace({"sadness":1,"anger":1,"fear":1,"joy":0,"love":0,"surprise":0})

X = sentimentdf["text"]
y = sentimentdf["label"]

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.2,random_state=1)

print(ytest.value_counts())
print(ytrain.value_counts())

import nltk
nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
wne = WordNetLemmatizer()
import re

def transform(data):
    corpus = []
    for i in data:
        newi = re.sub("[^a-zA-Z]"," ",i)
        newi = newi.lower()
        newi = newi.split()
        list1 = [wne.lemmatize(word)for word in newi if word not in stopwords.words("english")]
        corpus.append(list1)
    return corpus

Xtraincorpus = transform(Xtrain)

print(Xtraincorpus[0:5])