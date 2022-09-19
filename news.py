import requests


class Newsfeed:
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "f63785601fdc4c8cafd9781ea8eb0871"

    def __init__(self, topic, from_date, to_date):
        self.topic = topic
        self.from_date = from_date
        self.to_date = to_date
        self.url = self.make_url()

    def make_url(self):
        return f"{self.base_url}q={self.topic}&from={self.from_date}&to={self.to_date}&" \
               "sortBy=popularity&language=en&" \
               f"apiKey={self.api_key}"

    def get_feed(self):
        response = requests.get(self.url)
        content = response.json()
        articles = content['articles']
        newsfeed = ''
        for article in articles:
            newsfeed += article['title'] + '\n' + \
                        article['source']['name'] + '\n' + \
                        article['publishedAt'] + '\n' + \
                        article['url'] + '\n\n'
        return newsfeed


# himax = Newsfeed('himax', '2022-09-14', '2022-09-18')
# print(himax.get_feed())
