import datetime as dt
import smtplib
import random

MY_EMAIL = input("Enter your Email Address : ")
MY_PASSWD = input("Enter your email's Applications' Password : ")

with open("quotes.txt") as quotes_file:
    quotes_list = quotes_file.readlines()
    print(quotes_list, end="\n\n")
    quote = random.choice(quotes_list)
    print(quote)

now = dt.datetime.now()
day = now.weekday()
hour = now.hour
minute = now.minute

if day == 0 and hour == 9 and minute == 00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"subject:Motivational Letter\n\n{quote}"
                            )

