#0121-2026 challenge of the morning
# -- get top  men and women in tennis
# -- experimented with colored text
# -- print(f"{color}{player['place'].rjust(2)}.{player['player'].ljust(30)} {player ['country'].ljust(20)} ranking_points: {player['points']} {RESET}")
# .rjust(2) - right justify e.g. ' 1' 
# .ljust(30) -left justify e.g. 'Rafel Nadal...............' 
# {color} temp var , set depending even  or ordd {RESET} - removes color set  
#
# 0206-2026 free trial has run out ;-( 
# 
import requests
import json 
key='7d425543747e310d1672ffdbfff92f58ec355f1a8df7cc0d4d1aab673f4e376c'

# color printing 
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m' # Resets the color/style to default

url_atp='https://api.api-tennis.com/tennis/?method=get_standings&event_type=ATP&APIkey='
url_wta='https://api.api-tennis.com/tennis/?method=get_standings&event_type=WTA&APIkey='

complete_url = url_atp + key
data = requests.get(complete_url).json()
players = data['result']
print(players)
for player in players:
    if int(player['place']) % 2 == 0:
        color = GREEN
    else:
        color = WHITE
    print(f"{color}{player['place'].rjust(2)}.{player['player'].ljust(30)} {player ['country'].ljust(20)} ranking_points: {player['points']} {RESET}")
    if int(player['place']) >29:
        break
    
complete_url = url_wta + key
data = requests.get(complete_url).json()
BLUE = '\033[34m'
players = data['result']
for player in players:
    if int(player['place']) % 2 == 0:
        color = CYAN
    else:
        color = WHITE
    print(f"{color} {player['place'].rjust(2)}.{player['player'].ljust(30)} {player ['country'].ljust(20)} ranking_points: {player['points']} {RESET}")
    if int(player['place']) >30:
        break
    
# BLACK = '\033[30m'
# RED = '\033[31m'
# GREEN = '\033[32m'
# YELLOW = '\033[33m'
# BLUE = '\033[34m'
# MAGENTA = '\033[35m'
# CYAN = '\033[36m'
# WHITE = '\033[37m'
# RESET = '\033[0m' # Resets the color/style to default