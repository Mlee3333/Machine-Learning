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
nltk.download('omw-1.4')
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
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
        corpus.append(" ".join(list1))
    return corpus

Xtraincorpus = transform(Xtrain)

print(Xtraincorpus[0:5])

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(ngram_range=(1,2))
Xtrainnew = cv.fit_transform(Xtraincorpus)
print(Xtrainnew.shape)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(Xtrainnew,ytrain)
trainpred = rfc.predict(Xtrainnew)

print(classification_report(ytrain,trainpred))

Xtestcorpus = transform(Xtest)
Xtestnew = cv.fit_transform(Xtestcorpus)
print(Xtestnew.shape)
'''testpred = rfc.predict(Xtestnew)

print(classification_report(ytest,testpred))

def newSentiment(text):
    trtext = transform(text)
    trtext = cv.fit_transform(trtext)
    textpred = rfc.predict(trtext)
    if textpred[0] == 1:
        print("negative")
    else:
        print("positive")

str1 = ["it is raining outside and i am unhappy"]
str2 = ["the weather is good and i am excited"]

newSentiment(str1)
newSentiment(str2)'''