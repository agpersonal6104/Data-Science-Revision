# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:17:21 2026

@author: emper
"""

import pandas as pd

ipl=pd.read_csv(r'C:\Users\emper\Downloads\ipl-matches.csv')

print(ipl.head())
print(ipl.columns)

#find all the final winners
mask=ipl['MatchNumber']=='Final'
new_df=ipl[mask]#stored only teams that have played the final match
print(new_df)
print(new_df[['Season','WinningTeam']])

#fancy Indexing
print(ipl[ipl['MatchNumber']=='Final'][['Season','WinningTeam']])

print('-------------------------------')

# How amny Superovers have occured
print(ipl[ipl['SuperOver']=='Y'].shape[0])

print('-------------------------------')

# How many matched has CSK won in Kolkata
print(ipl[(ipl['City']=='Kolkata') & (ipl['WinningTeam']=='Chennai Super Kings')])

print('-------------------------------')

# Toss winner is match winner in percentage
print(ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0]/ipl.shape[0])

print('--------------------------------')

# Action movies with higher rating than 7.5
# mask1=movies['genre'].str.split('|').apply(lambda x:'Action' in s)
# mask1=movies['genre'].str.contains('Action')
# mask2=movies['imdb_rating']>7.5
# movies[mask1 & mask2]

# Write a function that can return the track records if 2 teams against each other

#Important dataframe functions

#astype
print(ipl.info())
ipl['ID']=ipl['ID'].astype('int32')

print('--------------------------------')
print(ipl.info())