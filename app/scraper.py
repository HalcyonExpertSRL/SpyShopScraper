import calculate
import saveProducts
import saveCSV
import htmlget
URL = "https://www.spy-shop.ro"

'''
products = saveProducts.getProduct()
csv = saveCSV.CSV()

#print(htmlText)

x = csv.checkAttr(URL)
csv.mergeLines()

isntance =  getUrls.Urls()

x = isntance.getUrls(URL)
print(x) 
'''

requestInstance = htmlget.Request()

requestInstanceCSV = saveCSV.CSV()

listUrls = requestInstance.getUrls(URL)

for item in listUrls:
    requestInstanceCSV.checkAttr(item)