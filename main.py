# ce0ae42b24e9451794188ce5c7d5e3a1
import requests
from pprint import pprint


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass


url = 'https://newsapi.org/v2/everything?'\
      'qInTitle=meditation&'\
      'from=2024-03-08&'\
      'language=en&'\
      'to=2024-03-01&'\
      'apiKey=ce0ae42b24e9451794188ce5c7d5e3a1'

response = requests.get(url)
content = response.json()
articles = content['articles']


email_body = ''

for article in articles:
    email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

print(email_body)