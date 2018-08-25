import requests
import pandas as pd
import config as cfg

url = 'https://spreadsheets.google.com/feeds/list/1nas3AqWZtCu_UZIV77Jgxd9oriF1NQjzSjFWW86eong/2/public/full?alt=json'
r = requests.get(url)
year = 2018
j = r.json()

df = pd.DataFrame()

print(cfg.keys)
for entry in j['feed']['entry']:
    k = [key[4:] for key in cfg.keys]
    v = [entry[key]['$t'] for key in cfg.keys]
    # v['salary'] = v['salary'].replace('$','')
    # print(dict(zip(k,v)))
        # print key[4:]
    row = pd.DataFrame([dict(zip(k,v))])
    # print(row)
    df = df.append(row)

df = df.reset_index(drop=True)
df['salary'] = df['salary'].str.replace('$','')
df.to_csv('csv/roster.csv', index=False)
print(df.shape)
print(df.dtypes)
# print(df.salary.sum())
df[['salary','end']] = df[['salary','end']].apply(pd.to_numeric)
df.sort_values(['end', 'position'])
print(df[(df.id == '15683')])
print(df[(df.owner.str.contains('|'.join(['Sy']), na=False))])
print(df[(df.owner.str.contains('|'.join(['Sy']), na=False)) & (df.end >= year) & (df.end <= (year+1))])

# .salary.sum())
# print(len(j['feed']['entry']))
# s = pd.merge(rookieDF, espnDF, how='left', on=['name'])
# s.drop(s[s.position_x.isin(['T','G','LS','OT','C','OG','OL'])].index, inplace=True)
# s[pd.isnull(s.id)][['overall','team_x','name','id','position_x']]
    
