import htmlget
from bs4 import BeautifulSoup

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
        return list

    def getProductAttr(self, URL):
        lista = self.getProductList(URL)
        extractedList = []
        for item in lista:
            item_str = str(item)
            start_index = item_str.index("'id'") + 1
            end_index = item_str.rindex("'brand'")
            extracted_item = item_str[start_index:end_index]
            extracted_item = list(extracted_item.split("\n"))
            extractedList.append(extracted_item)
        return extractedList