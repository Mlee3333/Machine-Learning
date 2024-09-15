import pandas as pd



moviedf = pd.read_csv("movies_metadata.csv")
print(moviedf.info())

'''
moviedf.sort_values("vote_average")
print(moviedf.head(15)[["original_title","vote_average"]], " are the top 15 recommended movies by vote average")
'''

#Weighted Rating - 
#(v/v+m)*R + (m/v+m)*C
#v = number of votes -- vote_count 
#m = minimum number of votes required
#R = average rating -- vote_average
#C = mean vote across the whole

m = moviedf["vote_count"].quantile(0.9)
C = moviedf["vote_average"].mean()
print(m)

movies = moviedf.loc[moviedf["vote_count"]>m]

def weightedR(movies):
    v = movies["vote_count"]
    R = movies["vote_average"]
    WR = (v/(v+m))*R + (m/(v+m))*C
    return WR

movies["weighted_rating"] = movies.apply(weightedR,axis = 1)

print(movies.head(10))

movies = movies.sort_values("weighted_rating",ascending= False)

print(movies.head(15)[["original_title","weighted_rating"]], " are the top 15 recommended movies by vote average weighted")