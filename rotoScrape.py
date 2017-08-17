import requests
import pandas as pd
import config as cfg
from bs4 import BeautifulSoup

host = 'http://rotoworld.com'
depth_url = '/teams/depth-charts/nfl.aspx'
    
all_teams = []
all_players = []
set_players = set()


for divisions in cfg.rotoworld_divisions:
    print(divisions)
    body = cfg.rotoworld_raw_data
    body['ctl00$cp1$ddlDivisions']=divisions
    if divisions == 'AE':
        body = {}
    # print(body)
    # print(cfg.rotoworld_raw_data.format(divisions))
    r = requests.post(host+depth_url, data=body)
    soup = BeautifulSoup(r.text, 'lxml')
    a = soup.find('table', class_='depthtable').find('tr').find_all('th')
    teams = [team.a.find(text=True, recursive=False) for team in a]        
    pos = ''
    for k,v in enumerate(teams):
        print('working on team'+str(k+1)+': '+v)
        a = soup.find('table', id='cp1_tblTeam'+str(k+1))
        tr = a.find_all('tr')
        rank = 1
        for player in tr:
            x = player.find_all('td')[0].find(text=True)
            if x: 
                pos = x
                rank = 1
            # print(pos)
            if pos in cfg.rw_ignore_position:
                continue
            # print(x)
            y = player.find_all('td')[1].a.find(text=True)
            href = player.find_all('td')[1].a['href']
            # print(y)
            # if y not in set_players and rank <= 3:
            all_players.append({'name': y, 'rank': rank, 'position': pos, 'team': v, 'href': host+href})
            set_players.add(y)
            rank += 1
    all_teams.extend(teams)
    print(teams)
    print(len(list(set_players)))
    print(len(all_players))
print(all_teams)
    
    
print(len(list(set_players)))
# print(list(all_players))
# df = pd.DataFrame.from_records(list(all_players), columns=['player'])
# df = pd.DataFrame({'name': list(set_players)})
df = pd.DataFrame.from_records(all_players)
print(df.shape)
print(df.dtypes)
df.to_csv('csv/rotoworld_raw.csv', index=False)
