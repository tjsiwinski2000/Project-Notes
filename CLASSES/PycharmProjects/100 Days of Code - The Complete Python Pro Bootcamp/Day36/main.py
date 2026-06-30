STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
import requests
import os
from datetime import datetime, timedelta


#TODO add API to environment vars:
STOCK_API_KEY=os.environ.get('STOCK_API_KEY')
NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

NEWS_URL = "https://newsapi.org/v2/everything"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "TSLA",
    "apikey" : STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

# Provide key to get KEY we need immediately
data = response.json()['Time Series (Daily)']

# data is : {'2025-12-05': {'1. open': '453.0300', '2. high': '458.8700', '3. low': '451.6600', '4. close': '455.0000', '5. volume': '56427522'}
#              ^ dictionary with each date is a KEY
#
# Convert to LIST using LIST COMPREHENSION
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100
#If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > .03:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_API_KEY
    }
    news_response = requests.get(url=NEWS_URL, params=news_parameters)
    articles = news_response.json()["articles"]

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    # 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    # 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    for story in three_articles:
        print(story['title'])
        print(story['description'])

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles_list = [f"Headline: {item['title']}. \nBrief: {item['description']}" for item in three_articles]
print(formatted_articles_list)

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

