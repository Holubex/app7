import yagmail
import pandas
from news import NewsFeed

df = pandas.read_excel('people.xlsx')
for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], from_date='2024-03-09', to_date='2024-03-10')
    email = yagmail.SMTP(user='holubek.kubo@gmail.com', password='xflcqaittnjbnhup')
    email.send(to=row['email'],
               subject=f'Your {row['interest']} news for today!',
               contents=f"Hi {row['name']} \n See what's on about {row['interest']} today.\n"
                        f"{news_feed.get()}",
               attachments='requirements.txt'
            )