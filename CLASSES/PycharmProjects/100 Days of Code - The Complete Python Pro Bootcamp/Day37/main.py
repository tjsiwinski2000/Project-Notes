import requests
from datetime import datetime

USERNAME = "thaddeus"
TOKEN = "fooofofof123adfjladfj"
PIXELA_ENDPOINT ="https://pixe.la/v1/users"
GRAPH_ID= "graph1"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

#Create your user account https://pixe.la/
# response = requests.post(url=PIXELA_ENDPOINT,json= user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config ={
    "id" : "graph1",
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "momiji"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
#Create a graph
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers = headers)
# print(response.text)

today = datetime.now().strftime("%Y%m%d")
print(today)

POST_VALUE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
post_value_dict = {
    "date" : "20251209",
    "quantity" : "6635.0"
}

#Post a value to our graphs
# response = requests.post(url=POST_VALUE_ENDPOINT,json=post_value_dict, headers=headers)
# print(response.text)

# PUT a value (essentially edit)
# ../<username>/graphs/<graphID>/<yyyyMMdd>
edit_date = today
PUT_EDIT_ENDPOINT= f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{edit_date}"
put_value_dict = {
    "quantity" : "100000.0"
}

# response = requests.put(url=PUT_EDIT_ENDPOINT, json=put_value_dict, headers=headers)
# print(response.text)

delete_date = today
DELETE_EDIT_ENDPOINT =  f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date}"
response = requests.delete(url=DELETE_EDIT_ENDPOINT, headers=headers)
print(response.text)