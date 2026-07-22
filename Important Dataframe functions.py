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