import requests


def get_top_catchers():
    player_list = []
    URL = "http://hummbabybaseball.com/documentaries/the-top-15-mlb-catchers-of-all-time-posey-berra-molina"
    response = requests.get(URL)
    response.raise_for_status()
    html_content = response.text
    for count in range(15,0,-1):
        flag = "<strong>" +str(count) + ". "
        flag_location = html_content.find(flag)
        player_line = html_content[flag_location: flag_location+100]
        #player_line example: <strong>15. Ted Simmons</strong></p><p class="" style="white-space:pre-wrap;">A player who wasn’
        player_line=player_line.removeprefix('<strong>')
        flag_location = player_line.find('</strong>')
        current_player = player_line[:flag_location]
        player_list.append(current_player)
    return(player_list[::-1])