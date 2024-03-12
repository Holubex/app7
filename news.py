import requests


class NewsFeed:
    """
    Representing multiple news titles and links as a single string.
    """

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "ce0ae42b24e9451794188ce5c7d5e3a1"

    def __init__(self, interest: str, from_date: str, to_date: str, language="en"):
        self.language = language
        self.to_date = to_date
        self.from_date = from_date
        self.interest = interest

    def get(self):
        url = self._build_url()
        articles = self._get_articles(url)

        email_body = ""

        for article in articles:
            email_body = email_body + article["title"] + "\n" + article["url"] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content["articles"]
        return articles

    def _build_url(self):
        url = (
            f"{self.base_url}"
            f"qInTitle={self.interest}&"
            f"from={self.from_date}&"
            f"language={self.language}&"
            f"to={self.to_date}&"
            f"apiKey={self.api_key}"
        )
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(
        interest="nasa", from_date="2024-03-10", to_date="2024-03-12", language="en"
    )
    print(news_feed.get())
