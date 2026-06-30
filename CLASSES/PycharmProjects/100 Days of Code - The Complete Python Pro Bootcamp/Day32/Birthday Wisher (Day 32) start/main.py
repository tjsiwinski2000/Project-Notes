import smtplib
import datetime as dt
import random


#1.Open quotes.txt , make list
quote_list = []
with open("quotes.txt") as f1:
    for line in f1:
        quote_list.append(line)

#2.Function to Return Random Quote
def random_quote():
    return(random.choice(quote_list))

#3.Function to Check for Tuesday
def check_for_day():
    now = dt.datetime.now()
    # print(now.weekday())
    if now.weekday()== 1:
        print("Today is Tuesday time to send a quote")

    return True

#4.Function to send e-mail
def send_email(quote):
    my_email = "joseph.siwinski.2025@gmail.com"
    password = "desnmdhnedrokrmp"
    port = 465  # For SSL

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="joseph.siwinski@yahoo.com",
            msg=f"Subject:Motivational Quote\n\n{quote}")


day = check_for_day()

if day:
    today_quote = random_quote()
    print(f"About to send this quote:\n\t{today_quote}")
    send_email(today_quote)


#4. Send random quote from function