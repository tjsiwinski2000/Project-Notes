from bs4 import BeautifulSoup
with open("website.html") as f1:
    contents = f1.read()

# NOTE: must specify parser type [re:https://www.crummy.com/software/BeautifulSoup/bs4/doc/]
soup = BeautifulSoup(contents,'html.parser')

# NOTE: soup is now a python object
print(soup.prettify())
print(soup.title)           #<title>Angela's Personal Site</title>
print(soup.title.string)    #Angela's Personal Site
print(soup.li)              #Note: finds first only <li>The Complete iOS App Development Bootcamp</li>

#NOTE find_all is DOPE very common use
all_anchor_tags = soup.find_all(name = "a")
for tag in all_anchor_tags:
    print(tag.get("href"))
#NOTE find_all w/o name also works
# ----if no other anchor tags do not have to specify class
quiz1 = soup.find_all("a")
print(quiz1)
#-----------------------------------------------------------
#NOTE looking for => <h1 id="name">Angela Yu</h1>
heading = soup.find(name="h1", id="name")
print(heading)
#-----------------------------------------------------------
#NOTE looking for => <h3 class="heading">Books and Teaching</h3>
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.string)
#-----------------------------------------------------------
#-----------------------------------------------------------
#NOTE select_one() first matching item in a list [p a] = anchor tag in <p>
#      selector is CSS selector actually
company_url = soup.select_one(selector ="p a")
print(company_url)
#-----------------------------------------------------------
#NOTE select on id use #
#      example: <h1 id="name">Angela Yu</h1>
name = soup.select_one(selector="#name")
print(f"#name select: {name}")
#-----------------------------------------------------------
#NOTE find anchor tags in <li>
quiz2=soup.select("li a")
print(quiz2)
#-----------------------------------------------------------
#NOTE select on class add "."
headings = soup.select(".heading")
print(headings)
print("-" *30)
#-----------------------------------------------------------
#NOTE  <input type="text" name="q" maxlength="255" value=""></input>
#      need to return maxlength
#      1. get the tag    2. ".get('value)

input_tag = soup.find("input")
print(f"maxlength:{input_tag.get('maxlength')}")
#-----------------------------------------------------------

# print(type(soup))           #<class 'bs4.BeautifulSoup'>
# print(type(maxlength))      #<class 'bs4.element.Tag'>

#================================================

