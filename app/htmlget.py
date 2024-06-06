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
                url = a['href']
                urls.append(url)
        return urls

    def getUrlsAltPages(self, URL):
        urls = self.getUrls(URL)
        calc = calculate.Paginas()
        for page in urls:
            try:
                product_number = calc.getProductNumber(page)
                print(f"Product number: {product_number}")
                if product_number is not None:
                    page_count = int(product_number / 80)
                    if page_count > 0:
                        for i in range(2, page_count + 1):
                            urls.append(page + f"?p={i}")
            except Exception as e:
                print(f"Error occurred while processing page: {page}")
                print(f"Error message: {str(e)}")
