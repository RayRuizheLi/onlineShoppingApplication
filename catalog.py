from product import Product

class Catalog:
    def __init__(self):
        self.__items = 0
        self.__products = dict()
        self.initProducts()

    def initProducts(self):
        logins = open("productStore.txt", "r")

        while True:
            name = logins.readline()
            price = logins.readline()
            amount = logins.readline()

            if not name:
                break
            
            name = name.rstrip("\n")
            price = price.rstrip("\n")
            amount = amount.rstrip("\n") 

            prod = Product(name, price, amount)
            self.__products[prod.getName()] = prod

    # name: string
    def getProduct(self, name):
        return self.__products[name];

    def getCatalogSize(self):
        return self.__products.len()

    # prod: product
    def addProduct(self, prod):
        self.__products[prod.getName()] = prod
        f = open("productStore.txt", "a")
        f.write(prod.getName() + "\n")
        f.write(prod.getPrice() + "\n") 
        f.write(prod.getAmount() + "\n") 
        f.close()
    
    # name: string
    def removeProduct(self, name):
        if name not in self.__products:
            print("Product does not exist")
            return 

        with open("productStore.txt", "r") as f:
            lines = f.readlines()
        with open("productStore.txt", "w") as f:
            for line in lines:
                if (line.strip("\n") != self.__products[name].getName() and 
                   line.strip("\n") != self.__products[name].getPrice() and 
                   line.strip("\n") != self.__products[name].getAmount()):
                    f.write(line)
        
        del self.__products[name]

    def listProducts(self):
        for p in self.__products:
            print("name: {}, price: {}, amount: {}".format(self.__products[p].getName(), self.__products[p].getPrice(), self.__products[p].getAmount()))