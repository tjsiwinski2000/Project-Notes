#base_fen =  "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
#base_fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"

from sys import argv
import json 
def sanitize_fen(fen: str) -> str:
    parts = fen.split(" ")
    parts[3] = "-"  # zero out en passant square
    return " ".join(parts)
    
base_fen =  argv[1:]
base_fen = str(base_fen).replace("'","")
print(f"argument passed {base_fen}")

base_fen = sanitize_fen(base_fen)
parameters = {
  "fen": base_fen
}
print(parameters)
#parameters["moves"] =["a7b6"]
print("-"*10)
print(parameters)

import requests
chess_url = "https://chess-api.com/v1"


response = requests.post(url=chess_url, json=parameters)
response.raise_for_status()
data = response.json()
#Next_move=data["continuationArr"][0]
#print(data["continuationArr"])
print(data)

