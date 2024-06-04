import calculate

URL = "https://www.spy-shop.ro/supraveghere-video/sisteme-supraveghere-exterior.html?limit=80"

requestInstance = calculate.Paginas()
#htmlText = requestInstance.getPages(URL)

#print(htmlText)

y = requestInstance.getProductNumber(URL)

print(y)