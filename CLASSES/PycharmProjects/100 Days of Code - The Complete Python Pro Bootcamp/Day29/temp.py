import json

with open("data.json") as f1:
    data = json.load(f1)

game_over = False

while not game_over:
    word = input("enter a website to search")
    if word == "quit":
        game_over = True
    entry = data.get(word)
    if entry == None:
        print("No details for the website exists")
    else:
        print(f'email: {entry["email"]} password: {entry["password"]}')