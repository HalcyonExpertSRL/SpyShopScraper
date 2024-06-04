import saveProducts
import pandas as pd

class CSV():
    def checkAttr(self, URL):
        requestInstance = saveProducts.getProduct()
        lista = requestInstance.getProductAttr(URL)
        for item in lista:
            for item2 in item:
                print(f"{item2}XD")
                with open('test.csv', 'a') as file:
                    if 'id' in item2 or 'name' in item2 or 'price' in item2:
                        item2 = item2.replace(", ", " ")
                        item2 = item2.replace("                ", "")
                        file.write(f"{item2}\n")
        return "Done"

    def mergeLines(self):
        with open('test.csv', 'r') as file:
            lines = file.readlines()
        merged_lines = [','.join(lines[i:i+4]).replace('\n', '') for i in range(0, len(lines), 4)]
        with open('merged.csv', 'w') as file:
            file.write('\n'.join(merged_lines))
        return "Merged lines and saved to merged.csv"