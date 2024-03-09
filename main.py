# ce0ae42b24e9451794188ce5c7d5e3a1
import requests

class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass

response = requests.get('https://newsapi.org/v2/everything?q=apple&from=2024-03-08&to=2024-03-08&sortBy=popularity&apiKey=ce0ae42b24e9451794188ce5c7d5e3a1')