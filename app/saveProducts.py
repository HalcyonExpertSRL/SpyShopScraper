import htmlget
from bs4 import BeautifulSoup

class getProduct():
    def getProductInfo(self, URL):
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

    def getProductID(self, URL):
        extracted_content = self.getProductInfo(URL)
        list = []
        for item in extracted_content:
            if "id" in item:
                list.append(item)
        return list[0]
