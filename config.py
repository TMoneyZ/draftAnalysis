#!/usr/bin/env python
keys = [
    'gsx$id',
    'gsx$owner',
    'gsx$name',
    'gsx$position',
    'gsx$start',
    'gsx$end',
    'gsx$salary'
]

rotoworld_divisions = ['AE','AN','AS','AW','NE','NN','NS','NW']

# rotoworld_raw_data = '__EVENTTARGET=ctl00%24cp1%24ddlDivisions&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKMTY5MDM3Mjg4MQ9kFgJmD2QWBAIBD2QWDAIKDxYCHgRUZXh0BVA8bGluayByZWw9ImNhbm9uaWNhbCIgaHJlZj0iaHR0cDovL3JvdG93b3JsZC5jb20vdGVhbXMvZGVwdGgtY2hhcnRzL25mbC5hc3B4IiAvPmQCCw8WAh8ABVA8bGluayByZWw9ImNhbm9uaWNhbCIgaHJlZj0iaHR0cDovL3JvdG93b3JsZC5jb20vdGVhbXMvZGVwdGgtY2hhcnRzL25mbC5hc3B4IiAvPmQCDA8WAh8ABVA8bGluayByZWw9ImNhbm9uaWNhbCIgaHJlZj0iaHR0cDovL3JvdG93b3JsZC5jb20vdGVhbXMvZGVwdGgtY2hhcnRzL25mbC5hc3B4IiAvPmQCIA8WAh8ABWI8c2NyaXB0IGxhbmd1YWdlPSdqYXZhc2NyaXB0JyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnIHNyYz0nL3psaWJzL2ZseW91dG5hdl92MDkwNDIwMTMuanMnPjwvc2NyaXB0PmQCIQ8WAh8ABWI8c2NyaXB0IGxhbmd1YWdlPSdqYXZhc2NyaXB0JyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnIHNyYz0nL3psaWJzL2ZseW91dG5hdl92MDkwNDIwMTMuanMnPjwvc2NyaXB0PmQCIg8WAh8ABWI8c2NyaXB0IGxhbmd1YWdlPSdqYXZhc2NyaXB0JyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnIHNyYz0nL3psaWJzL2ZseW91dG5hdl92MDkwNDIwMTMuanMnPjwvc2NyaXB0PmQCAw9kFgICAw9kFgQCAw9kFgQCAw8QZGQWAQIBZAILD2QWAmYPZBYIZg8PZBYCHgVzdHlsZQUYYmFja2dyb3VuZC1jb2xvcjojMzExOTZCFgJmDw8WBB4LTmF2aWdhdGVVcmwFHy90ZWFtcy9uZmwvYmFsL2JhbHRpbW9yZS1yYXZlbnMfAAUQQmFsdGltb3JlIFJhdmVuc2RkAgEPD2QWAh8BBRhiYWNrZ3JvdW5kLWNvbG9yOiMwMDAwMDAWAmYPDxYEHwIFIS90ZWFtcy9uZmwvY2luL2NpbmNpbm5hdGktYmVuZ2Fscx8ABRJDaW5jaW5uYXRpIEJlbmdhbHNkZAICDw9kFgIfAQUYYmFja2dyb3VuZC1jb2xvcjojZmMzZTFkFgJmDw8WBB8CBR8vdGVhbXMvbmZsL2NsZS9jbGV2ZWxhbmQtYnJvd25zHwAFEENsZXZlbGFuZCBCcm93bnNkZAIDDw9kFgIfAQUYYmFja2dyb3VuZC1jb2xvcjojMDAwMDAwFgJmDw8WBB8CBSIvdGVhbXMvbmZsL3BpdC9waXR0c2J1cmdoLXN0ZWVsZXJzHwAFE1BpdHRzYnVyZ2ggU3RlZWxlcnNkZAIFD2QWAgIDD2QWBgIBDxYCHwAFDU5GTCBIZWFkbGluZXNkAgIPDxYCHwIFJH4vaGVhZGxpbmVzL25mbC8wL0Zvb3RiYWxsLWhlYWRsaW5lc2RkAgQPD2QPEBYBZhYBFgIeDlBhcmFtZXRlclZhbHVlBQNuZmwWAWZkZGQJWxfv%2FR2PKQlrve4GCzEHoesd4Q%3D%3D&__VIEWSTATEGENERATOR=69A1B4A8&__EVENTVALIDATION=%2FwEdABG1un3jghljDe0P9bcGbCDK%2FO4ixjo7sCeqv3CW2GXy1aZpqYyq%2BCJ6AZZd14rJe12NaG8eZRdz6mjYA50YCFxpk%2FH21IBSVrSQ9TOeHKqk8%2FXdSTOl7foNNC4vnav6mRJA0xr6ESRH378GIXdIEsf%2BVhRyzBMsGg0Pv8sD1FTPhvKvCs%2BIF%2FTvyqx2qQjPshSp9rXuOKbZSQfG5lW7Fwza5PAEFNW7BFpNbrPYBEktgAqUrodr2wRLWfpNQr2E89RkK0vRPbOw9P42vTGnrglcDQ4N%2FSTj7opKv%2FkXJdidbqurldSadafCBLaPrmIizX4dEzA0wAN3aCaWVKVl9e3fb5qhBA7jMObF0TTanxQ%2BP%2BWf3HOahrkyA9YHBrN9Bq6FdBIG&ctl00%24siteheader%24tbHeaderSearchBox=LAST+NAME%2C+FIRST+NAME&ctl00%24siteheader%24hidpage=&ctl00%24cp1%24ddlDivisions={0}&ctl00%24cp1%24headlinesNFL%24hidHeadlineSport=nfl'

