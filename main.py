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
      'to=2024-03-01&'\
      'language=en&'\
      'apiKey=ce0ae42b24e9451794188ce5c7d5e3a1'

response = (requests.get(url))
content = response.text
pprint(content)
