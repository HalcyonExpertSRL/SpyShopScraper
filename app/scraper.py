import calculate
import saveProducts

URL = "https://www.spy-shop.ro/supraveghere-video/sisteme-supraveghere-exterior.html?limit=80"

products = saveProducts.getProduct()
requestInstance = calculate.Paginas()
#htmlText = requestInstance.getPages(URL)

#print(htmlText)

y = requestInstance.getProductNumber(URL)
x = products.getProductID(URL)
print(x)