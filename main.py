import smtplib
import ssl
import datetime as dt
import random
import pandas

MY_EMAIL = "johnedaise@gmail.com"
PASSWORD = "iclvuycjrvtywpbu"


now = dt.datetime.now()

today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}

if today in birthday_dict:
    birthday_row = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_row["name"])

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        # connection.starttls()
        connection.ehlo()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_row["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}")


# now = dt.datetime.now()
# day_of_week = now.weekday()
#
# if day_of_week == 4: # TODO set to 0 for Monday
#     with open("quotes.txt") as file:
#         all_quotes = file.readlines()
#         single_quote = random.choice(all_quotes)
#
#     print(single_quote)
#     with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="jdaise@gmail.com",
#             msg=f"Subject:Monday Motivation\n\n{single_quote}")
#
#     # TODO check the Yahoo details of lesson to allow email send

