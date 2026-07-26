# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 18:18:20 2026

@author: emper
"""

import numpy as np
import pandas as pd

movies=pd.read_csv(r"C:\Users\emper\Downloads\imdb-top-1000.csv")
print(movies.columns)
print(movies.shape)
print(movies.head(2))

print('------------------------------------')

genres=movies.groupby('Genre')
print(genres)
print('------------------------------------')
# Apply aggregate functions
print(genres.sum())
print(genres.min())

print('====================================')

# Find top 3 genres by total earning
print(genres.sum()['Gross'].sort_values(ascending=False).head(3)) # saare numerical sols mai sum laga rahe ho
print('------------------------------------')
print(genres['Gross'].sum().sort_values(ascending=False).head(3)) #Better and Faster: Gross wala column nikalke uspe sum laga rahe ho

print('====================================')
# Find the genre with highet avg IMDB rating
print(genres['IMDB_Rating'].mean().sort_values(ascending=False).head(1))

print('=====================================')
# Most popular director
director=movies.groupby('Director')
print(movies.columns)
print('-------------------------------------')
print(director['No_of_Votes'].sum().sort_values(ascending=False).head(1))

print('======================================')
# Find highest rated movie of ech genre
print(genres['IMDB_Rating'].max().sort_values(ascending=False).head(1))

print('======================================')
# Find number if movies done by each actor
print(movies['Star1'].value_counts())
print('--------------------------------------')
protagonist=movies.groupby('Star1')
print(protagonist['Series_Title'].count().sort_values(ascending=False))

print('======================================')
# Find the total number of groups formed by groupby
print(len(movies.groupby('Genre')))
print(movies['Genre'].nunique())

print('=====================================')
# Rows present in each group
print(movies.groupby('Genre').size())
print('----------------------------------------')
print(movies['Genre'].value_counts())