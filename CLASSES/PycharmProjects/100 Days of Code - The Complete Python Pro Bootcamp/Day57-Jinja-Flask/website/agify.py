import requests

def get_message(name):
    response = requests.get(f"https://api.agify.io/?name={name}")

    response.raise_for_status()
    data = response.json()
    #print(response.text)
    return data['age'],str(data['name']).title()

# age, name = get_message('thaddeus')
# print(f'age:{age}\tname: {name}')