import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import linear_kernel

booksdf = pd.read_csv("BooksDataset.csv")
print(booksdf.info())
print(booksdf["Description"].head(5))

print(booksdf.isnull().sum())

booksdf["Description"] = booksdf["Description"].fillna("")
print(booksdf.isnull().sum())
desc = booksdf["Description"][0:35000]

Vect = TfidfVectorizer(stop_words="english")
matrix = Vect.fit_transform(desc)
print(matrix.shape)
print(Vect.get_feature_names_out()[19000:19010])

linearK = linear_kernel(matrix,matrix)
print(linearK.shape)
print(linearK[0:3])

indices = pd.Series(booksdf.index,index=booksdf["Title"])
print(indices.head(5))

def recommender(title):
    index = indices[title]
    print(index)
    simscores = list(enumerate(linearK[index]))
    sss = sorted(simscores,key=lambda x : x[1],reverse=True)
    selectedid = [i[0]for i in sss]
    title = booksdf["Title"][selectedid]
    return title[1:11]

print(recommender("J. K. Rowling: The Wizard Behind Harry Potter"))