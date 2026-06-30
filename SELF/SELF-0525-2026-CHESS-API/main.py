#0525-2026 experiment to call Chess API
# continuationArr key shows expected sequence

import requests
base_fen =  "8/k7/8/8/8/8/7P/K7 w - - 0 1"
parameters = {
  "fen": base_fen
}

chess_url = "https://chess-api.com/v1"

response = requests.post(url=chess_url, json=parameters)
response.raise_for_status()
data = response.json()
next_move=data["continuationArr"][0]