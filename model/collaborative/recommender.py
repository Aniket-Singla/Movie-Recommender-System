from surprise import Reader, Dataset, SVD, evaluate
import pandas as pd

reader = Reader()
ratings = pd.read_csv(r'C:\Users\HP1\Desktop\work\Recommendation System\input\ratings_small.csv')
ratings.head()
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
data.split(n_folds=5)

svd = SVD()
evaluate(svd, data, measures=['RMSE', 'MAE'])


# print(svd.predict(1, 302))
print('Collaborative Filtering Processing Done')
def get_table(userId):
    return ratings.loc[ratings['userId']==int(userId)]
def get_recommendations_collab(userId , movieId , svd = svd ):
    result = svd.predict(int(userId),int(movieId))
    result1=(str(result).split())
    return result1[9]
# This system matches persons with similar interests and provides recommendations based on this matching. 
# Collaborative filters do not require item metadata like its content-based counterparts.

# The given dataset ratings_small.csv contains the data of 671 users who rated different movies
# userid, movie_id, rating, timestamp