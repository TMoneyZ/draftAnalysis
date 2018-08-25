import pandas as pd
import numpy as np

espnDF = pd.read_csv('csv/espn.csv')
rookieDF = pd.read_csv('csv/rookie.csv')

print(rookieDF['position'].unique())
s = pd.merge(rookieDF, espnDF, how='left', on=['name'])
print(s.shape)

# wikipedia position labels
s.drop(s[s.position_x.isin(['OT','G','LS','C','P'])].index, inplace=True)
print(s['position_x'].unique())
print(s.iloc[0])
# print(s[pd.isnull(s.id)])
print(s[pd.isnull(s.id)][['overall','team_x','name','id','position_x']])

# only save to rookie_id.csv when ready
s.to_csv('csv/rookie_id.csv', index=False)
