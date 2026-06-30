#0115-2026
# - goal scrape news , open thre most popular stories by upvotes
from bs4 import BeautifulSoup
import requests
import webbrowser

# Before you scrape
# -- See https://news.ycombinator.com/robots.txt :: [Crawl-delay]

def main_function():
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

    print("*" * 50)
    print("*" * 50)

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
                print(f"Title: {article_texts[count]},Link: {article_links[count]},Upvotes: {max_upvotes}")
                url=article_links[count]
                webbrowser.open(url)
                
                # now we remove current article from each list so we can get the next most popular article
                article_texts.pop(count)
                article_links.pop(count)
                article_upvotes.pop(count)
                break
    
if __name__ == "__main__":
    main_function()