import htmlget
from bs4 import BeautifulSoup
import json
class getProduct():
    def getProductBulk(self, URL):
        requestInstance = htmlget.Request()
        htmlText = requestInstance.url(URL)

        soup = BeautifulSoup(htmlText, 'html.parser')
        script_tag = soup.find('script', text=lambda t: t and 'window.CategoryFilteredProducts.push' in t)

        if script_tag:
            content = script_tag.string
            start_index = content.index("(") + 1
            end_index = content.rindex(")")
            extracted_content = content[start_index:end_index]
            extracted_content = str(extracted_content)
            extracted_content = list(extracted_content.split("window.CategoryFilteredProducts.push"))
            return extracted_content
        else:
            return None

    def getProductList(self, URL):
        extracted_content = self.getProductBulk(URL)
        list = []
        for item in extracted_content:
            if "id" in item:
                list.append(item)
        return list[0]

    def getProductAttr(self, URL):
        lista = self.getProductList(URL)
        lista = str(lista)
        start_index = lista.index("'id'") + 1
        end_index = lista.rindex("'brand'")
        extractedList = lista[start_index:end_index]
        extractedList = list(extractedList.split("\n"))
        for x in extractedList:
            print(x)