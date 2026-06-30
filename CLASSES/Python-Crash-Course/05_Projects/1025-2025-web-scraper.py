import requests
url = "https://tjsiwinski.com"
url = "https://text.npr.org"
response = requests.get(url)
html_content = response.text
#print(html_content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content,'html.parser')
paragraphs = soup.find_all('p')

for p in paragraphs:
    print(p.get_text())