from bs4 import BeautifulSoup
import requests

# Before you scrape
# -- See https://news.ycombinator.com/robots.txt :: [Crawl-delay]

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title) - shows web page title

#---------------------------------------------------------
article= soup.find(class_="titleline")
print(article)
#<span class="titleline"><a href="https://donotnotify.com/">Show HN: DoNotNotify – log and intelligently block notifications on Android</a><span class="sitebit comhead"> ...

article_tag = article.find(name="a")
print(article_tag)
#<a href="https://donotnotify.com/">Show HN: DoNotNotify – log and intelligently block notifications on Android</a>

article_text = article_tag.get_text()
print(article_text)
#Show HN: DoNotNotify – log and intelligently block notifications on Android

article_link =article_tag.get("href")
print(article_link)
# https://github.com/Adversis/tailsnitch

article_upvote = soup.find(name="span", class_="score")
#<span class="score" id="score_46503554">24 points</span>
print(article_upvote.get_text())
#24  points
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
# List Comprehension
# -- '129 points' change to 129

print(article_texts)
print(article_links)
print(article_upvotes)

# At this point we have three lists: text,link,upvotes
# -- but which article is most popular [most upvotes]
max_upvotes= max(article_upvotes)
print(f"max upvotes:{max_upvotes}")

for count in range(0,len(article_upvotes) -1):
    if article_upvotes[count] == max_upvotes:
        break
print(count)
print(article_texts[count],article_links[count],max_upvotes)
# TJ:Solution: The above ^ works to find most popular article

#-----------------------------------------
largest_index = article_upvotes.index(max_upvotes)
print(article_texts[largest_index], article_links[largest_index], max_upvotes)
# UDEMY:Solution: above ^ cleaner