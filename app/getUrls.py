import htmlget
from bs4 import BeautifulSoup

class Urls():

    def getUrls(self, URL):
        requestInstance = htmlget.Request()
        htmlText = requestInstance.url(URL)
        soup = BeautifulSoup(htmlText, 'html.parser') 
        href_labels = soup.find_all('a') 
        content_list = [] 
        for label in href_labels: 
            content_list.append(label.text) 
            print(content_list)