rw_ignore_position = ['LT','LG','C','RG','RT','FB','3RB','GLB']

rotoworld_raw_data = {
    '__EVENTTARGET':'ctl00$cp1$ddlDivisions',
    '__VIEWSTATE':'/wEPDwUKMTY5MDM3Mjg4MQ9kFgJmD2QWBAIBD2QWBAIKDxYCHgRUZXh0BVA8bGluayByZWw9ImNhbm9uaWNhbCIgaHJlZj0iaHR0cDovL3JvdG93b3JsZC5jb20vdGVhbXMvZGVwdGgtY2hhcnRzL25mbC5hc3B4IiAvPmQCIA8WAh8ABWI8c2NyaXB0IGxhbmd1YWdlPSdqYXZhc2NyaXB0JyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnIHNyYz0nL3psaWJzL2ZseW91dG5hdl92MDkwNDIwMTMuanMnPjwvc2NyaXB0PmQCAw9kFgICAw9kFgQCAw9kFgQCAw8QZGQWAWZkAgsPZBYCZg9kFghmDw9kFgIeBXN0eWxlBRhiYWNrZ3JvdW5kLWNvbG9yOiMxOTRCOEMWAmYPDxYEHgtOYXZpZ2F0ZVVybAUcL3RlYW1zL25mbC9idWYvYnVmZmFsby1iaWxscx8ABQ1CdWZmYWxvIEJpbGxzZGQCAQ8PZBYCHwEFGGJhY2tncm91bmQtY29sb3I6IzAwNzg4MxYCZg8PFgQfAgUdL3RlYW1zL25mbC9taWEvbWlhbWktZG9scGhpbnMfAAUOTWlhbWkgRG9scGhpbnNkZAICDw9kFgIfAQUYYmFja2dyb3VuZC1jb2xvcjojMjQzRTgyFgJmDw8WBB8CBSIvdGVhbXMvbmZsL25lL25ldy1lbmdsYW5kLXBhdHJpb3RzHwAFFE5ldyBFbmdsYW5kIFBhdHJpb3RzZGQCAw8PZBYCHwEFGGJhY2tncm91bmQtY29sb3I6IzE2NDUyRBYCZg8PFgQfAgUcL3RlYW1zL25mbC9ueWovbmV3LXlvcmstamV0cx8ABQ1OZXcgWW9yayBKZXRzZGQCBQ9kFgICAw9kFgYCAQ8WAh8ABQ1ORkwgSGVhZGxpbmVzZAICDw8WAh8CBSR+L2hlYWRsaW5lcy9uZmwvMC9Gb290YmFsbC1oZWFkbGluZXNkZAIEDw9kDxAWAWYWARYCHg5QYXJhbWV0ZXJWYWx1ZQUDbmZsFgFmZGRkYo+/S3cgkNSclstVGG7+YAer2hQ=',
    '__VIEWSTATEGENERATOR':'69A1B4A8',
    '__EVENTVALIDATION':'/wEdABFXafMpC2rT7FB49rEwbRNG/O4ixjo7sCeqv3CW2GXy1aZpqYyq+CJ6AZZd14rJe12NaG8eZRdz6mjYA50YCFxpk/H21IBSVrSQ9TOeHKqk8/XdSTOl7foNNC4vnav6mRJA0xr6ESRH378GIXdIEsf+VhRyzBMsGg0Pv8sD1FTPhvKvCs+IF/Tvyqx2qQjPshSp9rXuOKbZSQfG5lW7Fwza5PAEFNW7BFpNbrPYBEktgAqUrodr2wRLWfpNQr2E89RkK0vRPbOw9P42vTGnrglcDQ4N/STj7opKv/kXJdidbqurldSadafCBLaPrmIizX4dEzA0wAN3aCaWVKVl9e3fb5qhBA7jMObF0TTanxQ+P21RkzPxa8CGTXYHa2Q7mJZcRTpi',
    'ctl00$cp1$headlinesNFL$hidHeadlineSport':'nfl'
}

