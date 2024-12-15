import pandas as pd

gamedf = pd.read_csv("game/games.csv")
print(gamedf.info())

gamedf["rating"] = gamedf["positive_ratio"]/10

m = gamedf["user_reviews"].quantile(0.9)
C = gamedf["rating"].mean()
print(C)

games = gamedf.loc[gamedf["user_reviews"]>m]

def weightedR(games):
    v = games["user_reviews"]
    R = games["rating"]
    WR = (v/(v+m))*R + (m/(v+m))*C
    return WR

games["weighted_rating"] = games.apply(weightedR,axis = 1)

print(games.head(10))

games = games.sort_values("weighted_rating",ascending= False)

print("Top 15 most recommended games: \n", games.head(15)[["title","weighted_rating"]])