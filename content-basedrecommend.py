import pandas as pd

moviesdf = pd.read_csv("movies_metadata.csv")
print(moviesdf.info())
print(moviesdf["overview"].head(5))

from sklearn.feature_extraction.text import TfidfVectorizer

Vect = TfidfVectorizer(stop_words="english")

print(moviesdf.isnull().sum())
#empty = moviesdf[moviesdf["overview"].isnull()]
#print(empty["genres"])

moviesdf["overview"] = moviesdf["overview"].fillna("")
print(moviesdf.isnull().sum())
matrix = Vect.fit_transform(moviesdf["overview"])
print(matrix.shape)
print(Vect.get_feature_names_out()[2000:2010])

from sklearn.metrics.pairwise import linear_kernel

linearK = linear_kernel(matrix,matrix)
print(linearK.shape)
print(linearK[0:3])

indices = pd.Series(moviesdf.index,index=moviesdf["title"])
print(indices.head(5))

def recommender(title):
    index = indices[title]
    similarityscores = list(enumerate(linearK[index]))
    sss = sorted(similarityscores,key=lambda x : x[1],reverse=True)
    selectedmovieid = [i[0]for i in sss]
    title = moviesdf["title"][selectedmovieid]
    return title

print(recommender("The Dark Knight Rises"))