owners = ['Brett/Luke', 'John/Zach', 'Koci/Mueller', 'Patrick', 'Syed/Terence', 'James', 'Daniel', 'Schex/Jeff', 'Quinn', 'Trevor', 'Mitch', 'Keyon']

espn_to_rw = {'Jax': 'Jacksonville Jaguars', 'Min': 'Minnesota Vikings', 'Mia': 'Miami Dolphins', 'Chi': 'Chicago Bears', 'Oak': 'Oakland Raiders', 'NYJ': 'New York Jets', 'Hou': 'Houston Texans', 'NYG': 'New York Giants', 'Phi': 'Philadelphia Eagles', 'NO': 'New Orleans Saints', 'Dal': 'Dallas Cowboys', 'NE': 'New England Patriots', 'Cle': 'Cleveland Browns', 'Buf': 'Buffalo Bills', 'Wsh': 'Washington Redskins', 'Atl': 'Atlanta Falcons', 'Det': 'Detroit Lions', 'Cin': 'Cincinnati Bengals', 'GB': 'Green Bay Packers', 'Den': 'Denver Broncos', 'Bal': 'Baltimore Ravens', 'Car': 'Carolina Panthers', 'KC': 'Kansas City Chiefs', 'Ten': 'Tennessee Titans', 'TB': 'Tampa Bay Buccaneers', 'LAC': 'Los Angeles Chargers', 'Sea': 'Seattle Seahawks', 'Ind': 'Indianapolis Colts', 'Ari': 'Arizona Cardinals', 'Pit': 'Pittsburgh Steelers', 'SF': 'San Francisco 49ers', 'LAR': 'Los Angeles Rams'}

rw_drop = {
    'QB': 3,
    'RB': 5,
    'WR': 4,
    'TE': 3,
    'K': 2
}
# t = pd.merge(u, roster, how='left', on=['id'])
# x = t.loc[:, ~t.columns.str.contains('^Unnamed')]
# import numpy as np
# x['status'] = np.NaN
# rook_id = list(rookies.id)
# x.loc[x.id.isin(rook_id), 'status'] = 'Rookie'
# x.loc[(~pd.isnull(x.owner)) & (x.status.str != 'Rookie') & (x.end == 2016), 'status'] = 'RFA'
# x.loc[(~pd.isnull(x.owner)) & (pd.isnull(x.status)) & (x.end > 2016), 'status'] = 'Own'
# x.loc[(x.owner == 'Syed/Terence') & (x.status == 'Own'), 'status'] = 'OurOwn'
# x.loc[(x.owner == 'Syed/Terence') & (x.status == 'RFA'), 'status'] = 'OurRFA'
