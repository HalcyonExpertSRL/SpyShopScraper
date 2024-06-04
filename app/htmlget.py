import requests
from bs4 import BeautifulSoup

class Request:
    def url (self, url):
        text = requests.get(url)
        text  = text.text
        return text

    def getUrls(self, URL):
        htmlText = self.url(URL)
        soup = BeautifulSoup(htmlText, 'html.parser') 
        urls = []
        for a in soup.find_all('a', href=True):
            if a['href'].startswith('https://www.spy-shop.ro/'):
                urls.append(a['href'])
        return urls
