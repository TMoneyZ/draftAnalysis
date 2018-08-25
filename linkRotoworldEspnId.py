import pandas as pd
import numpy as np
import config as cfg

espnDF = pd.read_csv('csv/espn.csv')
rotoDF = pd.read_csv('csv/rotoworld_edit.csv')

print(espnDF.team.unique())
print(rotoDF.team.unique())

rw_to_espn  = {v:k for k,v in cfg.espn_to_rw.items()}
print(rw_to_espn)
rotoDF['team'].replace(rw_to_espn, inplace=True)

print(rotoDF.shape)

for pos, rank in cfg.rw_drop.items():
    rotoDF.drop(rotoDF[(rotoDF['position'].str.contains(pos)) & (rotoDF['rank'] >= rank)].index, inplace=True)
print(rotoDF.shape)
# print(rotoDF.team.unique())
s = pd.merge(rotoDF, espnDF, how='left', on=['name', 'team'])
print(s[pd.isnull(s.id)][['name', 'team', 'position_x', 'rank']])

missing = s[pd.isnull(s.id)]
missing.to_csv('csv/rw_missing.csv', index=False)

s.to_csv('csv/rotoworld_espn_id_unique.csv', index=False)
# print(rookieDF['position'].unique())
# s = pd.merge(rookieDF, espnDF, how='left', on=['name'])
# print(s.shape)


# only save to rookie_id.csv when ready
# s.to_csv('csv/rookie_id.csv', index=False)
