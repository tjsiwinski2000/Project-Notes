#0203-2026 just an idea to organize daily "runs" into html docs for easy reading
import boto3
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup
import requests

# CONSTANTS color printing 
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m' # Resets the color/style to default

# Provided by AI; simple straight forward to get users on an Account
def list_iam_users():
    # Initialize the IAM client
    iam = boto3.client('iam')

    try:
        # Call the list_users API
        response = iam.list_users()
        
        print("Users found in IAM:")
        for user in response['Users']:
            print(f"{RED}- Username: {user['UserName']} (ID: {user['UserId']}){RESET}")
            
    except ClientError as e:
        print(f"Error accessing AWS: {e}")
# Get tope three articles
def top_three_articles():
    response = requests.get("https://news.ycombinator.com/news")
    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, "html.parser")
    # print(soup.title) - shows web page title

    #---------------------------------------------------------
    # article= soup.find(class_="titleline")
    # article_tag = article.find(name="a")
    # article_text = article_tag.get_text()
    # article_link =article_tag.get("href")

    # article_upvote = soup.find(name="span", class_="score")

    #---------------------------------------------------------
    # GETTING ALL THE ARTICLES
    print("*" * 50)
    articles= soup.find_all(class_="titleline")
    article_texts = []
    article_links = []
    for article in articles:
        article_tag = article.find(name="a")
        if article_tag:
            text = article_tag.get_text()
            article_texts.append(text)
            link = article_tag.get("href")
            article_links.append(link)


    #article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
    # List Comprehension
    # -- in essence a FOR loop to build a list of [score.getText()]
    # -- example '129 points'

    article_upvotes = [int(score.getText().split()[0])for score in soup.find_all(name="span", class_="score")]

    #Open three most popular articles 
    for _ in range(1,4):
        max_upvotes= max(article_upvotes)
        print(f"current max upvotes:{max_upvotes}")

        #find the article that corresponds to *current* max_upvotes 
        for count in range(0,len(article_upvotes) -1):
            if article_upvotes[count] == max_upvotes:
                print(f"Title: {article_texts[count]}, Upvotes: {max_upvotes}")
                temp_link = article_links[count]
                if temp_link[:5] == 'item?':
                    temp_link = 'https://news.ycombinator.com/' + temp_link
                print(f"\tLink:{CYAN}{temp_link}{RESET}")
                url=article_links[count]
                #webbrowser.open(url)
                
                # now we remove current article from each list so we can get the next most popular article
                article_texts.pop(count)
                article_links.pop(count)
                article_upvotes.pop(count)
                break
#print current uses on my account      
list_iam_users()
#print top3 articles
top_three_articles()