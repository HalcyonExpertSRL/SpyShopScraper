import calculate
import saveProducts
import saveCSV

URL = "https://www.spy-shop.ro/supraveghere-video/sisteme-supraveghere-exterior.html?limit=80"

products = saveProducts.getProduct()
requestInstance = calculate.Paginas()
csv = saveCSV.CSV()
#htmlText = requestInstance.getPages(URL)

#print(htmlText)

x = csv.checkAttr(URL)
csv.mergeLines()
print(x)