import yagmail
import pandas
from news import Newsfeed
import datetime


df = pandas.read_excel('people.xlsx')
user = 'tester123jkjk123@gmail.com'
password = 'hlnwuhhlptnguodm'

today = datetime.datetime.now().strftime('%Y-%m-%d')
initial = datetime.datetime.now() - datetime.timedelta(days=1)
initial = initial.strftime('%Y-%m-%d')

for index, row in df.iterrows():
    newsfeed = Newsfeed(row['interest'], initial, today)
    email = yagmail.SMTP(user, password)
    email.send(to=row['email'],
               subject=f"Your {row['interest']} newsfeed for today",
               contents=f"Hi {row['name']},\n Your newsfeed below:\n {newsfeed.get_feed()} \n Love,\nBecky")
