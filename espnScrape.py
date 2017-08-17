import requests
import pandas as pd
from bs4 import BeautifulSoup

leagueId = 1225885
seasonId = 2017
startIndex = 0
inc = 50
n = 0

url = 'http://games.espn.com/ffl/freeagency?leagueId=122885&seasonId=2017&context=freeagency&view=overview&version=projections&avail=-1&startIndex={0}'

def scape(index):
    r = requests.get(url.format(index))
    soup = BeautifulSoup(r.text, 'lxml')
    return soup.find_all('td', class_='playertablePlayerName')
    

lst = []
index = startIndex
rows = scape(index)
# while rows and n == 0:
while rows:
    # rows = soup.find_all("tr", class_="pncPlayerRow")
    print(index)
    print(len(rows))

    for row in rows:
        # playertablePlayerName = row.find_all('td', class_='playertablePlayerName')[0]['a']
        # print(playertablePlayerName)
        # print(row)
        # print(row.a.get('playerid'))
        playerid = row.a.get('playerid')
        # print(row.a.find(text=True, recursive=False))
        playername = row.a.find(text=True, recursive=False)
        tdAttributes = row.find(text=True, recursive=False).replace(u'\xa0', ' ').split(' ', 2)
        team = tdAttributes[1]
        pos = tdAttributes[2].replace(' ','').split(',')
        lst.append({'name': playername, 'id': playerid, 'team': team, 'position': pos})
        # print(tdAttributes)
        # print(team)
        # print(pos)
    index += inc
    # n+=1
    rows = scape(index)
    
# print(lst)
df = pd.DataFrame(lst)
print(df.shape)
print(df.dtypes)
df.to_csv('csv/espn.csv', index=False)
