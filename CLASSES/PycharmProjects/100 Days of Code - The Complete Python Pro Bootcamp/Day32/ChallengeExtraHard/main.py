##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas
import os

#Function to send e-mail
def send_email(content, email):
    my_email = "joseph.siwinski.2025@gmail.com"
    password = os.environ.get('GMAIL_2ND_PASSWORD')
    print(f"password: {password}")
    port = 465  # For SSL

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()☎️
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Anniversary\n\n{content}")

# 1. Update the anniversary.csv ✅ done

# 2. Check if today matches an anniversary in the anniversary.csv
now = dt.datetime.now()
date_now = now.day
month_now = now.month
anniversary_DataFrame = pandas.read_csv("anniversary.csv")

for data in anniversary_DataFrame.iterrows():
    name=data[1].values[0]
    email=data[1].values[1]
    year=data[1].values[2]
    month=data[1].values[3]
    day=data[1].values[4]
    # 3. If step 2 is true, pick a random letter from letter templates
    #    and replace the [NAME] with the person's actual name from anniversary.csv
    if date_now == day and month_now == month:
        print(f"About to send random letter to {name} at email: {email}")
        ran_number = random.randint(1, 3)
        file_name = f"letter_templates/letter_{ran_number}.txt"
        print(file_name)
        with open(file_name) as f2:
            letter_text = f2.read().replace("[NAME]", name)
        # 4. Send the letter generated in step 3 to that person's email address.
        send_email(letter_text,email)









