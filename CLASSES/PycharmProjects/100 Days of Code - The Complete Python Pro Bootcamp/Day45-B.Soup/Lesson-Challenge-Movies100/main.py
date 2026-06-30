from bs4 import BeautifulSoup
import requests

# Before you scrape
# -- See https://news.ycombinator.com/robots.txt :: [Crawl-delay]

# empireonline seems ANTI scraping
# response = requests.get("https://www.empireonline.com/movies/features/best-movies-of-all-time-us/")
# empire_web_page = response.text
# print(empire_web_page)
with open("empireonline.html") as f1:
    soup = BeautifulSoup(f1, "html.parser")

all_movie_tags = soup.find(class_='htmlInsert_html-insert-wrapper__tbN37')

for tag in all_movie_tags:
    num = tag.get_text().split(' ')[0]
    title = tag.get_text().removeprefix(num).removeprefix(" ")
    if title:
        print(f"{num}) {title}")

# article_tag = article.find(name="a")
# print(article_tag)
# # <a href="https://donotnotify.com/">Show HN: DoNotNotify – log and intelligently block notifications on Android</a>
#
# article_text = article_tag.get_text()