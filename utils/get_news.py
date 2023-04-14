import json
import requests
import xmltodict


def get_news():
    news_list = []
    result = requests.get("https://lenta.ru/rss/")
    if result.status_code == 200:
        o = xmltodict.parse(result.text)
        json.dumps(o)
        if o.get('rss').get('channel').get('item') is not None:
            for i in range(0, 2):
                news = o['rss']['channel']['item'][i]
                news_list.append({
                    'photo_url': news.get('enclosure').get('@url'),
                    'title': news['title'],
                    'description': news['description'],
                    'author': news['author'],
                    'pubDate': news['pubDate'],
                    'link': news['link']
                })
    return news_list





