import requests
import os

NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

NEWS_URL = "https://newsapi.org/v2/everything"

parameters = {
    "q" : "tesla",
    "apikey" : NEWS_API_KEY
}

# 
response = requests.get(url=NEWS_URL, params=parameters)
response.raise_for_status()
data = response.json()

# assign data variable the contents of the "article" key 
data = response.json()['articles']
# print the first three articles
#print(data[:3])
#print  article author, title , url
for article in data[:3]:
    print(f"Author: {article['author']} \n\tTitle:{article['title']} \n\tURL: {article['url']} ")