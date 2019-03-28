import pandas as pd 
import numpy as np 
import json
from model.demographic.download_image import get_image
df1=pd.read_csv(r'C:\Users\HP1\Desktop\work\Recommendation System\input\tmdb_5000_credits.csv')
df2=pd.read_csv(r'C:\Users\HP1\Desktop\work\Recommendation System\input\tmdb_5000_movies.csv')

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
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)
def return_top(num,q_movies=q_movies):
    
    q_movies = q_movies[['title', 'vote_count', 'vote_average', 'score','id']].head(num).set_index(pd.Index(range(num)))
    # q_movies['image_url'] = q_movies['id'].apply(get_image)
    q_movies['image_url'] = q_movies.apply(lambda x: get_image(x['id']), axis=1)
    print(q_movies.shape)
    # return q_movies[['title', 'vote_count', 'vote_average', 'score','id']].set_index(pd.Index(q_movies['id'])).head(num)
    return q_movies[['title', 'image_url', 'score','id']]
##

# print(list(return_top(10)['image_url']))
##pop= df2.sort_values('popularity', ascending=False)
##import matplotlib.pyplot as plt
##plt.figure(figsize=(12,4))
##
##plt.barh(pop['title'].head(6),pop['popularity'].head(6), align='center',
##        color='skyblue')
##plt.gca().invert_yaxis()
##plt.xlabel("Popularity")
##plt.title("Popular Movies")

    

