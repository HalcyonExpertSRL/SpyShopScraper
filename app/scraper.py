import calculate
import saveProducts
import saveCSV
import htmlget
URL = "https://www.spy-shop.ro"

'''
products = saveProducts.getProduct()

#print(htmlText)

x = csv.checkAttr(URL)
csv.mergeLines()

isntance =  getUrls.Urls()

x = isntance.getUrls(URL)
print(x) 

'''
requestInstanceCSV = htmlget.Request()
csv = saveCSV.CSV()


listUrls = requestInstanceCSV.getUrls(URL)

for item in listUrls:
    csv.checkAttr(item)


