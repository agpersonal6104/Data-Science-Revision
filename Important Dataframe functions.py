# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 22:02:45 2026

@author: emper
"""
import numpy as np
import pandas as pd

marks=pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])

print(marks)

# value_counts(Series and dataframe)
print(marks.value_counts())

ipl=pd.read_csv(r"C:\Users\emper\Downloads\ipl-matches.csv")
movies=pd.read_csv(r"C:\Users\emper\Downloads\movies.csv")

print('------------------------------------')
# find which player has won most potm in finals and qualifiers
a=ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()
print(a)

print('------------------------------------')
# toss decision plot
ipl['TossDecision'].value_counts().plot(kind='pie')

print('------------------------------------')
# how many matches each team has played
b=ipl['Team1'].value_counts()+ipl['Team2'].value_counts()
print(b)

print('============================================')

# sort_values(Series and DataFrame)
x=pd.Series([15,12,1,56,78])
print(x)

print(x.sort_values())

print(movies.columns)

print(movies.sort_values('title_x',ascending=False))
print('--------------------------------------')

print(movies.sort_values(['title_x','year_of_release'],ascending=[False,True]))

print('============================================')

# rank(Series)

batsman=pd.read_csv(r"C:\Users\emper\Downloads\batsman_runs_ipl.csv")
batsman['batting_rank']=batsman['batsman_run'].rank(ascending=False)
print(batsman.sort_values('batting_rank'))

print("====================================")

# sort_index(Series and dataframe)

marks={
       'maths':67,
       'english':57,
       'science':89,
       'hindi':100
}

marks_series=pd.Series(marks).astype(np.int32)
print(marks_series)
print('----------------------------------------')

print(marks_series.sort_index(ascending=False))

print('=====================================')

# set_index(dataframe) -> inplace

print(batsman.head(5))
print('--------------------------------------')
bat2=batsman
bat2.set_index('batter',inplace=True)
print(bat2.head())

print('====================================')

# reset index(Series and Dataframe)
bat2.reset_index(inplace=True)
print(bat2)

print('--------------------------------')
print(type(marks_series))
print(marks_series.reset_index())
print(type(marks_series.reset_index()))

print('====================================')

# rename(Dataframe) -> index

print(movies.columns)
print(movies.rename(columns={'title_x':'title','imdb_id':'imdb'}).columns)
# willl work same in rows

print('==============================')

# unique(Series)
print(ipl['Season'].unique())