import copy
from catalog import Catalog
from decimal import Decimal

class ShoppingCart:
    # Input: boolean for if shopping cart is for guest

    def __init__(self, isGuest):
        self.__isGuest = isGuest
        self.__catalog = Catalog()
        self.__price = 0
        self.__cart = list()
    
    def browse(self):
        self.__catalog.listProducts()
    
    # Input: name of product and amount 
    def addProduct(self, name, quantity):
        prod = copy.deepcopy(self.__catalog.getProduct(name))
        prod.setAmount(quantity)
        prod.setPrice(str(int(quantity) * Decimal(prod.getPrice())))

        self.__cart.append(prod)

    # Input: name of product and amount 
    def removeProduct(self, name, quantity):
        for i in range(len(self.__cart)):
            if(self.__cart[i].getName() == name):
                self.__cart[i].setAmount(str(int(self.__cart[i].getAmount()) - int(quantity)))
                
                if self.__cart[i].getAmount() <= 0:
                    del self.__cart[i]
                    break

                self.__cart[i].setPrice(str(int(self.__cart[i].getAmount()) * Decimal(self.__cart[i].getPrice() / (int(self.__cart[i].getAmount()) + int(quantity)))))

                break

    def listCart(self):
        for i in self.__cart:
            print("name: {}, total price: {}, amount: {}".format(i.getName(), i.getPrice(), i.getAmount()))

    def checkOut(self):
        if self.__isGuest: 
            print("Guest cannot checkout")
            return 

        for i in self.__cart:
            prod = copy.deepcopy(self.__catalog.getProduct(i.getName()))
            self.__catalog.removeProduct(i.getName())

            prod.setAmount(str(int(prod.getAmount()) - int(i.getAmount())))

            if(int(prod.getAmount()) > 0):
                self.__catalog.addProduct(prod)

        print("Checkout complete, here is your receipt")

        self.listCart()
        
        exit()
    
    def startShopping(self):
        while(True):
            command = input("choose a command: list catalog (list) | list cart (cart) | remove product (remove) | add product (add) | checkout (check) | exit (exit)\n")

            if command == "exit":
                exit()
            elif command == "list": 
                self.__catalog.listProducts()
            elif command == "cart": 
                self.listCart()
            elif command == "add":
                name = input("name: ")
                amount = input("amount: ")
                self.addProduct(name, amount)
            elif command == "remove":
                name = input("name: ")
                amount = input("amount: ")
                self.removeProduct(name, amount)
            elif command == "check":
                self.checkOut()



    

    

