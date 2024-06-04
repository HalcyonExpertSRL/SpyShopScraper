import htmlget

URL = "http://www.spyshop.ro"

requestInstance = htmlget.Request()

htmlText = requestInstance.url(URL)

print(htmlText)
