import requests
from bs4 import BeautifulSoup
import calculate

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
                url = a['href'] + '?limit=80'
                urls.append(url)
        return urls

    def getUrlsAltPages(self, URL):
        urls = self.getUrls(URL)
        calc = calculate.Paginas()
        for page in urls:
            try:
                for i in range(0, int((calc.getProductNumber(page)/80 - 1))):
                    urls.append(f"{page}&p={i}")
            except Exception as e:
                print(f"Error occurred while processing page: {page}")
                print(f"Error message: {str(e)}")
        return urls