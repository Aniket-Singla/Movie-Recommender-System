import pandas as pd 
import numpy as np 
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from model.demographic.download_image import get_image

df1=pd.read_csv(r'C:\Users\HP1\Desktop\work\Recommendation System\input\tmdb_5000_credits.csv')
df2=pd.read_csv(r'C:\Users\HP1\Desktop\work\Recommendation System\input\tmdb_5000_movies.csv')

df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')

tfidf = TfidfVectorizer(stop_words='english')
df2['overview'] = df2['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df2['overview'])
tfidf_matrix.shape


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    result = df2.iloc[movie_indices]
    result['image_url'] = result['id'].apply(get_image)

    return result[['id','title','image_url']]

# print(get_recommendations('The Dark Knight Rises'))