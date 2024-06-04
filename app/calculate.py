import htmlget
from bs4 import BeautifulSoup

class Paginas():
    def getPages(self, URL):
        requestInstance = htmlget.Request()
        htmlText = requestInstance.url(URL)
        return htmlText

    def getProductChain(self, URL):
        htmlText = self.getPages(URL)
        soup = BeautifulSoup(htmlText, 'html.parser')
        target_div = soup.find('div', class_='pull-right products-nr')
        return target_div
    
    def getProductNumber(self, target_div):
        for number in target_div.split():
            if number.isdigit():
                return number