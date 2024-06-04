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

    def getProductNumber(self, URL):
        target_div = self.getProductChain(URL)
        list = []
        target_div = str(target_div)
        for number in target_div.split():
            try:
                list.append(int(number))
            except ValueError:
                pass
        list = int(list[0])
        return list
    