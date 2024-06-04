import saveProducts
import pandas as pd

class CSV():
    def checkAttr(self, URL):
        requestInstance = saveProducts.getProduct()
        lista = requestInstance.getProductAttr(URL)
        for item in lista:
            for item2 in item:
                with open('test/csv', 'a') as file:
                    file.write(item2 + '\n')