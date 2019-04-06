import pandas as pd 
import numpy as np 
df1=pd.read_csv(r'C:\Users\HP1\Desktop\work\Recommendation System\input\tmdb_5000_credits.csv')
df2=pd.read_csv(r'C:\Users\HP1\Desktop\work\Recommendation System\input\tmdb_5000_movies_with_images.csv')

df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')
# print(df2.head())

# Demographic Filtering

C= df2['vote_average'].mean()
m= df2['vote_count'].quantile(0.9)
q_movies = df2.copy().loc[df2['vote_count'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    print(v, R, C, m)
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)
# q_movies = q_movies[['title', 'vote_count', 'vote_average', 'score','id']].head(30)
print('Demographic Processing Over')
def return_top(num,q_movies=q_movies):
    
    print(q_movies.shape)
    return q_movies[['title', 'image_url', 'score','id']].head(num)


    

