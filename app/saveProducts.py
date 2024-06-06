import htmlget
from bs4 import BeautifulSoup
import csv
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
    
    def clean_product_data(self, URL):
        cleaned_data = []
        product_data = self.getProductList(URL)

        for product in product_data:
            product_dict = {}
            for line in product.split(","):
                if "'id':" in line:
                    product_dict['id'] = line.split(":")[1].strip().strip("'").strip()
                elif "'name':" in line:
                    name_parts = line.split(":")[1:]
                    product_dict['name'] = ":".join(name_parts).strip().strip("'").strip()
                elif "'price':" in line:
                    product_dict['price'] = line.split(":")[1].strip().strip("'").strip()
            if 'id' in product_dict and 'name' in product_dict and 'price' in product_dict:
                cleaned_data.append(product_dict)
        return cleaned_data
    
    def save_to_csv(self, cleaned_data, filename):
        keys = cleaned_data[0].keys()
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(cleaned_data)



