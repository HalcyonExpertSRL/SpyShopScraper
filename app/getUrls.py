import htmlget
from bs4 import BeautifulSoup

class Urls():

    def getUrls(self, URL):
        requestInstance = htmlget.Request()
        htmlText = requestInstance.url(URL)
        soup = BeautifulSoup(htmlText, 'html.parser') 
        urls = []
        for a in soup.find_all('a', href=True):
            if a['href'].startswith('https'):
                urls.append(a['href'])
        return urls
