import pandas as pd
import numpy as np

u = pd.read_csv('csv/rotoworld_espn_id_unique.csv')
roster = pd.read_csv('csv/roster.csv')
rookies = pd.read_csv('csv/rookie_id.csv')

t = pd.merge(u, roster, how='left', on=['id'])

x = t.loc[:, ~t.columns.str.contains('^Unnamed')]
x['status'] = np.NaN
rook_id = list(rookies.id)
x.loc[x.id.isin(rook_id), 'status'] = 'Rookie'
x.loc[(~pd.isnull(x.owner)) & (x.status.str != 'Rookie') & (x.end == 2016), 'status'] = 'RFA'
x.loc[(~pd.isnull(x.owner)) & (pd.isnull(x.status)) & (x.end > 2016), 'status'] = 'Own'
x.loc[(x.owner == 'Syed/Terence') & (x.status == 'Own'), 'status'] = 'OurOwn'
x.loc[(x.owner == 'Syed/Terence') & (x.status == 'RFA'), 'status'] = 'OurRFA'
x.loc[pd.isnull(x.status), 'status'] = 'FA'

x.to_csv('csv/final_depth.csv',index=False)
