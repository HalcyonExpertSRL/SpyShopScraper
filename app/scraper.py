import calculate
import saveProducts
import saveCSV
import htmlget
import getUrls
URL = "https://www.spy-shop.ro"

'''
products = saveProducts.getProduct()
requestInstance = calculate.Paginas()
csv = saveCSV.CSV()
#htmlText = requestInstance.getPages(URL)

#print(htmlText)

x = csv.checkAttr(URL)
csv.mergeLines()
'''
isntance =  getUrls.Urls()

x = isntance.getUrls(URL)
print(x) 
isntance.getUrls(URL)