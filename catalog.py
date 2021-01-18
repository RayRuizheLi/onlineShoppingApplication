from product import Product

class Catalog:
    def __init__(self):
        self.__items = 0
        self.__products = dict()

    # name: string
    def getProduct(self, name):
        return self.__products[name];

    def getCatalogSize(self):
        return self.__products.len()

    # prod: product
    def addProduct(self, prod):
        self.__products[prod.getName()] = prod
    
    # name: string
    def removeProduct(self, name):
        del self.__products[name]

# Test catalog
cat = Catalog()
item = Product("test1", 1.1, 2)
print(item.getName())
cat.addProduct(item)
test = cat.getProduct("test1")
print(test.getName())