import calculate
import saveProducts
import saveCSV
import htmlget
URL = "https://www.spy-shop.ro/supraveghere-video/sisteme-supraveghere-video.html?limit=80"

def menu():
    print("Menu:")
    print("1. Save to CSv")
    print("2. Save Products")
    print("3. Order CSV")
    print("4. Exit")

    choose = "3"
    if choose == "1":
        requestInstanceCSV = htmlget.Request()
        csv = saveCSV.CSV()
        listUrls = requestInstanceCSV.getUrls(URL)
        for item in listUrls:
            csv.checkAttr(item)

    elif choose == "2":
        saveProducts.getProduct()
    elif choose == "3":
        csv = saveCSV.CSV()
        csv.mergeLines()
    elif choose == "4":
        print("Exiting...")
        return
    else:
        print("Invalid choose. Please try again.")



def art(URL):
    prd = saveProducts.getProduct()
    products = prd.getProductAttr(URL)
    for product in products:
        print(product)
        print("---------------------------------------------------------")

art(URL)